import type { APIRoute } from 'astro';

const OPENAI_ENDPOINT = 'https://api.openai.com/v1/chat/completions';
const MODEL = 'gpt-4o-mini';

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  try {
    const apiKey = import.meta.env.OPENAI_API_KEY;
    if (!apiKey) {
      return new Response(
        JSON.stringify({ error: 'OPENAI_API_KEY not configured on server' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const { text } = await request.json();
    if (!text || typeof text !== 'string') {
      return new Response(JSON.stringify({ error: 'Missing text' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const payload = {
      model: MODEL,
      messages: [
        { role: 'system', content: 'You summarize blog post drafts into a concise paragraph.' },
        { role: 'user', content: `Summarize this draft in 3-4 sentences:\n\n${text}` },
      ],
      temperature: 0.3,
      max_tokens: 180,
    };

    const res = await fetch(OPENAI_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const err = await res.text();
      return new Response(JSON.stringify({ error: 'Upstream error', detail: err }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const data = await res.json();
    const summary = data?.choices?.[0]?.message?.content?.trim();

    return new Response(JSON.stringify({ summary }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    console.error(err);
    return new Response(JSON.stringify({ error: 'Unexpected error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
