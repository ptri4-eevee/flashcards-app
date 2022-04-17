package com.eevee.eeveeflashcards.data

import android.app.Application
import android.util.Log
import androidx.lifecycle.*
import com.eevee.eeveeflashcards.R
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.squareup.moshi.Moshi
import com.squareup.moshi.Types
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import kotlinx.coroutines.launch
import okio.buffer
import okio.source

class FlashcardViewModel(application: Application) : AndroidViewModel(application) {
    private val moshi = Moshi.Builder().add(KotlinJsonAdapterFactory()).build()
    private val moshiAdapter = moshi.adapter<List<Flashcard>>(Types.newParameterizedType(List::class.java, Flashcard::class.java))

    private lateinit var flashcards: List<Flashcard>

    private val _currentCard = MutableLiveData<Flashcard>()
    val currentCard: LiveData<Flashcard> = _currentCard

    init {
        viewModelScope.launch {
            flashcards = getFlashcards()
            getNextCard()
        }
    }

    fun getNextCard() {
        _currentCard.value = flashcards.random()
    }

    private suspend fun getFlashcards() : List<Flashcard> {
        return withContext(Dispatchers.IO) {
            getApplication<Application>()
                .applicationContext.resources.openRawResource(R.raw.data)
                .source().buffer().use {source ->
                    moshiAdapter.fromJson(source)
                }
        } ?: emptyList()
    }

}