/**
 * Uno Más — Web Design System components (reference implementation)
 * Self-contained React + inline styles using the brand tokens.
 * These mirror the live site (homepage hero, /about timeline, Fiesta Box page)
 * and are the canonical components for Claude Design / new builds.
 *
 * Load fonts once in the app head:
 *   https://fonts.googleapis.com/css2?family=Antonio:wght@400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap
 */
import React, { useEffect, useRef, useState } from "react";

export const tokens = {
  navy: "#06243F", navy2: "#0C3D72", pink: "#E22690", blue: "#18BCDC",
  yellow: "#FFEC00", magenta: "#BF28BF", orange: "#E8761B",
  ink: "#0A1F33", muted: "#5A6B7B", line: "#E6E9EE", paper: "#FAF8F4", white: "#FFFFFF",
  display: '"Antonio","Helvetica Neue",Arial,sans-serif',
  body: '"Montserrat",-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif',
  iconPattern: "https://res.cloudinary.com/drxrfyq9i/image/upload/w_2200/uno-mas/website/icons/icons-pattern-forramsey-02-1.png",
};

/* ---------- Type ---------- */
export const Eyebrow = ({ children, color = tokens.pink }: { children: React.ReactNode; color?: string }) => (
  <p style={{ fontFamily: tokens.body, fontWeight: 700, textTransform: "uppercase", letterSpacing: ".26em", fontSize: 12, color }}>{children}</p>
);

export const Display = ({ children, style }: { children: React.ReactNode; style?: React.CSSProperties }) => (
  <h2 style={{ fontFamily: tokens.display, fontWeight: 600, textTransform: "uppercase", letterSpacing: ".01em", lineHeight: .95, color: tokens.navy, fontSize: "clamp(2rem,4.6vw,3.4rem)", ...style }}>{children}</h2>
);

/* ---------- Buttons ---------- */
type BtnProps = { children: React.ReactNode; href?: string; variant?: "primary" | "sun" | "ghost"; onDark?: boolean };
export function Button({ children, href = "#", variant = "primary", onDark = false }: BtnProps) {
  const base: React.CSSProperties = {
    display: "inline-flex", alignItems: "center", justifyContent: "center",
    fontFamily: tokens.body, fontWeight: 700, textTransform: "uppercase", letterSpacing: ".04em",
    fontSize: 15, padding: "15px 28px", borderRadius: 999, textDecoration: "none", border: "2px solid transparent",
  };
  const variants: Record<string, React.CSSProperties> = {
    primary: { background: tokens.pink, color: "#fff", boxShadow: "0 8px 0 #9c1163" },
    sun: { background: tokens.yellow, color: tokens.navy, boxShadow: "0 8px 0 #b8a800" },
    ghost: onDark
      ? { background: "rgba(255,255,255,.16)", color: "#fff", borderColor: "#fff" }
      : { background: "#fff", color: tokens.navy, borderColor: tokens.navy },
  };
  return <a href={href} style={{ ...base, ...variants[variant] }}>{children}</a>;
}

/* ---------- Badges ---------- */
// Yellow "stamp" used for product/section titles (e.g. "Fiesta Boxes To-Go", "Add-Ons")
export const TitleBadge = ({ children }: { children: React.ReactNode }) => (
  <span style={{ display: "inline-block", background: tokens.yellow, color: tokens.navy, fontFamily: tokens.display, fontWeight: 700, textTransform: "uppercase", letterSpacing: ".04em", fontSize: "clamp(1.05rem,2vw,1.6rem)", padding: "9px 18px", borderRadius: 12, transform: "rotate(-2deg)", boxShadow: "0 8px 22px rgba(0,0,0,.28)" }}>{children}</span>
);

// Pink "Pro tip" sticker (pulse). Place over imagery.
export function ProTipSticker({ label = "Pro tip", children }: { label?: string; children: React.ReactNode }) {
  return (
    <div style={{ maxWidth: 300, background: tokens.pink, color: "#fff", border: "2px solid #fff", borderRadius: 16, padding: "17px 21px", fontSize: 15.5, lineHeight: 1.35, fontWeight: 700, boxShadow: "0 12px 26px rgba(0,0,0,.4)", animation: "umPulse 1.8s ease-in-out infinite" }}>
      <b style={{ display: "block", color: tokens.yellow, fontSize: 13, textTransform: "uppercase", letterSpacing: ".05em", marginBottom: 2 }}>{label}</b>
      {children}
    </div>
  );
}

/* ---------- Ticket card (add-ons / feature trios) ---------- */
export function TicketCard({ icon, title, body, tag }: { icon?: React.ReactNode; title: string; body: string; tag?: string }) {
  return (
    <div style={{ position: "relative", flex: 1, minWidth: 240, background: "#fff", color: tokens.navy, padding: "26px 24px", borderRadius: 14, borderLeft: "2px dashed #cfd6de", boxShadow: "0 18px 40px rgba(0,0,0,.34)" }}>
      {tag && <span style={{ position: "absolute", top: 18, right: 20, background: tokens.pink, color: "#fff", fontWeight: 800, fontSize: 11, letterSpacing: ".06em", textTransform: "uppercase", padding: "5px 11px", borderRadius: 999 }}>{tag}</span>}
      {icon && <div style={{ width: 88, height: 88, borderRadius: "50%", background: "#F4F6F8", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: 14, overflow: "hidden" }}>{icon}</div>}
      <h3 style={{ fontFamily: tokens.display, fontWeight: 600, textTransform: "uppercase", fontSize: 23, marginBottom: 6 }}>{title}</h3>
      <p style={{ fontFamily: tokens.body, fontSize: 14, color: "#43586c", lineHeight: 1.45 }}>{body}</p>
    </div>
  );
}

/* ---------- Section shells ---------- */
export const SECTION_PAD = "clamp(40px,5.5vw,96px)";

// Light section with subtle navy brand-icon scatter (seamless cover, slight rotation)
export function ScatterSection({ children, tint = "06243F" }: { children: React.ReactNode; tint?: string }) {
  return (
    <section style={{ position: "relative", overflow: "hidden", background: "#fff", padding: `${SECTION_PAD}` }}>
      <div aria-hidden style={{ position: "absolute", inset: "-26%", backgroundImage: `url(https://res.cloudinary.com/drxrfyq9i/image/upload/w_2200/e_colorize,co_rgb:${tint}/uno-mas/website/icons/icons-pattern-forramsey-02-1.png)`, backgroundSize: "cover", backgroundPosition: "center", opacity: .06, transform: "rotate(-8deg)", pointerEvents: "none" }} />
      <div style={{ position: "relative", zIndex: 2, maxWidth: 1200, margin: "0 auto" }}>{children}</div>
    </section>
  );
}

// Navy feature section (e.g. "Three venues", "Add-Ons")
export const NavySection = ({ children }: { children: React.ReactNode }) => (
  <section style={{ background: tokens.navy, color: "#fff", padding: SECTION_PAD }}>
    <div style={{ maxWidth: 1200, margin: "0 auto" }}>{children}</div>
  </section>
);

// Gradient CTA band
export const CtaBand = ({ children }: { children: React.ReactNode }) => (
  <section style={{ background: "linear-gradient(135deg,#18BCDC,#E22690)", color: "#fff", textAlign: "center", padding: SECTION_PAD }}>{children}</section>
);

/* ---------- Typewriter (rotating phrase, e.g. "Great for ___") ---------- */
export function Typewriter({ phrases, color = tokens.pink }: { phrases: string[]; color?: string }) {
  const [text, setText] = useState("");
  const i = useRef(0); const pos = useRef(0); const del = useRef(false);
  useEffect(() => {
    if (window.matchMedia?.("(prefers-reduced-motion: reduce)").matches) { setText(phrases[0]); return; }
    let t: any;
    const tick = () => {
      const p = phrases[i.current];
      if (!del.current) { pos.current++; setText(p.slice(0, pos.current)); if (pos.current >= p.length) { del.current = true; t = setTimeout(tick, 1200); return; } }
      else { pos.current--; setText(p.slice(0, pos.current)); if (pos.current <= 0) { del.current = false; i.current = (i.current + 1) % phrases.length; t = setTimeout(tick, 260); return; } }
      t = setTimeout(tick, del.current ? 40 : 78);
    };
    tick(); return () => clearTimeout(t);
  }, [phrases]);
  return <span style={{ color, borderBottom: "0" }}>{text}<span style={{ borderLeft: "0.06em solid currentColor", marginLeft: ".04em" }} /></span>;
}

/* Keyframes — inject once at app root */
export const UnoMasKeyframes = () => (
  <style>{`
    @keyframes umPulse{0%,100%{transform:rotate(-3deg) scale(1)}50%{transform:rotate(-3deg) scale(1.06)}}
    @media (prefers-reduced-motion: reduce){*{animation:none!important}}
  `}</style>
);
