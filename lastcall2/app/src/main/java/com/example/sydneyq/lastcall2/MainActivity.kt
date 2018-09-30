package com.example.sydneyq.lastcall2

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.text.InputFilter
import android.util.Log
import android.widget.EditText
import android.widget.Toast
import com.example.sydneyq.lastcall2.activities.createhop.JoinHop
import com.example.sydneyq.lastcall2.activities.createhop.RegisterHop
import com.example.sydneyq.lastcall2.activities.reuseable.LoadingActivity

import com.example.sydneyq.lastcall2.activities.viewhop.HopView
import com.example.sydneyq.lastcall2.api.rest.lastCallREST
import com.example.sydneyq.lastcall2.tools.startActivityWithBundle
import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import org.apache.commons.lang3.StringUtils
import java.util.concurrent.TimeUnit

class MainActivity : AppCompatActivity() {
    val TAG = "MAINACT"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        create_hop.setOnClickListener { click ->
            startActivityWithBundle(this, RegisterHop::class.java)
        }

        join_hop.setOnClickListener { click ->
            Log.e(TAG, "Registered click")
            val hopId = hop_id.text.toString()
            if (hopId.length != 4 || !StringUtils.isAlphanumeric(hopId)) {
                Toast.makeText(this, "Cannot join without a 4-character Hop ID!", Toast.LENGTH_LONG)
            } else {
                if (DEBUG != PROGSTATE.DEBUG_NO_NETWORK) {
                    startActivityWithBundle(this, LoadingActivity::class.java, addToBackstack = false)
                    lastCallREST.checkIfHopExists(hopId)
                            .subscribeOn(Schedulers.io())
                            .observeOn(AndroidSchedulers.mainThread())
                            .doOnError { Toast.makeText(this, "Invalid Hop ID. Please try again!", Toast.LENGTH_SHORT) }
                            .subscribe {
                                if (it == true) {
                                    val args = Bundle()
                                    args.putString("hopid", hopId)
                                    startActivityWithBundle(this, JoinHop::class.java, args)
                                } else {
                                    Toast.makeText(this, "Invalid Hop ID. Please try again!", Toast.LENGTH_SHORT)
                                }
                            }
                } else {
                    Log.e(TAG, "HOPID: " + hopId)
                    val args = Bundle()
                    args.putString("hopid", hopId)
                    startActivityWithBundle(this, JoinHop::class.java, args)
                }
            }
        }
    }
}

