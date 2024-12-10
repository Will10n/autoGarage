import com.android.build.api.variant.BuildConfigField
import com.android.builder.compiling.BuildConfigType

plugins {
    alias(libs.plugins.android.application)
}

android {
    namespace = "com.example.locationtrack"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.locationtrack"
        minSdk = 34
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"

        buildConfigField("String", "httpURL", "\"${project.properties["httpUrl"]}\"")
        buildConfigField("float", "radius", "${project.properties["radius"]}")
        buildConfigField("double", "latitude", "${project.properties["latitude"]}")
        buildConfigField("double", "longitude", "${project.properties["longitude"]}")

    }
    buildFeatures{
        buildConfig = true
    }

    buildTypes {

        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
}

dependencies {

    implementation(libs.appcompat)
    implementation(libs.material)
    implementation(libs.activity)
    implementation(libs.constraintlayout)
    implementation(libs.play.services.location)
    testImplementation(libs.junit)
    androidTestImplementation(libs.ext.junit)
    androidTestImplementation(libs.espresso.core)
}