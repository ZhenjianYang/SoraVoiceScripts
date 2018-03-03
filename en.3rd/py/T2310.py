from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2310   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Zack',                                 # 9
        'Solomon',                              # 10
        'Clem',                                 # 11
        'Daniel',                               # 12
        'Elder Serge',                          # 13
        'Amelia',                               # 14
        'Sadie',                                # 15
        'Matron Theresa',                       # 16
        'Fisher',                               # 17
        'Creda',                                # 18
        'Target Camera',                        # 19
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01460 ._CH',             # 01
        'ED6_DT07/CH02590 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01050 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH02570 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01010 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01460P._CP',             # 01
        'ED6_DT07/CH02590P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01050P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH02570P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01010P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -28110,
        Z                   = 0,
        Y                   = 7510,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -29710,
        Z                   = 0,
        Y                   = 42820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28520,
        Z                   = 0,
        Y                   = 41210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -31800,
        Z                   = 0,
        Y                   = 39140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -31960,
        Z                   = 0,
        Y                   = 42210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -29220,
        Z                   = 0,
        Y                   = 38160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_328",          # 01, 1
        "Function_2_32F",          # 02, 2
        "Function_3_4AC",          # 03, 3
        "Function_4_8B8",          # 04, 4
        "Function_5_DA1",          # 05, 5
        "Function_6_137D",         # 06, 6
        "Function_7_16D7",         # 07, 7
        "Function_8_1B3C",         # 08, 8
        "Function_9_1CD9",         # 09, 9
        "Function_10_20F8",        # 0A, 10
        "Function_11_2215",        # 0B, 11
        "Function_12_2CD3",        # 0C, 12
        "Function_13_2CEC",        # 0D, 13
        "Function_14_2D8E",        # 0E, 14
        "Function_15_2E17",        # 0F, 15
        "Function_16_2E6F",        # 10, 16
        "Function_17_2ED3",        # 11, 17
        "Function_18_2F32",        # 12, 18
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -27000, 0, 39020, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30800, 0, 44300, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_2CD")
    SetChrPos(0x14, -31740, 0, 40230, 180)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, -29710, 0, 42820, 0)
    Jump("loc_303")

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_2D7")
    Jump("loc_303")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_2F2")
    SetChrPos(0x15, -1740, 0, 7940, 0)
    Jump("loc_303")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_2FC")
    Jump("loc_303")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_303")

    label("loc_303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    Event(0, 11)

    label("loc_327")

    Return()

    # Function_0_25A end

    def Function_1_328(): pass

    label("Function_1_328")

    OP_71(0x400, 0x0)
    ExitThread()
    Return()

    # Function_1_328 end

    def Function_2_32F(): pass

    label("Function_2_32F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_496")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_496")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_496")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_39F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_496")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_496")

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_496")

    label("loc_3EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_496")

    label("loc_403")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_496")

    label("loc_41C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_496")

    label("loc_435")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_496")

    label("loc_44E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_496")

    label("loc_467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_496")

    label("loc_480")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_4AB")

    Return()

    # Function_2_32F end

    def Function_3_4AC(): pass

    label("Function_3_4AC")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_5B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4FB")

    ChrTalk(    #0
        0x10,
        (
            "This is the kinda work I was born for, if you ask\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B4")

    label("loc_4FB")


    ChrTalk(    #1
        0x10,
        (
            "Some of the profits from this bazaar go towards\x01",
            "the running costs of the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "Fun to do and for a good cause! This is the kind\x01",
            "of work I was born for, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5B4")

    Jump("loc_8B4")

    label("loc_5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_643")

    ChrTalk(    #3
        0x10,
        "...Well, whatever. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "That guy who's always helping us out is pitching in,\x01",
            "so we should be fine even without them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725")

    label("loc_643")


    ChrTalk(    #5
        0x10,
        (
            "Come to think of it, we sent a request to the\x01",
            "Bracer Guild to help with the bazaar a while back,\x01",
            "didn't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "Still haven't seen anyone that meets that description\x01",
            "around, though... I wonder if they're even coming.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_725")

    Jump("loc_8B4")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_8A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_793")

    ChrTalk(    #7
        0x10,
        "Everything here costs 20 mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "I'll go as low as 10 mira for you girls, though!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_793")


    ChrTalk(    #9
        0x10,
        (
            "Welcome! Go ahead and let me know if anything\x01",
            "catches your eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "...Wait. Aren't you the kids from the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "Eh, no biggie. Offer still stands--let me know\x01",
            "if you see anything you want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "I'll knock a bit off the price, too, just for you\x01",
            "kids.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8A0")

    Jump("loc_8B4")

    label("loc_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_8AD")
    Jump("loc_8B4")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_8B4")

    label("loc_8B4")

    TalkEnd(0x10)
    Return()

    # Function_3_4AC end

    def Function_4_8B8(): pass

    label("Function_4_8B8")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_993")

    ChrTalk(    #13
        0x11,
        "While you're here, why not take a look around?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "You don't even need to buy anything if you don't\x01",
            "want to. Enjoying festivals is more about taking\x01",
            "in the atmosphere than opening your wallet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A94")

    label("loc_993")


    ChrTalk(    #15
        0x11,
        (
            "From what I remember, it was originally a Jenis\x01",
            "student who thought up the idea of holding the\x01",
            "bazaar here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "It's hard to imagine the town without it now,\x01",
            "though. It's one of our major attractions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "I mean, who doesn't love a good festival?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A94")

    Jump("loc_D9D")

    label("loc_A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B6E")

    ChrTalk(    #18
        0x11,
        (
            "Me and Zack are the only real organizers of\x01",
            "this event, so it feels kinda weird to call us its\x01",
            "organization committee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x11,
        (
            "...but two people's still technically a committee,\x01",
            "right? Riiight?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C36")

    label("loc_B6E")


    ChrTalk(    #20
        0x11,
        (
            "This is the third year this bazaar's been held,\x01",
            "actually. We have people who come every year,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "Makes me really giddy as someone who's been\x01",
            "involved in it since its humble beginnings.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C36")

    Jump("loc_D9D")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_D8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #22
        0x11,
        (
            "Sorry! I've told you all I know about that story.\x02\x03",

            "All I know is it's some old legend I picked up\x01",
            "from my old man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D89")

    label("loc_CC2")


    ChrTalk(    #23
        0x11,
        "Oh, heya. Come to ask more about that story?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "If you have, I can't help you, though. Sorry!\x01",
            "I've told you all I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "All I know is it's some old legend I picked up\x01",
            "from my old man.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D89")

    Jump("loc_D9D")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_D96")
    Jump("loc_D9D")

    label("loc_D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_D9D")

    label("loc_D9D")

    TalkEnd(0x11)
    Return()

    # Function_4_8B8 end

    def Function_5_DA1(): pass

    label("Function_5_DA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_F40")
    OP_8C(0xFE, 180, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E33")

    ChrTalk(    #26
        0xFE,
        (
            "I really do think you're worried about nothing,\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "More than anything, the children just want your\x01",
            "smile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3D")

    label("loc_E33")


    ChrTalk(    #28
        0xFE,
        "I think she's a lovely child, personally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "She's remarkably levelheaded for one her age,\x01",
            "too. I don't think you have anything to worry\x01",
            "about with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Especially as I'm sure she still has plenty of\x01",
            "growing and maturing to do. It's what children\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F3D")

    Jump("loc_1379")

    label("loc_F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_108A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FC9")

    ChrTalk(    #31
        0xFE,
        (
            "The young people of the village are so fired up\x01",
            "because of the bazaar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Hoho! That makes me very happy indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1087")

    label("loc_FC9")


    ChrTalk(    #33
        0xFE,
        (
            "There don't seem to have been many monsters\x01",
            "out on the Gull Seaside Way this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "...but apparently, that's thanks to someone who\x01",
            "took care of them because of the bazaar.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1087")

    Jump("loc_1379")

    label("loc_108A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_119B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1104")

    ChrTalk(    #35
        0xFE,
        (
            "I'm quite interested in seeing what's on sale at\x01",
            "this year's bazaar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "I can hardly wait to see!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1104")


    ChrTalk(    #37
        0xFE,
        (
            "I think I should go and have a look at how things\x01",
            "are doing soon myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I'm quite interested in seeing what's on sale this\x01",
            "year, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1198")

    Jump("loc_1379")

    label("loc_119B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_1372")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1264")

    ChrTalk(    #39
        0xFE,
        (
            "The cabin the bazaar is taking place in is on the\x01",
            "plateau at the edge of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "If you're interested, I suggest you run along and\x01",
            "see what's on offer. I'm sure you'd love it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136F")

    label("loc_1264")


    ChrTalk(    #41
        0xFE,
        "Well, well! if it isn't Matron Theresa's children.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Hoho! Surprised how lively it is in town?\x01",
            "Well, there's a bazaar being held in the\x01",
            "windmill cabin now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "If you're interested, I suggest you run along and see\x01",
            "what's on offer. I'm sure you'd love it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_136F")

    Jump("loc_1379")

    label("loc_1372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_1379")

    label("loc_1379")

    TalkEnd(0xFE)
    Return()

    # Function_5_DA1 end

    def Function_6_137D(): pass

    label("Function_6_137D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13B6")

    ChrTalk(    #44
        0xFE,
        "Now, what should I buy next? ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_1430")

    label("loc_13B6")


    ChrTalk(    #45
        0xFE,
        "Heehee. One pot, bought!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "I should've known I'd find one here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "You really CAN find anything at a bazaar.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1430")

    Jump("loc_16D3")

    label("loc_1433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_158B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14DC")

    ChrTalk(    #48
        0xFE,
        (
            "Come to think of it, I could probably do with\x01",
            "a new pot after burning the last one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I wonder if any of those will be on sale at the\x01",
            "bazaar...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_14DC")


    ChrTalk(    #50
        0xFE,
        "Zack's been helping out at the bazaar every year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "He wasn't very reliable as a child, what with him\x01",
            "always getting lost all the time, but he certainly\x01",
            "is now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1588")

    Jump("loc_16D3")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_16CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_162A")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #52
        0xFE,
        (
            "I'm sure I had a bunch of my own old clothes\x01",
            "somewhere around here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Where are they, though? I can't find them \x01",
            "anywhere...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_162A")


    ChrTalk(    #54
        0xFE,
        (
            "Hmm... Do we have anything that could be sold\x01",
            "at the bazaar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "There's Zack's old clothes, but I'm guessing no \x01",
            "one would buy those ratty things...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_16C9")

    Jump("loc_16D3")

    label("loc_16CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_16D3")

    label("loc_16D3")

    TalkEnd(0xFE)
    Return()

    # Function_6_137D end

    def Function_7_16D7(): pass

    label("Function_7_16D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_171D")

    ChrTalk(    #56
        0xFE,
        "I'd love to hold fishing classes for children here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B38")

    label("loc_171D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_1892")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1803")

    ChrTalk(    #57
        0xFE,
        (
            "By my reckoning, the rest of the week will be\x01",
            "clear skies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "First-rate fishermen are quite sensitive to small \x01",
            "changes in the weather. It's not hard to tell what\x01",
            "it's going to be like in the near future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188F")

    label("loc_1803")


    ChrTalk(    #59
        0xFE,
        (
            "Today's weather seems to be quite fine!\x01",
            "Yes, indeedy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I might even take up my rod and do a little\x01",
            "fishing near the lighthouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_188F")

    Jump("loc_1B38")

    label("loc_1892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1900")

    ChrTalk(    #61
        0xFE,
        "This is a wonderful little village, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "It's an excellent fishing spot, too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B5")

    label("loc_1900")


    ChrTalk(    #63
        0xFE,
        "I come here every year...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "...and I always find myself thinking what\x01",
            "a lovely place it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I hope I can live in a village as peaceful as\x01",
            "this when I reach old age.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_19B5")

    Jump("loc_1B38")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_1B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1A80")

    ChrTalk(    #66
        0xFE,
        (
            "I hear there's a very capable fisherman in this\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I'd love to invite them to become a member of\x01",
            "our guild. Oh, the things we enthusiasts could\x01",
            "learn from one another!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B2E")

    label("loc_1A80")


    ChrTalk(    #68
        0xFE,
        (
            "I found the most spectacular rod at this very\x01",
            "bazaar one year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "It was handmade, too, and clearly used lovingly\x01",
            "for a long time. Glad I snagged it while I could!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1B2E")

    Jump("loc_1B38")

    label("loc_1B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_1B38")

    label("loc_1B38")

    TalkEnd(0xFE)
    Return()

    # Function_7_16D7 end

    def Function_8_1B3C(): pass

    label("Function_8_1B3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BCB")

    ChrTalk(    #70
        0xFE,
        (
            "There are things here today that I donated myself,\x01",
            "too, so take a look around. You never know what\x01",
            "could sing to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAD")

    label("loc_1BCB")


    ChrTalk(    #71
        0xFE,
        "Welcome! Great weather today, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Everything here was donated by the people\x01",
            "of Manoria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Heehee. There are even things here that were\x01",
            "donated by me! So do take a look around and\x01",
            "see if anything sings to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1CAD")

    Jump("loc_1CD5")

    label("loc_1CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_1CBA")
    Jump("loc_1CD5")

    label("loc_1CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_1CC4")
    Jump("loc_1CD5")

    label("loc_1CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_1CCE")
    Jump("loc_1CD5")

    label("loc_1CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_1CD5")

    label("loc_1CD5")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B3C end

    def Function_9_1CD9(): pass

    label("Function_9_1CD9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_20CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 2)), scpexpr(EXPR_END)), "loc_1E82")
    OP_8C(0x17, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1D89")

    ChrTalk(    #74
        0x17,
        (
            "#754FI can't help but worry she's got it into her\x01",
            "head that she might become a burden to me\x01",
            "if she doesn't try to do everything she can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7F")

    label("loc_1D89")


    ChrTalk(    #75
        0x17,
        (
            "#754FI know how levelheaded she is better than\x01",
            "anyone...\x02\x03",

            "#757F...but with the way she is, I'm worried she'll always\x01",
            "find herself being relied on. I want her to feel like\x01",
            "she can actually act her age from time to time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14E,
        "#1713F(...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1E7F")

    Jump("loc_20CC")

    label("loc_1E82")


    ChrTalk(    #77
        0x17,
        "#753FMary? Whatever happened to Polly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x14E,
        (
            "#1713FW-Well...\x02\x03",

            "She's...playing with Clem and Daniel right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x17,
        (
            "#750FOh...\x02\x03",

            "#754FWell, that's all right, but if anything was to\x01",
            "happen, you would tell me, wouldn't you?\x02\x03",

            "I don't want you thinking you have to bottle things\x01",
            "up and deal with them yourself. I'm always here if\x01",
            "you need me, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x14E,
        (
            "#1714FTh-Thank you!\x02\x03",

            "#1712F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x14E,
        (
            "#1713F(I can't... I just can't.)\x02\x03",

            "(Mentioning the present thing to her is out\x01",
            "of the question, and Polly disappearing is all\x01",
            "my fault.)\x02\x03",

            "#1713F(I'll have to see if I can find her myself...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3A)

    label("loc_20CC")

    Jump("loc_20F4")

    label("loc_20CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_20D9")
    Jump("loc_20F4")

    label("loc_20D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_20E3")
    Jump("loc_20F4")

    label("loc_20E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_20ED")
    Jump("loc_20F4")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_20F4")

    label("loc_20F4")

    TalkEnd(0xFE)
    Return()

    # Function_9_1CD9 end

    def Function_10_20F8(): pass

    label("Function_10_20F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_21EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2182")

    ChrTalk(    #82
        0xFE,
        "I'm glad someone wanted that pot I donated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "It's always a relief to see things you donate\x01",
            "go to good homes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E9")

    label("loc_2182")


    ChrTalk(    #84
        0xFE,
        (
            "Oh, my! I'm surprised the pot I donated sold\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Someone must have really wanted it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_21E9")

    Jump("loc_2211")

    label("loc_21EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_21F6")
    Jump("loc_2211")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_2200")
    Jump("loc_2211")

    label("loc_2200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_220A")
    Jump("loc_2211")

    label("loc_220A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_2211")

    label("loc_2211")

    TalkEnd(0xFE)
    Return()

    # Function_10_20F8 end

    def Function_11_2215(): pass

    label("Function_11_2215")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_4A(0x11, 255)
    OP_4A(0x10, 255)
    SetChrFlags(0x14E, 0x40)
    SetChrFlags(0x14F, 0x40)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrPos(0x14E, -30500, -500, 34700, 0)
    SetChrPos(0x14F, -29780, -500, 34700, 0)
    OP_9F(0x14E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-29140, 0, 47160, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(55000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)

    def lambda_22C7():
        OP_6D(-29140, 0, 39160, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_22C7)

    def lambda_22DF():
        OP_6B(2720, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_22DF)

    def lambda_22EF():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_22EF)
    Sleep(5000)

    def lambda_2304():
        OP_8E(0xFE, 0xFFFF8878, 0x0, 0x8F34, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2304)

    def lambda_231F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_231F)
    Sleep(300)

    def lambda_2336():
        OP_8E(0xFE, 0xFFFF8B48, 0x0, 0x8D40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2336)

    def lambda_2351():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14F, 2, lambda_2351)
    OP_0D()
    WaitChrThread(0x1A, 0x1)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x14F, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_43(0x14E, 0x3, 0x0, 0xC)
    OP_8C(0x14F, 45, 400)
    Sleep(500)
    OP_8C(0x14F, 0, 400)
    Sleep(500)
    OP_8C(0x14F, 45, 400)
    Sleep(400)

    ChrTalk(    #86
        0x14F,
        "#1733FWow... This is so cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x14E,
        (
            "#1714F#12PYeah... There's so much available here.\x02\x03",

            "#1719FI wonder if there's anything that would make\x01",
            "a good present for the matron.\x02\x03",

            "There has to be with all that's here...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2479():
        OP_6D(-28370, 0, 39810, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2479)
    OP_43(0x14E, 0x2, 0x0, 0xD)
    OP_43(0x14F, 0x2, 0x0, 0xE)
    WaitChrThread(0x14F, 0x2)
    WaitChrThread(0x1A, 0x0)
    SetChrPos(0x12, -30080, -500, 34500, 0)
    SetChrPos(0x13, -30080, -500, 34500, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x6, 0x0, 0x64)
    OP_43(0x12, 0x3, 0x0, 0xF)
    OP_43(0x13, 0x3, 0x0, 0x10)
    OP_62(0x14F, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x14F)
    OP_8C(0x14F, 180, 400)
    Sleep(200)
    OP_8C(0x10, 225, 400)
    WaitChrThread(0x13, 0x3)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(100)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(500)
    OP_62(0x12, 0x0, 1600, 0x26, 0x27, 0xC8, 0x5)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x12)
    OP_63(0x10)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(500)
    OP_8C(0x13, 0, 400)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(100)
    OP_95(0x12, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    Sleep(500)
    OP_62(0x12, 0x0, 1600, 0x26, 0x27, 0xC8, 0x5)
    Sleep(300)
    OP_62(0x14F, 0x0, 1600, 0x26, 0x27, 0xC8, 0x2)
    Sleep(1000)
    OP_63(0x12)
    OP_63(0x14F)
    Sleep(1000)
    OP_43(0x12, 0x3, 0x0, 0x11)
    OP_43(0x13, 0x3, 0x0, 0x12)
    WaitChrThread(0x13, 0x3)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x10, 270, 400)
    Sleep(200)
    OP_8C(0x14F, 90, 400)

    def lambda_265F():
        OP_6D(-29390, 0, 44230, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_265F)

    def lambda_2677():
        OP_6B(2730, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2677)

    def lambda_2687():
        OP_6C(39000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2687)
    WaitChrThread(0x1A, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0x14E, 0x2)
    OP_63(0x14E)
    OP_8C(0x14E, 45, 400)
    Sleep(500)

    ChrTalk(    #88
        0x14E,
        (
            "#1900F#12P(A bazaar actually seems like the kind of\x01",
            "place you might accidentally stumble upon\x01",
            "magical items like the happiness stone...)\x02\x03",

            "#1900F(...but I wouldn't even know where to start.\x01",
            "Nothing I see looks like it, anyway...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x11,
        (
            "#5PThere something in particular you're looking\x01",
            "for that I could help with?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x14E, 0, 400)

    ChrTalk(    #90
        0x14E,
        (
            "#1714F#12PU-Umm...\x02\x03",

            "#1900F(M-Maybe it won't hurt to ask.)\x02\x03",

            "#1718FSir? Do you happen to know where I can\x01",
            "find a happiness stone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        "#5P...A what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x14E,
        (
            "#1710F#12PIt's a stone that makes people happy just\x01",
            "for owning it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        "#5PI... Uhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        (
            "#5PAhaha. I really couldn't tell you. Sorry,\x01",
            "sweetie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x14E,
        (
            "#1713F#12PTh-That's all right...\x02\x03",

            "#1716FSorry for the trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 400)
    Sleep(300)

    def lambda_2991():
        OP_8E(0xFE, 0xFFFF88FA, 0x0, 0xA0E6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2991)

    def lambda_29AC():
        OP_6D(-29590, 0, 43800, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_29AC)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(    #96
        0x11,
        "#5PHmm...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x1A, 0x0)

    ChrTalk(    #97
        0x11,
        (
            "#5PYou know, I do remember hearing a funny story\x01",
            "about the Krone mountains one time that might\x01",
            "be worth hearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x11,
        (
            "#5PI've got no idea if it's true or a bunch of hooey,\x01",
            "but would you like to hear it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 600)
    Sleep(400)

    ChrTalk(    #99
        0x14E,
        "#1718F#12PY-Yes, please!\x02",
    )

    CloseMessageWindow()

    def lambda_2AEE():
        OP_6D(-29600, 0, 44770, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2AEE)
    OP_8E(0x14E, 0xFFFF8774, 0x0, 0xA604, 0x5DC, 0x0)
    WaitChrThread(0x1A, 0x0)
    Sleep(300)

    ChrTalk(    #100
        0x11,
        "#5PIt's an old story I heard from my dad a while back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#5PSomething about them glowing gold all of a sudden\x01",
            "once a year. Around this time of the year, as it so\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x11,
        (
            "#5PApparently if a traveler happens to be walking\x01",
            "along them at exactly that time, they undergo\x01",
            "what I can only describe as a strange experience...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x11,
        "#5P...and then they become happy. Nice, isn't it?\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(2000, 0, -1)

    def lambda_2CB6():
        OP_6B(2560, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2CB6)
    OP_0D()
    Sleep(2200)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2300   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2215 end

    def Function_12_2CD3(): pass

    label("Function_12_2CD3")

    Sleep(500)
    OP_8C(0x14E, 45, 400)
    Sleep(800)
    OP_8C(0x14E, 0, 400)
    Return()

    # Function_12_2CD3 end

    def Function_13_2CEC(): pass

    label("Function_13_2CEC")


    def lambda_2CF2():
        OP_8E(0xFE, 0xFFFF8D3C, 0x0, 0x9920, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2CF2)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 90, 400)
    Sleep(2000)
    OP_8C(0x14E, 45, 400)
    Sleep(2000)
    OP_8C(0x14E, 0, 400)

    def lambda_2D31():
        OP_8E(0xFE, 0xFFFF89B8, 0x0, 0xA6A4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2D31)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 0, 400)
    Sleep(2000)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)

    label("loc_2D69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D8D")
    OP_8C(0x14E, 45, 400)
    Sleep(2500)
    OP_8C(0x14E, 0, 400)
    Sleep(3500)
    Jump("loc_2D69")

    label("loc_2D8D")

    Return()

    # Function_13_2CEC end

    def Function_14_2D8E(): pass

    label("Function_14_2D8E")

    Sleep(500)
    OP_8C(0x14F, 0, 400)
    Sleep(400)
    OP_8C(0x14F, 45, 400)
    Sleep(400)

    def lambda_2DB1():
        OP_8E(0xFE, 0xFFFF8E04, 0x0, 0x9510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2DB1)
    WaitChrThread(0x14F, 0x1)
    OP_8C(0x14F, 90, 400)
    Sleep(2500)
    OP_8C(0x14F, 135, 400)
    Sleep(2000)
    OP_8C(0x14F, 0, 400)

    def lambda_2DF0():
        OP_8E(0xFE, 0xFFFF8E2C, 0x0, 0x9B00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2DF0)
    WaitChrThread(0x14F, 0x1)
    OP_8C(0x14F, 90, 400)
    Sleep(3000)
    Return()

    # Function_14_2D8E end

    def Function_15_2E17(): pass

    label("Function_15_2E17")


    def lambda_2E1D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2E1D)

    def lambda_2E2F():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E2F)
    WaitChrThread(0x12, 0x1)

    def lambda_2E4F():
        OP_8E(0xFE, 0xFFFF8E2C, 0x0, 0x92E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E4F)
    WaitChrThread(0x12, 0x1)
    Sleep(6000)
    Return()

    # Function_15_2E17 end

    def Function_16_2E6F(): pass

    label("Function_16_2E6F")

    Sleep(500)

    def lambda_2E7A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2E7A)

    def lambda_2E8C():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E8C)
    WaitChrThread(0x13, 0x1)

    def lambda_2EAC():
        OP_8E(0xFE, 0xFFFF8F58, 0x0, 0x8F20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2EAC)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 45, 400)
    Sleep(500)
    Return()

    # Function_16_2E6F end

    def Function_17_2ED3(): pass

    label("Function_17_2ED3")

    OP_8C(0x12, 220, 500)

    def lambda_2EE0():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2EE0)
    WaitChrThread(0x12, 0x1)

    def lambda_2F00():
        OP_8E(0xFE, 0xFFFF8A80, 0xFFFFFE0C, 0x86C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2F00)
    Sleep(100)

    def lambda_2F20():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2F20)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_17_2ED3 end

    def Function_18_2F32(): pass

    label("Function_18_2F32")

    Sleep(500)
    OP_8C(0x13, 220, 500)

    def lambda_2F44():
        OP_8E(0xFE, 0xFFFF8B0C, 0x0, 0x8D90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2F44)
    WaitChrThread(0x13, 0x1)

    def lambda_2F64():
        OP_8E(0xFE, 0xFFFF8A80, 0xFFFFFE0C, 0x86C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2F64)
    Sleep(100)

    def lambda_2F84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2F84)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_18_2F32 end

    SaveToFile()

Try(main)
