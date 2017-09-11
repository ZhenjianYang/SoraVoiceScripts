from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2512   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Jill',                                 # 9
        'Ms. Wiola',                            # 10
        'Mr. Effort',                           # 11
        'Alice',                                # 12
        'Purity',                               # 13
        'Argyle',                               # 14
        'Dennis',                               # 15
        'Felicity',                             # 16
        'Reina',                                # 17
        'CH22000',                              # 18
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH01210 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01590 ._CH',             # 03
        'ED6_DT07/CH01090 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01370 ._CH',             # 07
        'ED6_DT06/CH20100 ._CH',             # 08
        'ED6_DT06/CH20109 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH01210P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01590P._CP',             # 03
        'ED6_DT07/CH01090P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01370P._CP',             # 07
        'ED6_DT06/CH20100P._CP',             # 08
        'ED6_DT06/CH20109P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
        Direction           = 90,
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
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
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
        X                   = 84400,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -60350,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -60450,
        Z                   = 0,
        Y                   = 30850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28710,
        Z                   = 0,
        Y                   = 25280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -31400,
        Z                   = 0,
        Y                   = -800,
        Direction           = 90,
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
        X                   = -63000,
        Z                   = 0,
        Y                   = -3700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -61500,
        Z                   = 0,
        Y                   = -3700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -28640,
        Z                   = 700,
        Y                   = 31090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835018,
        ChipIndex           = 0xA,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -28640,
        TriggerZ            = 700,
        TriggerY            = 31090,
        TriggerRange        = 1000,
        ActorX              = -28640,
        ActorZ              = 1000,
        ActorY              = 31090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_3D6",          # 01, 1
        "Function_2_423",          # 02, 2
        "Function_3_5A0",          # 03, 3
        "Function_4_691",          # 04, 4
        "Function_5_94F",          # 05, 5
        "Function_6_996",          # 06, 6
        "Function_7_AB2",          # 07, 7
        "Function_8_E5A",          # 08, 8
        "Function_9_FE0",          # 09, 9
        "Function_10_14B9",        # 0A, 10
        "Function_11_1982",        # 0B, 11
        "Function_12_2972",        # 0C, 12
        "Function_13_2C74",        # 0D, 13
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2AB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58560, 0, -1150, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -60740, 0, 750, 180)
    Jump("loc_380")

    label("loc_2AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2B5")
    Jump("loc_380")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2BF")
    Jump("loc_380")

    label("loc_2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2C9")
    Jump("loc_380")

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_322")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -119550, 0, 30420, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 29320, 0, 27850, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_380")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 29790, 0, 30750, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_380")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_35B")
    Jump("loc_380")

    label("loc_35B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_365")
    Jump("loc_380")

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_374")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_380")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_380")
    ClearChrFlags(0xC, 0x80)

    label("loc_380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_390")
    SetChrFlags(0x11, 0x80)

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 11)
    OP_B1("T2512_k")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 12)
    OP_B1("t2512_n")

    label("loc_3D5")

    Return()

    # Function_0_266 end

    def Function_1_3D6(): pass

    label("Function_1_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F7")
    OP_B1("t2512_y")
    Jump("loc_400")

    label("loc_3F7")

    OP_B1("t2512_n")

    label("loc_400")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_413")
    OP_65(0x0, 0x1)

    label("loc_413")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_422")
    OP_64(0x0, 0x1)

    label("loc_422")

    Return()

    # Function_1_3D6 end

    def Function_2_423(): pass

    label("Function_2_423")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_58A")

    label("loc_448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_58A")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_58A")

    label("loc_47A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_58A")

    label("loc_493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_58A")

    label("loc_4AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_58A")

    label("loc_4C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_58A")

    label("loc_4DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_58A")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_58A")

    label("loc_510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_58A")

    label("loc_529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_58A")

    label("loc_542")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_58A")

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_58A")

    label("loc_574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_58A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58A")

    label("loc_59F")

    Return()

    # Function_2_423 end

    def Function_3_5A0(): pass

    label("Function_3_5A0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        "Oh, is everyone still practicing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "You should get to bed and rest\x01",
            "up for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68D")

    label("loc_60D")


    ChrTalk(    #2
        0xFE,
        (
            "I wonder if everyone's still\x01",
            "on campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Everyone's cleared out of the\x01",
            "dorms, so I imagine they're\x01",
            "all over the place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D")

    TalkEnd(0x9)
    Return()

    # Function_3_5A0 end

    def Function_4_691(): pass

    label("Function_4_691")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_8DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_793")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_712")
    OP_A2(0x1)

    ChrTalk(    #4
        0xFE,
        "Thank you for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'm glad everything was settled\x01",
            "before it got too serious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790")

    label("loc_712")


    ChrTalk(    #6
        0xFE,
        (
            "Still, Mickey can be a royal\x01",
            "pain sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Heh. Maybe I ought to make him\x01",
            "work it off in his next phys. ed\x01",
            "class.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790")

    Jump("loc_8D9")

    label("loc_793")


    ChrTalk(    #8
        0xFE,
        (
            "Some of the kids came by earlier looking\x01",
            "for the key to unlock the old building. They\x01",
            "wanted materials for set dressing, they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "They went in some time ago,\x01",
            "but I haven't heard from them\x01",
            "since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "There's a lot of students who haven't\x01",
            "come back to their dorm rooms yet. I\x01",
            "might go make my rounds before curfew.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D9")

    Jump("loc_94B")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_94B")

    ChrTalk(    #11
        0xFE,
        (
            "Both dorms have a teacher who\x01",
            "patrols at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Ahem! ...Obviously, I patrol the boys' \x01",
            "dorm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94B")

    TalkEnd(0xA)
    Return()

    # Function_4_691 end

    def Function_5_94F(): pass

    label("Function_5_94F")

    TalkBegin(0xB)

    ChrTalk(    #13
        0xFE,
        "Whew...one more day finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "So, what to do next...?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_5_94F end

    def Function_6_996(): pass

    label("Function_6_996")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F2")
    OP_A2(0x3)

    ChrTalk(    #15
        0xFE,
        "Oh! Kloe and Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Good luck with the play tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2E")

    label("loc_9F2")


    ChrTalk(    #17
        0xFE,
        (
            "I'm working on the sets,\x01",
            "since I'm a big history buff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2E")

    Jump("loc_AAE")

    label("loc_A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_AAE")

    ChrTalk(    #18
        0xFE,
        (
            "I think I'm going to read that\x01",
            "book I bought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I'd like to write a book someday,\x01",
            "so I'm studying humanities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAE")

    TalkEnd(0xC)
    Return()

    # Function_6_996 end

    def Function_7_AB2(): pass

    label("Function_7_AB2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_BFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC4")
    OP_A2(0x4)

    ChrTalk(    #20
        0xFE,
        (
            "Heh heh heh...I wish evening would\x01",
            "come sooner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I find the dark very soothing,\x01",
            "so I really enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I especially like taking baths\x01",
            "in absolute, pitch black...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "You should try it, if you get the\x01",
            "chance. It's incredibly relaxing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFB")

    label("loc_BC4")


    ChrTalk(    #24
        0xFE,
        (
            "Heh heh heh...I wish evening\x01",
            "would come sooner...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFB")

    Jump("loc_E56")

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4E")
    OP_A2(0x4)

    ChrTalk(    #25
        0xFE,
        "Heh heh heh...night is upon us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Just north of here is an old\x01",
            "building that used to be part\x01",
            "of the school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Way back when, it was refitted\x01",
            "to serve as a military stronghold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "...I'll bet you couldn't make it\x01",
            "out of there...alive.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        "#506F...Oooooh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD4")

    label("loc_D4E")


    ChrTalk(    #31
        0xFE,
        (
            "The old school building was refitted\x01",
            "to serve as a military stronghold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I'll bet you couldn't make it\x01",
            "out of there...alive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD4")

    Jump("loc_E56")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_E56")

    ChrTalk(    #33
        0xFE,
        "It's almost time for the festival...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "The club's doing a food stand,\x01",
            "so I'd better get cracking on\x01",
            "the setup. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_E56")

    TalkEnd(0xD)
    Return()

    # Function_7_AB2 end

    def Function_8_E5A(): pass

    label("Function_8_E5A")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_EFF")

    ChrTalk(    #35
        0xFE,
        (
            "In my experience, reviewing\x01",
            "the class lesson really\x01",
            "makes a difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I review for three hours and\x01",
            "do prep work for another two,\x01",
            "every day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDC")

    label("loc_EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_F4F")

    ChrTalk(    #37
        0xFE,
        (
            "Ahhhh...it's almost time\x01",
            "for bed. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "Oh, wait...the play...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FDC")

    label("loc_F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_FDC")

    ChrTalk(    #39
        0xFE,
        (
            "Although I'd like to focus on\x01",
            "studying, I have to learn my\x01",
            "part for the play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "*sigh* How did I get roped into\x01",
            "this, anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDC")

    TalkEnd(0xE)
    Return()

    # Function_8_E5A end

    def Function_9_FE0(): pass

    label("Function_9_FE0")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A4")
    OP_A2(0x6)

    ChrTalk(    #41
        0xFE,
        (
            "We're working on art class\x01",
            "assignments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "We just came back here to get\x01",
            "some supplies, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "...Not that we forgot them. We...\x01",
            "uh...just needed more. Yeah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1123")

    label("loc_10A4")


    ChrTalk(    #44
        0xFE,
        (
            "We just came back here to get\x01",
            "some supplies, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "...Not that we forgot them. We...\x01",
            "uh...just needed more. Yeah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1123")

    Jump("loc_14B5")

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_14B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1463")
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0x10, 255)

    ChrTalk(    #46
        0xF,
        (
            "*sigh* It's just been a full\x01",
            "week of upheaval.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "Rehearsals for the play, setting up the\x01",
            "Art Club's food stall, plus helping out\x01",
            "with the class exhibition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "You did a pretty good...check that,\x01",
            "you did a GREAT job.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #49
        0xF,
        (
            "...And where were you during\x01",
            "all that work, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "I'd been considering backing\x01",
            "out of the play, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "Well, I wasn't expecting you\x01",
            "to volunteer for the role of the\x01",
            "Archbishop.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0xF,
        (
            "Of course I did! Did you think I'd\x01",
            "really play as a commoner?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        (
            "If I'm going to do something, I'm\x01",
            "going to do it right. Unfortunately,\x01",
            "I had to give up the lead role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        "My, my. I'm impressed.\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0xF,
        (
            "Somehow I get the feeling that\x01",
            "I'm being led down this thorny\x01",
            "path, Reina...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0x10, 255)
    Jump("loc_14B5")

    label("loc_1463")


    ChrTalk(    #56
        0xFE,
        (
            "Somehow I get the feeling that\x01",
            "I'm being led down this thorny\x01",
            "path, Reina...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B5")

    TalkEnd(0xF)
    Return()

    # Function_9_FE0 end

    def Function_10_14B9(): pass

    label("Function_10_14B9")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_15D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")
    OP_A2(0x7)
    OP_4A(0xF, 255)

    ChrTalk(    #57
        0x10,
        (
            "Well, hey...everyone forgets a\x01",
            "few things, from time to time.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_1537():
        TurnDirection(0xF, 0x10, 1500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1537)

    ChrTalk(    #58
        0xF,
        "...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(    #59
        0x10,
        (
            "Ha ha...if you don't hurry,\x01",
            "activities time will be over.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xF, 255)
    OP_8C(0xF, 90, 6000)
    Jump("loc_15D4")

    label("loc_159D")


    ChrTalk(    #60
        0xFE,
        (
            "Everyone forgets a few things,\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D4")

    Jump("loc_197E")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_197E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1914")
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0xF, 255)

    ChrTalk(    #61
        0xF,
        (
            "*sigh* It's just been a full week\x01",
            "of upheaval.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "Rehearsals for the play, setting up the\x01",
            "Art Club's food stand, plus helping out\x01",
            "with the class exhibition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "You did a pretty good...check that,\x01",
            "you did a GREAT job.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0xF,
        (
            "...And where were you during\x01",
            "all that work, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xF,
        (
            "I'd been considering backing\x01",
            "out of the play, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "Well, I wasn't expecting you\x01",
            "to volunteer for the role of the\x01",
            "Archbishop.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0xF,
        (
            "Of course I did! Did you think I'd\x01",
            "really play as a commoner?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xF,
        (
            "If I'm going to do something, I'm\x01",
            "going to do it right. Unfortunately,\x01",
            "I had to give up the lead role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "My, my. I'm impressed.\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0xF,
        (
            "Somehow I get the feeling that\x01",
            "I'm being led down this thorny\x01",
            "path, Reina...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_197E")

    label("loc_1914")


    ChrTalk(    #71
        0xFE,
        (
            "I like to watch your development...\x01",
            "you know, make sure that you're\x01",
            "turning out to be a good person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197E")

    TalkEnd(0x10)
    Return()

    # Function_10_14B9 end

    def Function_11_1982(): pass

    label("Function_11_1982")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(-120390, 0, -2060, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -121640, 0, -4360, 0)
    SetChrPos(0x105, -122120, 0, -3050, 180)
    SetChrPos(0x8, -121110, 0, -2820, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #72
        0x105,
        (
            "#040F#1POkay, Estelle.\x01",
            "Please use this bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#001FThank you... ♪\x02\x03",

            "#501FBut that means you and Jill\x01",
            "are in the same room.\x02\x03",

            "You two must be close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x105,
        (
            "#041F#1PHa ha... We have been, ever since\x01",
            "we first started here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#641F#3PAnd as roommates, we're pretty\x01",
            "much inseparable!\x02\x03",

            "#644FBy the way, I have a\x01",
            "proposition for you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#004FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#648F#3PWant to be an honorary best\x01",
            "friend of mine?\x02\x03",

            "After all, we're going to be\x01",
            "working together!\x02\x03",

            "You don't mind, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#001FHa ha ha. Of course not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x105,
        (
            "#040F#1PNot superseding me, I hope!\x02\x03",

            "We're a best friend trio, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#006FYeah, of course we are!\x02\x03",

            "#001FMy new best friends, Jill and Kloe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x105,
        "#048F#1PWonderful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#641F#3PLooks like it's just us girls\x01",
            "in here. This will be fun.\x02\x03",

            "No need to worry about boys'\x01",
            "prying eyes while we're here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #83
        0x105,
        "#045FYou make it sound so dirty!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #84
        0x8,
        (
            "#645F#4P*sigh* You're so innocent.\x02\x03",

            "Like a little lamb... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x105,
        (
            "#042FOh, that's just mean.\x02\x03",

            "Just for that, I'm not baking\x01",
            "you any sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#643F#4POh, well, pardon me.\x02\x03",

            "I apologize for offending you,\x01",
            "Ma'amselle Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x105,
        "#041FNope. Try again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#501F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #89
        0x105,
        "#044F#1PHmm...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #90
        0x8,
        (
            "#640F#3PWhat's wrong, Estelle?\x01",
            "What's with all the staring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#008FHa ha ha... It's no big deal.\x01",
            "I've just got a little green\x01",
            "monster on my shoulder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        "#643F#3PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#000FI have some friends back\x01",
            "in Rolent...\x02\x03",

            "But the most we ever did was\x01",
            "have sleepovers.\x02\x03",

            "#001FI think it must be nice to have\x01",
            "someone close, living under the\x01",
            "same roof with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)
    OP_63(0x105)

    ChrTalk(    #94
        0x8,
        "#642F#3P...What do you think, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x105,
        (
            "#045F#1PI'm not sure...\x02\x03",

            "I don't really understand what\x01",
            "would make you jealous, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#501FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#646F#3PI concur.\x02\x03",

            "I almost want to ask where\x01",
            "you get off saying something\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#004FWhy would you say that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#645F#3POh, come on...\x02\x03",

            "You've got a traveling companion,\x01",
            "don't you? (A pretty nice looking\x01",
            "one, to boot...)\x02\x03",

            "Who you've also, I don't know...\x01",
            "lived under the same roof with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#004FUh...\x02\x03",

            "Are you talking about Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x105,
        "#045F#1PThat's kind of a silly question...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#644F#3PYou've got a hot guy with you all\x01",
            "the time, and you're jealous of us\x01",
            "living in an all-girl household?\x02\x03",

            "I'm playing a tiny violin for you.\x01",
            "Like, minuscule in size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#007FShows what YOU know...\x02\x03",

            "#006FJoshua's more like a big brother\x01",
            "to me.\x02\x03",

            "Us living together is more like\x01",
            "a family thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#649F#3POh-ho...a 'family thing,'\x01",
            "she says.\x02\x03",

            "I wonder if Joshua feels the\x01",
            "same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#501FBuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#659F#3PI bet that's not what a guy his\x01",
            "age would think.\x02\x03",

            "It's gotta be tough for him to\x01",
            "always be around a pretty girl\x01",
            "like you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #108
        0x105,
        "#043FEnough, Jill!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #109
        0x105,
        (
            "#045F#1PI'm so sorry, Estelle.\x02\x03",

            "Jill has a bad habit of picking\x01",
            "on people.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #110
        0x8,
        (
            "#646F#4PPfffffft. If we're gonna start\x01",
            "talking about bad habits...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #111
        0x105,
        (
            "#042FIs there something you'd like\x01",
            "to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "#641F#4PNope. I'm good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#008FUmm... Ha ha ha...\x02\x03",

            "Come on, don't mess with me\x01",
            "like that.\x02\x03",

            "#503FAnd really...Joshua?\x01",
            "I mean...c'mon...no way!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #114
        0x8,
        "#649F#3PSomeone's in denial... ♪♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x105,
        "#047FJill!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #116
        0x8,
        (
            "#643F#3POops! I just remembered, I have\x01",
            "to give my daily report to the\x01",
            "teacher before bed.\x02\x03",

            "#648FSo, goodnight, ladies.\x01",
            "Sleep well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2716():
        OP_6D(-121140, 0, -5760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2716)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrFlags(0x8, 0x4)

    def lambda_2745():

        label("loc_2745")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2745")

    QueueWorkItem2(0x101, 2, lambda_2745)

    def lambda_2756():

        label("loc_2756")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2756")

    QueueWorkItem2(0x105, 2, lambda_2756)
    OP_8E(0x8, 0xFFFE27BC, 0x0, 0xFFFFF18C, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFE2906, 0x0, 0xFFFFDECC, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_2794():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2794)
    OP_8E(0x8, 0xFFFE28FC, 0x0, 0xFFFFD9A4, 0xBB8, 0x0)
    Sleep(200)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(    #117
        0x105,
        "#043FI swear...\x02",
    )

    CloseMessageWindow()
    OP_6D(-120390, 0, -2060, 1500)

    ChrTalk(    #118
        0x105,
        (
            "#045F#1POh, right... Estelle?\x02\x03",

            "If you'd like, I can lend you\x01",
            "some of my pajamas.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #119
        0x101,
        "#503F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x105,
        "#044F#1PEstelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#004F#5PHuhwhat?!\x02",
    )

    OP_9E(0x101, 0x32, 0x0, 0x12C, 0x1770)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 350, 400)

    ChrTalk(    #122
        0x101,
        (
            "#008FOh, right... Pajamas.\x02\x03",

            "Sure, that sounds great.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    AnonymousTalk(    #123
        "\x07\x05With that, Estelle and Joshua's unlikely life at the royal academy had begun.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapFlags(0x10000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2512   ._SN", 115, 0, 1)
    IdleLoop()
    Return()

    # Function_11_1982 end

    def Function_12_2972(): pass

    label("Function_12_2972")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_72(0x8, 0x20)
    OP_6F(0x8, 15)
    OP_72(0xA, 0x20)
    OP_6F(0xA, 15)
    OP_6D(-118900, 0, -2700, 0)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x101, 0x258, 1200, 0x1C, 0x21, 0xFA, 0x0)
    OP_62(0x8, 0x12C, 1750, 0x1C, 0x21, 0xFA, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x105, -118840, 0, -3930, 180)
    SetChrPos(0x101, -118500, 500, -5400, 0)
    SetChrPos(0x8, -118550, 100, 300, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x8, 8)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101)
    SetChrSubChip(0x101, 15)
    Sleep(50)
    SetChrSubChip(0x101, 16)
    Sleep(1000)

    def lambda_2A68():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A68)
    Sleep(50)
    OP_6F(0xA, 15)
    OP_70(0xA, 0x14)
    Sleep(1000)
    OP_62(0x101, 0x64, 1500, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x105, 270, 400)

    def lambda_2AA9():
        OP_6D(-118800, 0, -930, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2AA9)
    OP_8E(0x105, 0xFFFE297E, 0x0, 0xFFFFF060, 0xBB8, 0x0)
    OP_8E(0x105, 0xFFFE29A6, 0x0, 0xFFFFFBF0, 0xBB8, 0x0)
    OP_8E(0x105, 0xFFFE2FBE, 0x0, 0xFFFFFC0E, 0xBB8, 0x0)
    OP_8C(0x105, 0, 400)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101)
    Sleep(1000)

    def lambda_2B23():
        OP_99(0xFE, 0x7, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B23)
    Sleep(100)
    OP_6F(0xA, 20)
    OP_70(0xA, 0xF)
    WaitChrThread(0x101, 0x1)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_62(0x101, 0x258, 1200, 0x1C, 0x21, 0xFA, 0x0)
    TurnDirection(0x105, 0x101, 400)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1200)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x105, 270, 400)
    FadeToDark(2000, 0, -1)

    def lambda_2BB5():
        OP_6D(-118900, 0, -2700, 1500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2BB5)
    OP_8E(0x105, 0xFFFE29A6, 0x0, 0xFFFFFBF0, 0xDAC, 0x0)
    OP_8E(0x105, 0xFFFE297E, 0x0, 0xFFFFF060, 0xDAC, 0x0)
    OP_8E(0x105, 0xFFFE2FC8, 0x0, 0xFFFFF0A6, 0xDAC, 0x0)
    OP_8C(0x105, 180, 400)
    OP_0D()

    AnonymousTalk(    #124
        (
            "\x07\x05In the morning, they would wake up and go to school, just like the other\x01",
            "students...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2510   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2972 end

    def Function_13_2C74(): pass

    label("Function_13_2C74")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x11, 0x80)
    OP_64(0x0, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #125
        "\x07\x00Found \x07\x02Ruan Economics III\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33F, 1)
    OP_28(0x27, 0x1, 0x100)
    TalkEnd(0xFF)
    Return()

    # Function_13_2C74 end

    SaveToFile()

Try(main)
