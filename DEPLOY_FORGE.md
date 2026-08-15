# Deploying to Laravel Forge

This backend is Node/Express, not PHP — but it deploys fine on a Forge server
since Forge is really just a managed Ubuntu box + Nginx + process supervision.
The two things Forge gives PHP sites for free (a long-running process, Nginx in
front of it) we have to wire up manually for Node. That's it.

This is a **separate deployment of the same backend code** that already runs on
Vercel — same repo, same shared Postgres database — just running as a real
persistent process instead of serverless functions. That's specifically so
Socket.io (live rider tracking) actually works: it's disabled on Vercel
because serverless functions can't hold a WebSocket open, but on a real server
it just works with zero code changes (`isServerless = !!process.env.VERCEL` in
`src/index.js` becomes false here).

## 1. Create the site

- New Site in Forge, domain: your chosen subdomain (e.g. `app-api.mccshopghana.com`)
- Repository: `0boy1122/mcc-shop`, branch: `master`
- If your Forge account has native **Node.js** site support, use it and set the
  project directory to `backend/mcc-shop-backend`. If not, create a generic
  site and follow the manual Nginx step below — either way, the deploy script
  and Daemon command are the same.

## 2. Deploy script

Site → **Deploy Script**. Replace the default with:

```bash
cd $FORGE_SITE_PATH
git pull origin $FORGE_SITE_BRANCH

cd backend/mcc-shop-backend
npm ci
npm run build:prod   # prisma generate --schema=src/prisma/schema.production.prisma

# Restart the Daemon so the new code actually takes effect
sudo -S supervisorctl restart mcc-shop-backend
```

Note: schema **migrations are deliberately not run here**. `db:push:prod` changes
the live shared database (same one the website uses) — run that by hand,
once, only when you've actually changed the schema, not on every deploy.

## 3. Environment variables

Site → **Environment** (this becomes `.env` in the deploy path). Use the
**same values already set on the website's Vercel project** for `DATABASE_URL`,
so both backends read/write the same Postgres:

```
DATABASE_URL=<same Postgres URL as the website's Vercel env>
JWT_SECRET=<same as website, or a fresh one — tokens don't need to be
            cross-compatible unless you want app/website SSO>
NODE_ENV=production
PORT=5000
STAFF_PASSWORD=<pick one>
PAYSTACK_SECRET_KEY=<your real Paystack secret key>
CLIENT_URL=<not load-bearing for a native app — CORS only affects browser
            clients, so this can stay a placeholder unless you also test
            the app in a browser preview>
```

Leave `BLOB_READ_WRITE_TOKEN` unset — that's Vercel Blob specific. On Forge,
product photos and delivery-proof uploads go straight to local disk instead
(that's the bug I just fixed: the code used to force base64-in-Postgres
whenever `NODE_ENV=production`, which used to only ever mean "on Vercel." Now
it correctly only does that when `VERCEL` is actually set.)

## 4. Keep it running: Forge Daemon

Site → **Daemons** → New Daemon:

```
Command: node src/index.js
Directory: /home/forge/<your-domain>/backend/mcc-shop-backend
User: forge
```

This is what replaces Vercel's serverless functions — Forge supervises this
process, restarts it if it crashes, and keeps it alive between deploys.

## 5. Nginx (only if your Forge account has no native Node site type)

Site → **Edit Files** → Nginx config. Add inside the `server` block, above
the default PHP `location /` block:

```nginx
location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";   # required for Socket.io
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

The `Upgrade`/`Connection` headers matter — without them Nginx won't let
WebSocket connections through, which would silently defeat the entire point
of moving off Vercel.

## 6. SSL + go live

Forge auto-issues a Let's Encrypt cert once DNS for the subdomain points at
the server's IP. After the first successful deploy, confirm:

```bash
curl https://app-api.mccshopghana.com/health
```

Then update `mcc shop app/src/lib/api.js`:

```js
export const BASE_URL = "https://app-api.mccshopghana.com/api";
```
