package com.example.sydneyq.lastcall2.activities.createhop

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.EditText
import android.widget.RadioButton
import android.widget.Toast
import com.example.sydneyq.lastcall2.R
import com.example.sydneyq.lastcall2.api.models.BarHopMeta
import kotlinx.android.synthetic.main.activity_register_hop.*
import java.lang.Integer.parseInt

class RegisterHop : AppCompatActivity() {
    var currentlyChecked: RadioButton? = null
    fun setToggleListener(button: RadioButton) {
        button.setOnCheckedChangeListener { buttonView, isChecked ->
            Log.e("ISCHECKED", isChecked.toString())
            if (isChecked) {
                currentlyChecked?.isChecked = false
                currentlyChecked = button
            }
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register_hop)
        setToggleListener(toleranceLow)
        setToggleListener(toleranceMed)
        setToggleListener(toleranceHigh)
        submitHop.setOnClickListener submitlistener@{
            arrayListOf<EditText>(creatorName, hopName, hopStartTime,
                    hopCount, maxBarCost).map {
                if (it.text.toString().trim().isEmpty()) {
                    Toast.makeText(this, "Please fill out all fields!", Toast.LENGTH_SHORT)
                    return@submitlistener
                }
            }
            var tolerance = -1
            when (currentlyChecked) {
                toleranceLow -> tolerance = 1
                toleranceMed -> tolerance = 2
                toleranceHigh -> tolerance = 3
            }
            val name = creatorName.text.toString().trim()
            val hopname = hopName.text.toString().trim()
            val hopStart = hopStartTime.text.toString().trim().split(":")
            val count = parseInt(hopCount.text.toString().trim())
            val maxAmt = parseInt(maxBarCost.text.toString().trim())
            if (count < 1 || maxAmt < 1) {
                Toast.makeText(this, "All numeric fields cannot be less than one!", Toast.LENGTH_SHORT)
                return@submitlistener
            }
            if (hopStart.size != 2) {
                Toast.makeText(this, "Please enter time in 24-hour format of the form HH:mm (e.g. 23:10, 11:30)", Toast.LENGTH_LONG)
                return@submitlistener
            }
            val hr = parseInt(hopStart.get(0))
            val min = parseInt(hopStart.get(1))
            if (hr < 0 || hr > 23 || min < 0 || min > 59) {
                Toast.makeText(this, "Hours must be between 0-23, minutes must be between 0-59", Toast.LENGTH_LONG)
                return@submitlistener
            }
        }
    }
}
