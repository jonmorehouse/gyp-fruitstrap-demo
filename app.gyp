{

	# initialize global variables as needed for application
	"variables" : {

		# sdk version of application being used
		"ios_sdk_version": "7.0",

		# sdk directory that we are currently using
		"ios_sdk_dir": "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS"
	},

	# global conditions for application
	"target_defaults" : {

		"link_settings": {

			"libraries": [

				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/CoreGraphics.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/CoreText.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/Foundation.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/ImageIO.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/MobileCoreServices.framework",
				"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/UIKit.framework",
			],
		}

	}, # GLOBAL CONDITIONS ETC

	"targets": [
		{
			"target_name": "PulsePoll",
			"type": "executable",
			"mac_bundle": 1,
			"include_dirs" : [

			],

			"sources": [

			],

			"link_settings": {
				
				# default libraries to not include
				"libraries!": [

					"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/MobileCoreServices.framework",
					"<(ios_sdk_dir)<(ios_sdk_version).sdk/System/Library/Frameworks/UIKit.framework",
				]
			},

			"xcode_settings" : {

				"INFOPLIST_FILE" : "src/substructure/PulsePoll-Info.plist",
				"SDKROOT": "iphoneos",
				"TARGETED_DEVICE_FAMILY": "1,2",
				"CODE_SIGN_IDENTITY": "iPhone Developer",
				"IPHONEOS_DEPLOYMENT_TARGET": "5.0",
				"ARCHS": "$(ARCHS_UNIVERSAL_IPHONE_OS)",
				"HEADER_SEARCH_PATHS": "$(inherited)",
				"CLANG_ENABLE_OBJC_ARC": "YES",
			},
		}, # end of target
	]# end of all targets



}