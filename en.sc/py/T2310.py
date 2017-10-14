from ED6SCScenarioHelper import *

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
        'Clem',                                 # 9
        'Polly',                                # 10
        'Mary',                                 # 11
        'Daniel',                               # 12
        'Lucia',                                # 13
        'Zack',                                 # 14
        'Amelia',                               # 15
        'Solomon',                              # 16
        'Elder Serge',                          # 17
        'Targeting Camera',                     # 18
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02500 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH01070 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01000 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02500P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH01070P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01000P._CP',             # 08
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4440,
        Z                   = 0,
        Y                   = 5030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -130,
        Z                   = 0,
        Y                   = 8460,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -32750,
        Z                   = 0,
        Y                   = 3570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -28110,
        Z                   = 0,
        Y                   = 7510,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        "Function_0_232",          # 00, 0
        "Function_1_2AD",          # 01, 1
        "Function_2_2BD",          # 02, 2
        "Function_3_43A",          # 03, 3
        "Function_4_1C4B",         # 04, 4
        "Function_5_24A9",         # 05, 5
        "Function_6_2803",         # 06, 6
        "Function_7_3057",         # 07, 7
        "Function_8_3FA0",         # 08, 8
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25E")
    OP_8C(0xE, 0, 0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x10, -30060, 0, 3800, 270)
    Jump("loc_299")

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_268")
    Jump("loc_299")

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_283")
    SetChrPos(0x10, -27680, 0, 40800, 270)
    Jump("loc_299")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_28D")
    Jump("loc_299")

    label("loc_28D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_299")
    SetChrFlags(0x10, 0x80)

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2AC")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_2AC")

    Return()

    # Function_0_232 end

    def Function_1_2AD(): pass

    label("Function_1_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2BC")
    OP_71(0x0, 0x4)
    OP_82(0x82, 0x0)

    label("loc_2BC")

    Return()

    # Function_1_2AD end

    def Function_2_2BD(): pass

    label("Function_2_2BD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_424")

    label("loc_2E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_424")

    label("loc_2FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_424")

    label("loc_314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_424")

    label("loc_32D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_424")

    label("loc_346")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_424")

    label("loc_35F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_424")

    label("loc_378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_424")

    label("loc_391")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_424")

    label("loc_3AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_424")

    label("loc_3C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_424")

    label("loc_3DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_424")

    label("loc_3F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_424")

    label("loc_40E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_424")

    label("loc_439")

    Return()

    # Function_2_2BD end

    def Function_3_43A(): pass

    label("Function_3_43A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_5A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F1")

    ChrTalk(    #0
        0xFE,
        (
            "Seems like I haven't seen Vogt,\x01",
            "the lighthouse keeper, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "He's getting on in his years, so maybe I\x01",
            "should check up on him from time to time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A5")

    label("loc_4F1")

    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        "Oh, yeah, I wonder how ol' Vogt is doing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Feel like I haven't seen him lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "He's getting on in his years, so maybe I\x01",
            "should check up on him from time to time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A5")

    Jump("loc_896")

    label("loc_5A8")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0xFE,
        "Hey, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Already check out the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1000FYep, we stopped by.\x02\x03",

            "I could hardly believe how good it \x01",
            "looked. That was a real surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Not bad, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm pretty proud at having had\x01",
            "the chance to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "The kids've got their smiles back,\x01",
            "so it feels like things are finally\x01",
            "settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "By the way...\x01",
            "Did some kinda case happen?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7A6")

    ChrTalk(    #12
        0x106,
        (
            "#050FYeah, for a bit.\x02\x03",

            "We've basically solved it, though,\x01",
            "so no worries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_801")

    label("loc_7A6")


    ChrTalk(    #13
        0x103,
        (
            "#020FYes, just a little thing.\x02\x03",

            "We've basically solved it, however,\x01",
            "so you can relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #14
        0xFE,
        (
            "Phew! That's good to hear.\x01",
            "Safe and peaceful really is best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #15
        0xFE,
        (
            "Anyway, bracers.\x01",
            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1006FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_896")

    Jump("loc_1C47")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_D89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_96E")

    ChrTalk(    #17
        0xFE,
        (
            "I absolutely wanna pick someone with\x01",
            "a good heart for our next mayor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I'm sure that's what everyone thought\x01",
            "last time they voted, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "*sigh* Politics sure are tough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A50")

    label("loc_96E")

    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        (
            "It's been quite a while since that\x01",
            "villainous mayor was caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "If possible, I wanna pick someone with\x01",
            "a good heart for our next mayor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I'm sure that's what everyone thought\x01",
            "last time they voted, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50")

    Jump("loc_D86")

    label("loc_A53")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0xFE,
        "Hey, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Already check out the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1000FYep, we stopped by.\x02\x03",

            "I could hardly believe how good it \x01",
            "looked. That was a real surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Not bad, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I'm pretty proud at having had\x01",
            "the chance to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "The kids've got their smiles back,\x01",
            "so it feels like things are finally\x01",
            "settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "By the way...\x01",
            "Did some kinda case happen?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C6A")

    ChrTalk(    #30
        0x106,
        (
            "#050FNo, there's just a thing we're\x01",
            "lookin' into. Just in case.\x02\x03",

            "It's not a case, so don't worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF9")

    label("loc_C6A")


    ChrTalk(    #31
        0x103,
        (
            "#020FThere's a situation we're investigating,\x01",
            "but it's got a low likelihood of being\x01",
            "anything serious.\x02\x03",

            "You don't need to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF9")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #32
        0xFE,
        (
            "Phew! That's good. Safe and\x01",
            "peaceful really is best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Anyway, bracers.\x01",
            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #34
        0x101,
        "#1006FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_D86")

    Jump("loc_1C47")

    label("loc_D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_121B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E53")

    ChrTalk(    #35
        0xFE,
        (
            "My uncle, Orvid, is a merchant\x01",
            "that trades in foodstuffs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "He's always flying from place to place\x01",
            "and barely ever comes home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "I don't think I could live like that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EE2")

    label("loc_E53")

    OP_A2(0x0)

    ChrTalk(    #38
        0xFE,
        (
            "Safe and peaceful is nice, but I\x01",
            "need to find a job soon myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I wanna work around my hometown,\x01",
            "but there's not many good jobs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE2")

    Jump("loc_1218")

    label("loc_EE5")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0xFE,
        "Hey, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Already check out the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1000FYep, we stopped by.\x02\x03",

            "I could hardly believe how good it \x01",
            "looked. That was a real surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Not bad, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I'm pretty proud at having had\x01",
            "the chance to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "The kids've got their smiles back,\x01",
            "so it feels like things are finally\x01",
            "settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "By the way...\x01",
            "Did some kinda case happen?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10FC")

    ChrTalk(    #47
        0x106,
        (
            "#050FNo, there's just a thing we're\x01",
            "lookin' into. Just in case.\x02\x03",

            "It's not a case, so don't worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118B")

    label("loc_10FC")


    ChrTalk(    #48
        0x103,
        (
            "#020FThere's a situation we're investigating,\x01",
            "but it's got a low likelihood of being\x01",
            "anything serious.\x02\x03",

            "You don't need to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118B")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #49
        0xFE,
        (
            "Phew! That's good. Safe and\x01",
            "peaceful really is best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #50
        0xFE,
        (
            "Anyway, bracers.\x01",
            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1006FYeah, later.\x02",
    )

    CloseMessageWindow()

    label("loc_1218")

    Jump("loc_1C47")

    label("loc_121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_1884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_12B8")

    ChrTalk(    #52
        0xFE,
        (
            "Sunday School's bein' held over at\x01",
            "the Windmill Lodge to the south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It should be over soon, so why\x01",
            "don't you go check up on them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1881")

    label("loc_12B8")

    OP_A2(0x122D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_15AB")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0xFE,
        "Hey, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Already check out the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        "#051FYep, we just stopped by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1000FI could hardly believe how good it \x01",
            "looked. That was a real surprise.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #58
        0xFE,
        "Not bad, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I'm pretty proud at having had\x01",
            "the chance to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "The kids've got their smiles back,\x01",
            "so it feels like things are finally\x01",
            "settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1015FOh, speaking of the kids, they're at\x01",
            "Sunday School right now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Yeah, they're holding it over at the\x01",
            "Windmill Lodge in the south of the\x01",
            "village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "It should be over soon,\x01",
            "so why don't you stop by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x106,
        (
            "#050FThe Windmill Lodge to the south...\x01",
            "Got it, we'll go check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1006FWell, see ya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "Yeah, keep up the good work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1881")

    label("loc_15AB")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0xFE,
        "Hey, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "Already check out the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1000FYep, we just stopped by.\x02\x03",

            "I could hardly believe how good it \x01",
            "looked. That was a real surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Not bad, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I'm pretty proud at having had\x01",
            "the chance to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "The kids've got their smiles back,\x01",
            "so it feels like things are finally\x01",
            "settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015FOh, speaking of the kids, they're at\x01",
            "Sunday School right now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Yeah, they're holding it over at the\x01",
            "Windmill Lodge in the south of the\x01",
            "village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "It should be over soon,\x01",
            "so why don't you stop by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#020FThe Windmill Lodge to the south, huh?\x01",
            "Let's go pay them a visit, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1006FWell, see ya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "Yeah, good luck.\x02",
    )

    CloseMessageWindow()

    label("loc_1881")

    Jump("loc_1C47")

    label("loc_1884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 5)), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(    #79
        0xFE,
        "We owe you bracers a lot, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "If you've got some time, come by.\x01",
            "You're always welcome here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C47")

    label("loc_1902")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122D)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0xFE,
        "Hey, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Already check out the orphanage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1000FAh, we were just on our way there.\x02\x03",

            "We've got some stuff to check out,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "No way...\x01",
            "Are you on some kinda case?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A68")

    ChrTalk(    #85
        0x106,
        (
            "#050FNo, there's just a thing we're\x01",
            "lookin' into. Just in case.\x02\x03",

            "It's not a case, so don't worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF7")

    label("loc_1A68")


    ChrTalk(    #86
        0x103,
        (
            "#020FThere's a situation we're investigating,\x01",
            "but it's got a low likelihood of being\x01",
            "anything serious.\x02\x03",

            "You don't need to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF7")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #87
        0xFE,
        "Phew! Got'cha. That's good to hear.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #88
        0xFE,
        (
            "If you're not in a hurry, relax\x01",
            "here in the village for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "You'll always be welcome here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1006FYeah, thanks.\x02\x03",

            "#1015FIf we get a chance, we'll stop by later.\x01",
            "We have to head to the orphanage first,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Ohh, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Well, see ya when I see ya, then!\x02",
    )

    CloseMessageWindow()

    label("loc_1C47")

    TalkEnd(0xFE)
    Return()

    # Function_3_43A end

    def Function_4_1C4B(): pass

    label("Function_4_1C4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D34")

    ChrTalk(    #93
        0xFE,
        (
            "It's been a long time since I had\x01",
            "to use fire to cook something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I'm learning some simple cooking\x01",
            "techniques from Old Miss Creda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "The older generation sure do know\x01",
            "something about everything.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1DC0")

    label("loc_1D34")


    ChrTalk(    #96
        0xFE,
        (
            "I'm learning some simple cooking\x01",
            "techniques from Old Miss Creda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "It's been a long time since I had\x01",
            "to use fire to cook something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC0")

    Jump("loc_24A5")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEC")

    ChrTalk(    #98
        0xFE,
        (
            "Army airships are falling out of the sky,\x01",
            "orbments have stopped working...\x01",
            "It's terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "My younger brother Zack went to check\x01",
            "on the lighthouse to make sure everything's\x01",
            "all right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "It's just old Vogt up there on his own,\x01",
            "so we're both a little worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1F96")

    label("loc_1EEC")


    ChrTalk(    #101
        0xFE,
        (
            "My younger brother Zack went to check\x01",
            "on the lighthouse to make sure everything's\x01",
            "all right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "It's really reassuring having him\x01",
            "around at times like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F96")

    Jump("loc_24A5")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_20E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_203E")

    ChrTalk(    #103
        0xFE,
        (
            "My little brother apparently wants to\x01",
            "have a job that helps out the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "If he could find such work, I'm sure\x01",
            "he'd put his back into it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_203E")

    OP_A2(0x1)

    ChrTalk(    #105
        0xFE,
        (
            "My little brother apparently wants to\x01",
            "have a job that helps out the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "He jumped at the chance to help rebuild\x01",
            "the orphanage, so I can believe it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E1")

    Jump("loc_24A5")

    label("loc_20E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_225D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_217E")

    ChrTalk(    #107
        0xFE,
        (
            "My younger brother seems interested\x01",
            "in the mayoral election, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "What I want to know isn't the future of Ruan,\x01",
            "it's Zack's.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225A")

    label("loc_217E")

    OP_A2(0x1)

    ChrTalk(    #109
        0xFE,
        (
            "My younger brother seems interested\x01",
            "in the mayoral election, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "What I want to know isn't the future of Ruan,\x01",
            "it's Zack's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I don't care who he votes for. I just\x01",
            "want him to hurry up and find a job!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225A")

    Jump("loc_24A5")

    label("loc_225D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22F1")

    ChrTalk(    #112
        0xFE,
        "I wonder why my uncle is so reckless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "I'm especially worried because my younger\x01",
            "brother Zack is just like him sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2400")

    label("loc_22F1")

    OP_A2(0x1)

    ChrTalk(    #114
        0xFE,
        (
            "My uncle Orvid is finally back from\x01",
            "one of his crazy business 'trips.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "No sooner was his foot in the door than he\x01",
            "said he was heading back out again to\x01",
            "look for more ingredients. *sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I managed to stop him somehow,\x01",
            "but why the heck is he so reckless?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2400")

    Jump("loc_24A5")

    label("loc_2403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_24A5")

    ChrTalk(    #117
        0xFE,
        (
            "It seems like the orphanage kids\x01",
            "are back in good spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "You can hear them laughing all the\x01",
            "way out here on their way back from\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A5")

    TalkEnd(0xFE)
    Return()

    # Function_4_1C4B end

    def Function_5_24A9(): pass

    label("Function_5_24A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_25BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_252B")

    ChrTalk(    #119
        0xFE,
        (
            "Promote the tourism industry,\x01",
            "or save the harbor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "As my father said, this isn't\x01",
            "an easy decision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_252B")

    OP_A2(0x2)

    ChrTalk(    #121
        0xFE,
        (
            "Promote the tourism industry,\x01",
            "or maintain the harbor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Realistic politics are so black in white.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "That's what my father says.\x02",
    )

    CloseMessageWindow()

    label("loc_25BB")

    Jump("loc_27FF")

    label("loc_25BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_265D")

    ChrTalk(    #124
        0xFE,
        (
            "We've got to prepare a voting place\x01",
            "in Manoria for the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "There's a lot we need to do to get\x01",
            "ready for the mayoral election.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2711")

    label("loc_265D")

    OP_A2(0x2)

    ChrTalk(    #126
        0xFE,
        (
            "My father's also busy preparing for\x01",
            "the election, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Manoria's also got some things\x01",
            "to prepare for the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "The village elder's got a lot to do, too.\x02",
    )

    CloseMessageWindow()

    label("loc_2711")

    Jump("loc_27FF")

    label("loc_2714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2793")

    ChrTalk(    #129
        0xFE,
        "Seems like Sunday School's over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "It was so cheery over there until just\x01",
            "a bit ago. Now it's totally quiet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27FF")

    label("loc_2793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_27FF")

    ChrTalk(    #131
        0xFE,
        (
            "Seems like the orphanage kids are\x01",
            "doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "All that rebuilding was definitely worth it.\x02",
    )

    CloseMessageWindow()

    label("loc_27FF")

    TalkEnd(0xFE)
    Return()

    # Function_5_24A9 end

    def Function_6_2803(): pass

    label("Function_6_2803")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_29F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295E")

    ChrTalk(    #133
        0xFE,
        (
            "Manoria's surrounded by nature, so\x01",
            "it's not hard to find firewood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "If worse comes to worst, we can catch wild birds\x01",
            "and fish, and even find wild vegetables to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Big cities like the capital don't really\x01",
            "have that option, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "If this situation drags on, the biggest\x01",
            "danger is to the urban centers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_29F0")

    label("loc_295E")


    ChrTalk(    #137
        0xFE,
        (
            "If this situation drags on, the biggest\x01",
            "danger is to the urban centers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "After all, the bigger the city,\x01",
            "the more it relies on orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F0")

    Jump("loc_3053")

    label("loc_29F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B11")

    ChrTalk(    #139
        0xFE,
        (
            "We have some stocks of food and\x01",
            "fuel at the Windmill Lodge, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "If we relax because of that,\x01",
            "we'll run out really fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I sent my son Solomon out to seek\x01",
            "support from the City of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Hopefully he'll be able to negotiate\x01",
            "with the new mayor.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2B94")

    label("loc_2B11")


    ChrTalk(    #143
        0xFE,
        (
            "The supplies we have at the Windmill\x01",
            "Lodge will run out very quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "This is why I sent my son to request\x01",
            "aid so early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B94")

    Jump("loc_3053")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C6A")

    ChrTalk(    #145
        0xFE,
        (
            "The nobleman who was the previous mayor\x01",
            "was arrested, and commoner candidates\x01",
            "are competing to take up after him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "This election almost seems like it\x01",
            "represents the changing of an age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1B")

    label("loc_2C6A")

    OP_A2(0x3)

    ChrTalk(    #147
        0xFE,
        (
            "Norman and Portos are both commoners,\x01",
            "but they are also both great people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "The old elections used to be reserved for\x01",
            "nobility, but it seems the times have changed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1B")

    Jump("loc_3053")

    label("loc_2D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2DB7")

    ChrTalk(    #149
        0xFE,
        "Last election, this was the voting site.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Many people believed in the name of\x01",
            "the Dalmore family as they put in\x01",
            "their votes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E64")

    label("loc_2DB7")

    OP_A2(0x3)

    ChrTalk(    #151
        0xFE,
        "Last election, this was the voting site...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "...No matter how you\x01",
            "look at it it's too small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I guess I have to ask The White Magnolia\x01",
            "inn for a bit of help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E64")

    Jump("loc_3053")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2EF0")

    ChrTalk(    #154
        0xFE,
        (
            "The youth of the village went to help\x01",
            "rebuild the orphanage, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "I hope their hearts stay as generous forever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F93")

    ChrTalk(    #156
        0xFE,
        (
            "The trouble the last mayor caused was\x01",
            "a serious blow to Manoria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "After terrible incidents like that, tourists\x01",
            "stay far away, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2F93")

    OP_A2(0x3)

    ChrTalk(    #158
        0xFE,
        "Oh, travelers. Welcome to Manoria.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "The orphanage has been rebuilt,\x01",
            "and people have returned to their\x01",
            "normal lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Now we just have to wait for\x01",
            "our next mayor to be elected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3053")

    TalkEnd(0xFE)
    Return()

    # Function_6_2803 end

    def Function_7_3057(): pass

    label("Function_7_3057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3068")
    Call(0, 8)

    label("loc_3068")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    AddParty(0x8, 0xF8, 0xFF)
    OP_31(0x8, 0x0, 0x27)
    OP_31(0x8, 0xFE, 0x0)
    OP_41(0x8, 0xE6, 0xFF)
    OP_41(0x8, 0xFF, 0xFF)
    OP_41(0x8, 0x120, 0xFF)
    OP_41(0x8, 0x273, 0x0)
    OP_41(0x8, 0x25B, 0x1)
    OP_41(0x8, 0x258, 0x2)
    OP_41(0x8, 0x265, 0x3)
    OP_41(0x8, 0x262, 0x4)
    OP_35(0x8, 0x8C)
    OP_35(0x8, 0x0)
    OP_BB(0x8, 0x6, 0x10E)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xF7, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x101, -30000, 0, 34900, 0)
    SetChrPos(0xF7, -30000, 0, 34900, 0)
    SetChrPos(0x109, -30000, 0, 42500, 180)
    SetChrPos(0x8, -30000, 0, 40000, 0)
    SetChrPos(0x9, -28640, 0, 40440, 315)
    SetChrPos(0xA, -30970, 0, 40340, 0)
    SetChrPos(0xB, -31570, 0, 41240, 45)
    SetChrPos(0xC, -27690, 0, 41900, 315)
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x109, 0x0)
    OP_6C(45000, 0)
    OP_6B(3010, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #161
        0x109,
        (
            "#1065F...They do not deserve your sympathy!\x02\x03",

            "#1067FIn truth, Pedro did not think Duke\x01",
            "Gaston would back down easily.\x02\x03",

            "#1063FAnd what of the machinations of that\x01",
            "foul masked puppeteer, Harlequin?\x02\x03",

            "Capri, Pedro's teacher, seemed to know\x01",
            "the jester, but simply dodged any questions\x01",
            "about him with frustrating vagueness.\x02\x03",

            "#1065FRegardless, Pedro knew another battle would\x01",
            "come...and soon. He would have to upgrade the\x01",
            "Blue Knight if he hoped to emerge victorious.\x02\x03",

            "#1060FOh, Pedro...\x02\x03",

            "A slightly irritated, yet comforting, voice\x01",
            "snapped Pedro from his reverie.\x02\x03",

            "#1061FDo you wish for your tea to grow cold?\x02\x03",

            "The clear blue eyes which met his own carried\x01",
            "their own message: 'It will be all right.'\x02\x03",

            "#1062FPedro, a little embarrassed, took his tea...\x01",
            "and drank deeply. It was enough to\x01",
            "simply have this moment...with her.\x02\x03",

            "#1071F...The End!\x01",
            "That's The Doll Knight, kids.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_352D():
        OP_95(0x8, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_352D)

    def lambda_354B():
        OP_95(0xA, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_354B)
    Sleep(50)

    def lambda_356E():
        OP_95(0xB, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_356E)

    def lambda_358C():
        OP_95(0xC, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_358C)
    Sleep(50)

    def lambda_35AF():
        OP_95(0x9, 0x0, 0x0, 0x0, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_35AF)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    ChrTalk(    #162
        0x8,
        (
            "#774FWhat? That's it?!\x02\x03",

            "But what about the fight with Harlequin?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #163
        0xA,
        (
            "#1719F#5POh, Clem, you're such a dummy.\x01",
            "That's a wonderful ending.\x02\x03",

            "#1718FAnd you just know Pedro and Tia\x01",
            "go on to get married and live\x01",
            "happily ever after...\x02\x03",

            "#1903FAhhhh, so romantic... ㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #164
        0xC,
        "Yeah, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xC,
        "They gotta get married and be happy! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xB,
        "#1720FI want some of that tea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        "#1730F#4PCapri is so cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x109,
        (
            "#1068F*pheeeeeew*\x02\x03",

            "All twenty-two chapters of The Doll Knight in\x01",
            "one sitting for a bunch of rambunctious kids.\x01",
            "You want to talk challenges...\x02\x03",

            "#1062FAll right, kiddos, that's enough\x01",
            "for one day! Class is over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x8,
        "#772FAww!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x109, 400)

    ChrTalk(    #170
        0xA,
        "#1710F#5PThank you for teaching us, Mr. Graham!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x109,
        (
            "#1066FOookay, never underestimating this\x01",
            "group of kids again...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x109,
        (
            "#1062FYo, who's at the door?\x02\x03",

            "Class just wrapped up, so come on in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#5PHaha... You noticed me?\x02\x03",

            "Guess I stuck my nose in a little\x01",
            "too far. Sorry for intruding!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_3A09():
        OP_6D(-29990, 0, 40480, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A09)

    def lambda_3A21():
        OP_67(0, 6620, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A21)

    def lambda_3A39():
        TurnDirection(0x8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A39)

    def lambda_3A47():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A47)

    def lambda_3A55():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A55)

    def lambda_3A63():
        TurnDirection(0xB, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A63)

    def lambda_3A71():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3A71)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    def lambda_3A9A():
        OP_8F(0x101, 0xFFFF8ABC, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A9A)

    def lambda_3AB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3AB5)
    Sleep(500)
    ClearChrFlags(0xF7, 0x8)

    def lambda_3AD1():
        OP_8F(0xF7, 0xFFFF8742, 0x0, 0x8F70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3AD1)

    def lambda_3AEC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_3AEC)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #174
        0x109,
        "#1064F#6PHuh? Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        "#774F#6P#3SWHAAAAAAAAAAA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        "#1714F#6P#3SEstelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1018F#2PHi, kids! It's great to see you again!\x02\x03",

            "Are you guys doing okay?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C4E():
        OP_92(0x8, 0x101, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3C4E)
    Sleep(50)

    def lambda_3C68():
        OP_8E(0x9, 0xFFFF8D3C, 0x0, 0x94A2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C68)
    Sleep(50)

    def lambda_3C88():
        OP_8E(0xA, 0xFFFF86FC, 0x0, 0x947A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C88)
    Sleep(50)

    def lambda_3CA8():
        OP_8E(0xB, 0xFFFF8710, 0x0, 0x97EA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3CA8)
    Sleep(50)

    def lambda_3CC8():
        OP_8E(0xC, 0xFFFF8DF0, 0x0, 0x990C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3CC8)
    Sleep(50)

    def lambda_3CE8():
        OP_8E(0x109, 0xFFFF8A44, 0x0, 0xA136, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CE8)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #178
        0x8,
        "#771F#1PHoly moly! Did you come to play?!\x02",
    )

    WaitChrThread(0xC, 0x1)
    TurnDirection(0xC, 0x101, 0)
    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        "#1718F#5PThis is great! It's been for-e-verrrrr!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xB,
        "#1721F#5PMiss Esteeeelle! Play with me! Me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        "#1732F#2PWelcome back! Welcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1016F#2PHaha! Well, you haven't lost\x01",
            "any energy, it seems!\x02\x03",

            "#1017FAnd...Father Kevin!\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x109,
        "#1061F#6PAh, she remembers me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#1006F#2POf course I do!\x02\x03",

            "#1016FWow, though. You really are a priest...\x01",
            "despite that getup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x109,
        (
            "#1068F#6PReally, why all the hate on my\x01",
            "awesome duds?\x02\x03",

            "#1062FBut, hey. What are the chances\x01",
            "we'd meet again, here, of all places?\x02\x03",

            "#1061FCould this be...fate? ㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_3057 end

    def Function_8_3FA0(): pass

    label("Function_8_3FA0")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4019"),
        (1, "loc_401F"),
        (SWITCH_DEFAULT, "loc_4025"),
    )


    label("loc_4019")

    OP_A2(0x1200)
    Jump("loc_4025")

    label("loc_401F")

    OP_A2(0x1201)
    Jump("loc_4025")

    label("loc_4025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4033")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4037")

    label("loc_4033")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4037")

    Return()

    # Function_8_3FA0 end

    SaveToFile()

Try(main)
