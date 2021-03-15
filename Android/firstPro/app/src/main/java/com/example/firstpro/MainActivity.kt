package com.example.firstpro

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.layout_test)
    }

    fun okClick(view: View){
        Toast.makeText(this@MainActivity, "Ok clicked", Toast.LENGTH_SHORT).show()
    }

    fun cancelClick(view: View){
        Toast.makeText(this@MainActivity, "Cancel clicked", Toast.LENGTH_SHORT).show()
    }
}