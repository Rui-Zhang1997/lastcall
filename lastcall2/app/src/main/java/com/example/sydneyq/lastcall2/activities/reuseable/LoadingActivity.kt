package com.example.sydneyq.lastcall2.activities.reuseable

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.example.sydneyq.lastcall2.R
import kotlinx.android.synthetic.main.activity_loading.*

class LoadingActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_loading)
        val args: Bundle? = intent.extras
        if (args != null) {
            loading_text.setText(args.getString("text") +  "(✿˵◕‿◕˵)")
        }
    }
}
