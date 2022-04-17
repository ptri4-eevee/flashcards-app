package com.eevee.eeveeflashcards

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.navigation.fragment.findNavController
import com.eevee.eeveeflashcards.data.FlashcardViewModel
import com.eevee.eeveeflashcards.databinding.FragmentFlashcardBinding

class FlashcardFragment: Fragment() {

    private lateinit var binding: FragmentFlashcardBinding

    private val flashcardViewModel: FlashcardViewModel by activityViewModels()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        binding = FragmentFlashcardBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding?.apply {
            viewModel = flashcardViewModel
            lifecycleOwner = viewLifecycleOwner
            fragment = this@FlashcardFragment
        }
    }

    fun goToDetail() {
        findNavController().navigate(R.id.action_flashcardFragment_to_flashcardChallengeFragment)
    }
}