package com.example.sydneyq.lastcall2.activities.createhop

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import com.example.sydneyq.lastcall2.R

class JoinHop : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_join_hop)
        val argBundle = intent.extras.getBundle("args")
        Log.d("HOPID", argBundle.getString("hopid"))
    }
}
