package com.example.sydneyq.lastcall2.activities.createhop

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.RadioButton
import android.widget.Toast
import com.example.sydneyq.lastcall2.DEBUG
import com.example.sydneyq.lastcall2.PROGSTATE
import com.example.sydneyq.lastcall2.R
import com.example.sydneyq.lastcall2.activities.reuseable.LoadingActivity
import com.example.sydneyq.lastcall2.activities.viewhop.HopView
import com.example.sydneyq.lastcall2.api.models.HopMember
import com.example.sydneyq.lastcall2.api.rest.lastCallREST
import com.example.sydneyq.lastcall2.tools.startActivityWithBundle
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_join_hop.*
import java.lang.Integer.parseInt

class JoinHop : AppCompatActivity() {
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
        setContentView(R.layout.activity_join_hop)
        val argBundle = intent.extras.getBundle("args")
        val hopId = argBundle.getString("hopid")
        activityTitle.text = "Joining Hop ${hopId}"
        setToggleListener(toleranceLow)
        setToggleListener(toleranceMed)
        setToggleListener(toleranceHigh)
        submitHop.setOnClickListener {
            val name = memberName.text.toString()
            val maxCost = if (!maxBarCost.text.toString().trim().isEmpty()) parseInt(maxBarCost.text.toString()) else -1
            if (name.trim().isEmpty()) {
                Toast.makeText(this, "Name must not be empty!", Toast.LENGTH_SHORT)
            } else if (currentlyChecked == null) {
                Toast.makeText(this, "Please check tolerance level!", Toast.LENGTH_SHORT)
            } else if (maxCost < 1) {
                Toast.makeText(this, "Please enter a value greater than 1", Toast.LENGTH_SHORT)
            } else {
                var tolerance = -1
                when (currentlyChecked) {
                    toleranceLow -> tolerance = 1
                    toleranceMed -> tolerance = 2
                    toleranceHigh -> tolerance = 3
                }
                startActivityWithBundle(this, LoadingActivity::class.java, addToBackstack = false)
                if (DEBUG != PROGSTATE.DEBUG_NO_NETWORK) {
                    lastCallREST
                            .joinHop(hopId, HopMember("", name, tolerance, maxCost, hopId))
                            .subscribeOn(Schedulers.io())
                            .observeOn(AndroidSchedulers.mainThread())
                            .subscribe { it ->
                                val args = Bundle()
                                args.putSerializable("user", it)
                                startActivityWithBundle(this, HopView::class.java, args)
                            }
                } else {
                    val args = Bundle()
                    val member = HopMember("12344asdfko4", name, tolerance, maxCost, hopId)
                    args.putSerializable("user", member)
                    startActivityWithBundle(this, HopView::class.java, args)
                }
            }
        }
    }
}
