import { defineCollection, z } from 'astro:content';

const videos = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    youtubeId: z.string(),
    thumbnail: z.string().optional(),
    tags: z.array(z.string()).default([]),
    duration: z.string().optional(),
  }),
});

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    tags: z.array(z.string()).default([]),
    youtubeId: z.string().optional(),
    heroImage: z.string().optional(),
  }),
});

export const collections = {
  videos,
  posts,
};
