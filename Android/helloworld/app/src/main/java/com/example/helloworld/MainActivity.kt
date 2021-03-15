package com.example.helloworld

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Toast


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("Son", "onCreate()호출")
        setContentView(R.layout.activity_main)
    }

    //Activity의 life cycle
    override fun onStart() {
        super.onStart()
        Log.d("Son", "onStart()호출")
    }

    override fun onResume() {
        super.onResume()
        Log.d("Son", "onResume()호출")
    }

    override fun onPause() {
        super.onPause()
        Log.d("Son", "onPause()호출")
    }

    override fun onStop() {
        super.onStop()
        Log.d("Son", "onStop()호출")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("Son", "onDestroy()호출")
    }

    //
    fun btnclick(view: View){
        Log.d("Son", "버튼이 눌러졌습니다.")
    }
}