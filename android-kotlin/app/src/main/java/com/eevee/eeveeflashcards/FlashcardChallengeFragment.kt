package com.eevee.eeveeflashcards

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import com.eevee.eeveeflashcards.data.FlashcardViewModel
import com.eevee.eeveeflashcards.databinding.FragmentChallengeBinding

class FlashcardChallengeFragment: Fragment() {

    private lateinit var binding: FragmentChallengeBinding

    private val flashcardViewModel: FlashcardViewModel by activityViewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentChallengeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding?.apply {
            viewModel = flashcardViewModel
            lifecycleOwner = viewLifecycleOwner
            fragment = this@FlashcardChallengeFragment
        }
    }

    fun showAnswer() {
        Log.d("FRAG", "answer")
        binding.answerText.visibility = View.VISIBLE
    }

}