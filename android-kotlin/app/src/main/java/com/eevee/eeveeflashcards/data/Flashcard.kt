package com.eevee.eeveeflashcards.data

data class Flashcard(
    val id: Int,
    val name: String,
    val description: String,
    val challengeQuestion: String,
    val challengeAnswer: String
)