import { pgTable, serial, text, varchar, integer, boolean, json, timestamp } from "drizzle-orm/pg-core";

// Extend the default user schema to include hardware/software background
export const users = pgTable("user", {
  id: serial("id").primaryKey(),
  email: varchar("email", { length: 255 }).notNull().unique(),
  emailVerified: boolean("email_verified").default(false),
  hashedPassword: varchar("hashed_password", { length: 255 }).notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
  
  // Extended fields for hardware/software background
  softwareExperience: varchar("software_experience", { length: 50 }).default("beginner").notNull(),
  hardwareExperience: varchar("hardware_experience", { length: 50 }).default("none").notNull(),
  programmingLanguages: json("programming_languages").default([]),
  fieldOfInterest: varchar("field_of_interest", { length: 100 }).default(""),
  educationalAffiliation: varchar("educational_affiliation", { length: 100 }).default(""),
  personalizationEnabled: boolean("personalization_enabled").default(false),
  bonusPoints: integer("bonus_points").default(0).notNull(),
  avatar: varchar("avatar", { length: 255 })
});

// Sessions table (handled by better-auth)
// Accounts table (handled by better-auth)
// Verification tokens table (handled by better-auth)