package com.example.sydneyq.lastcall2.tools

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import java.util.*

fun <T: Any> startActivityWithBundle(currentActivity: Activity,
                                    targetActivity: Class<T>,
                                    bundle: Bundle? = null,
                                     addToBackstack: Boolean = true) : Unit {
    val intent = Intent(currentActivity, targetActivity).apply {
        putExtra("args", bundle)
    }
    if (!addToBackstack) {
        intent.addFlags(Intent.FLAG_ACTIVITY_NO_HISTORY)
    }
    currentActivity.startActivity(intent)
}

fun <T: Any, K: Any> goToLoadingPageUntilCallCompleted(currentActivity: Activity,
                                               targetActivity: Class<T>,
                                               bundle: Bundle?,
                                               fn: (Observable) -> Unit) {

}
