from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3602   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3602.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12660 ._CH',             # 00
        'ED6_DT29/CH12661 ._CH',             # 01
        'ED6_DT29/CH12670 ._CH',             # 02
        'ED6_DT29/CH12671 ._CH',             # 03
        'ED6_DT29/CH12680 ._CH',             # 04
        'ED6_DT29/CH12681 ._CH',             # 05
        'ED6_DT29/CH12690 ._CH',             # 06
        'ED6_DT29/CH12691 ._CH',             # 07
        'ED6_DT29/CH12700 ._CH',             # 08
        'ED6_DT29/CH12701 ._CH',             # 09
        'ED6_DT29/CH12710 ._CH',             # 0A
        'ED6_DT29/CH12711 ._CH',             # 0B
        'ED6_DT29/CH12720 ._CH',             # 0C
        'ED6_DT29/CH12721 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12660P._CP',             # 00
        'ED6_DT29/CH12661P._CP',             # 01
        'ED6_DT29/CH12670P._CP',             # 02
        'ED6_DT29/CH12671P._CP',             # 03
        'ED6_DT29/CH12680P._CP',             # 04
        'ED6_DT29/CH12681P._CP',             # 05
        'ED6_DT29/CH12690P._CP',             # 06
        'ED6_DT29/CH12691P._CP',             # 07
        'ED6_DT29/CH12700P._CP',             # 08
        'ED6_DT29/CH12701P._CP',             # 09
        'ED6_DT29/CH12710P._CP',             # 0A
        'ED6_DT29/CH12711P._CP',             # 0B
        'ED6_DT29/CH12720P._CP',             # 0C
        'ED6_DT29/CH12721P._CP',             # 0D
    )

    DeclMonster(
        X                   = 16890,
        Z                   = -3600,
        Y                   = -90,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7864,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30,
        Z                   = -3600,
        Y                   = 17250,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7865,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20800,
        Z                   = -3600,
        Y                   = 20800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7866,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13110,
        Z                   = -3600,
        Y                   = -13270,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7867,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60,
        Z                   = -450,
        Y                   = 61800,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x415,
        Unknown_18          = 7868,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24710,
        Z                   = -7600,
        Y                   = -24730,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7869,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24890,
        Z                   = -7600,
        Y                   = 24770,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7870,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24900,
        Z                   = -7600,
        Y                   = 24950,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7871,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24090,
        Z                   = -3600,
        Y                   = -300,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7872,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 300,
        Z                   = -3600,
        Y                   = -23660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7873,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 72970,
        TriggerRange        = 1000,
        ActorX              = -40,
        ActorZ              = 0,
        ActorY              = 73590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6880,
        TriggerZ            = 0,
        TriggerY            = 66010,
        TriggerRange        = 1000,
        ActorX              = -7540,
        ActorZ              = 0,
        ActorY              = 66010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6880,
        TriggerZ            = 0,
        TriggerY            = 66010,
        TriggerRange        = 1000,
        ActorX              = 7580,
        ActorZ              = 0,
        ActorY              = 66010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22970,
        TriggerZ            = -3600,
        TriggerY            = 7630,
        TriggerRange        = 1000,
        ActorX              = -22840,
        ActorZ              = -3600,
        ActorY              = 8250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -16670,
        TriggerZ            = -3600,
        TriggerY            = -50,
        TriggerRange        = 1000,
        ActorX              = -15970,
        ActorZ              = -3600,
        ActorY              = 20,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -3600,
        TriggerY            = -16640,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = -3600,
        ActorY              = -15930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7680,
        TriggerZ            = -3600,
        TriggerY            = -22920,
        TriggerRange        = 1000,
        ActorX              = 8300,
        ActorZ              = -3600,
        ActorY              = -22720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45890,
        TriggerZ            = -8000,
        TriggerY            = -47410,
        TriggerRange        = 1000,
        ActorX              = 45890,
        ActorZ              = -8000,
        ActorY              = -47410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45890,
        TriggerZ            = -8000,
        TriggerY            = 46040,
        TriggerRange        = 1000,
        ActorX              = 45890,
        ActorZ              = -8000,
        ActorY              = 46040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47420,
        TriggerZ            = -8000,
        TriggerY            = -47410,
        TriggerRange        = 1000,
        ActorX              = -47420,
        ActorZ              = -8000,
        ActorY              = -47410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47200,
        TriggerZ            = -7850,
        TriggerY            = 46160,
        TriggerRange        = 1000,
        ActorX              = -47200,
        ActorZ              = -7850,
        ActorY              = 46160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3BE",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_533",          # 02, 2
        "Function_3_64A",          # 03, 3
        "Function_4_761",          # 04, 4
        "Function_5_878",          # 05, 5
        "Function_6_98F",          # 06, 6
        "Function_7_A8B",          # 07, 7
        "Function_8_BA2",          # 08, 8
        "Function_9_CB9",          # 09, 9
        "Function_10_11AA",        # 0A, 10
        "Function_11_16BC",        # 0B, 11
        "Function_12_1BF0",        # 0C, 12
        "Function_13_206E",        # 0D, 13
        "Function_14_2559",        # 0E, 14
        "Function_15_2654",        # 0F, 15
        "Function_16_26CC",        # 10, 16
        "Function_17_27C7",        # 11, 17
        "Function_18_283F",        # 12, 18
        "Function_19_294C",        # 13, 19
        "Function_20_29CD",        # 14, 20
        "Function_21_2ADA",        # 15, 21
        "Function_22_2B5B",        # 16, 22
        "Function_23_2C4E",        # 17, 23
        "Function_24_2D41",        # 18, 24
        "Function_25_2D8F",        # 19, 25
    )


    def Function_0_3BE(): pass

    label("Function_0_3BE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3D6"),
        (101, "loc_3DD"),
        (102, "loc_3E4"),
        (103, "loc_3EB"),
        (SWITCH_DEFAULT, "loc_3F2"),
    )


    label("loc_3D6")

    Event(0, 14)
    Jump("loc_3F2")

    label("loc_3DD")

    Event(0, 16)
    Jump("loc_3F2")

    label("loc_3E4")

    Event(0, 18)
    Jump("loc_3F2")

    label("loc_3EB")

    Event(0, 20)
    Jump("loc_3F2")

    label("loc_3F2")

    Return()

    # Function_0_3BE end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405")
    OP_6F(0x24, 0)
    Jump("loc_40C")

    label("loc_405")

    OP_6F(0x24, 60)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E")
    OP_6F(0x25, 0)
    Jump("loc_425")

    label("loc_41E")

    OP_6F(0x25, 60)

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437")
    OP_6F(0x26, 0)
    Jump("loc_43E")

    label("loc_437")

    OP_6F(0x26, 60)

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450")
    OP_6F(0x27, 0)
    Jump("loc_457")

    label("loc_450")

    OP_6F(0x27, 60)

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469")
    OP_6F(0x28, 0)
    Jump("loc_470")

    label("loc_469")

    OP_6F(0x28, 60)

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482")
    OP_6F(0x29, 0)
    Jump("loc_489")

    label("loc_482")

    OP_6F(0x29, 60)

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    OP_6F(0x2A, 0)
    Jump("loc_4A2")

    label("loc_49B")

    OP_6F(0x2A, 60)

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 0)), scpexpr(EXPR_END)), "loc_4AE")
    SetChrFlags(0x8, 0x80)

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 1)), scpexpr(EXPR_END)), "loc_4BA")
    SetChrFlags(0x9, 0x80)

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 2)), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0xA, 0x80)

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 3)), scpexpr(EXPR_END)), "loc_4D2")
    SetChrFlags(0xB, 0x80)

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 4)), scpexpr(EXPR_END)), "loc_4DE")
    SetChrFlags(0xC, 0x80)

    label("loc_4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 5)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0xD, 0x80)

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 6)), scpexpr(EXPR_END)), "loc_4F6")
    SetChrFlags(0xE, 0x80)

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 7)), scpexpr(EXPR_END)), "loc_502")
    SetChrFlags(0xF, 0x80)

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 0)), scpexpr(EXPR_END)), "loc_50E")
    SetChrFlags(0x10, 0x80)

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 1)), scpexpr(EXPR_END)), "loc_51A")
    SetChrFlags(0x11, 0x80)

    label("loc_51A")

    Call(0, 9)
    OP_1B(0x0, 0x0, 0xF)
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x13)
    OP_1B(0x3, 0x0, 0x15)
    Return()

    # Function_1_3F3 end

    def Function_2_533(): pass

    label("Function_2_533")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_5A2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F40)
    Jump("loc_608")

    label("loc_5A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_608")

    Jump("loc_63C")

    label("loc_60B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_63C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_533 end

    def Function_3_64A(): pass

    label("Function_3_64A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xE3, 1)"), scpexpr(EXPR_END)), "loc_6B9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xE3\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F42)
    Jump("loc_71F")

    label("loc_6B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xE3\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE3\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_71F")

    Jump("loc_753")

    label("loc_722")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_753")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_64A end

    def Function_4_761(): pass

    label("Function_4_761")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_839")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF0, 1)"), scpexpr(EXPR_END)), "loc_7D0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF0\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F44)
    Jump("loc_836")

    label("loc_7D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF0\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF0\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_836")

    Jump("loc_86A")

    label("loc_839")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_86A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_761 end

    def Function_5_878(): pass

    label("Function_5_878")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_8E7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F46)
    Jump("loc_94D")

    label("loc_8E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_94D")

    Jump("loc_981")

    label("loc_950")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_981")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_878 end

    def Function_6_98F(): pass

    label("Function_6_98F")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x1E)
    OP_73(0x28)
    OP_6F(0x28, 30)
    AddSepith(0x2, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x00得到了\x07\x02#58I火之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F47)
    Jump("loc_A79")

    label("loc_A5F")


    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A79")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_98F end

    def Function_7_A8B(): pass

    label("Function_7_A8B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B63")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_AFA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F48)
    Jump("loc_B60")

    label("loc_AFA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_B60")

    Jump("loc_B94")

    label("loc_B63")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B94")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A8B end

    def Function_8_BA2(): pass

    label("Function_8_BA2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_C11")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F49)
    Jump("loc_C77")

    label("loc_C11")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_C77")

    Jump("loc_CAB")

    label("loc_C7A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CAB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_BA2 end

    def Function_9_CB9(): pass

    label("Function_9_CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 6)), scpexpr(EXPR_END)), "loc_D4B")
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_6F(0xA, 360)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    Jump("loc_DD3")

    label("loc_D4B")

    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 7)), scpexpr(EXPR_END)), "loc_E87")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Jump("loc_F31")

    label("loc_E87")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 0)), scpexpr(EXPR_END)), "loc_FC3")
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_6F(0x12, 360)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)
    Jump("loc_104B")

    label("loc_FC3")

    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)

    label("loc_104B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 2)), scpexpr(EXPR_END)), "loc_10FF")
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x20, 0x20)
    OP_72(0x21, 0x20)
    OP_72(0x22, 0x20)
    OP_72(0x23, 0x20)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_72(0x20, 0x8)
    OP_72(0x21, 0x8)
    OP_72(0x22, 0x8)
    OP_72(0x23, 0x8)
    OP_6F(0x1A, 360)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6F(0x22, 0)
    OP_6F(0x23, 0)
    Jump("loc_11A9")

    label("loc_10FF")

    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x20, 0x20)
    OP_72(0x21, 0x20)
    OP_72(0x22, 0x20)
    OP_72(0x23, 0x20)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_72(0x20, 0x8)
    OP_72(0x21, 0x8)
    OP_72(0x22, 0x8)
    OP_72(0x23, 0x8)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6F(0x22, 0)
    OP_6F(0x23, 0)

    label("loc_11A9")

    Return()

    # Function_9_CB9 end

    def Function_10_11AA(): pass

    label("Function_10_11AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FF")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0xA, 0x78)
    OP_70(0xA, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0xE, 0x64)
    OP_B0(0xF, 0x64)
    OP_B0(0x10, 0x64)
    OP_B0(0x11, 0x64)
    OP_70(0xE, 0xF0)
    Sleep(100)
    OP_70(0xF, 0xF0)
    Sleep(100)
    OP_70(0x10, 0xF0)
    Sleep(100)
    OP_70(0x11, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0xB, 0x64)
    OP_B0(0xC, 0x64)
    OP_B0(0xD, 0x64)
    OP_70(0xB, 0x168)
    OP_70(0xC, 0x168)
    OP_70(0xD, 0x168)
    OP_73(0xB)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #20
        (
            "\x07\x05#1S『关于湖岸的地下设施（１／４）』\x01",
            "　\x01",
            "要使■■■■构』■形\x01",
            "巨■■■■■■\x01",
            "■■模■■施■是不可■■的\x01",
            "■先，作■■量■■，\x01",
            "我们研究■■■■『■■的利用\x01",
            "　\x01",
            "■』对人的愿望■■■■\x01",
            "■予恩■\x01",
            "也就是■，可以■此想到\x01",
            "是否只要是■实现人的愿望，就可以从『环』中■■■应的能量\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x05#1S……■■■种■■没能■得■。\x01",
            "■■』在拥有了■主性■■■久，\x01",
            "那种■■■人们的■■\x01",
            "■为了■方■的■予\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\x01\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x401, 1)
    OP_A2(0x1E0E)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0xA, 360)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6D(44390, -7800, -49020, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 44390, -7800, -49020, 45)
    SetChrPos(0x1, 44390, -7800, -49020, 45)
    SetChrPos(0x2, 44390, -7800, -49020, 45)
    SetChrPos(0x3, 44390, -7800, -49020, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_16B8")

    label("loc_14FF")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #23
        (
            "\x07\x05#1S『关于湖岸的地下设施（１／４）』\x01",
            "　\x01",
            "要使■■■■构』■形\x01",
            "巨■■■■■■\x01",
            "■■模■■施■是不可■■的\x01",
            "■先，作■■量■■，\x01",
            "我们研究■■■■『■■的利用\x01",
            "　\x01",
            "■』对人的愿望■■■■\x01",
            "■予恩■\x01",
            "也就是■，可以■此想到\x01",
            "是否只要是■实现人的愿望，就可以从『环』中■■■应的能量\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05#1S……■■■种■■没能■得■。\x01",
            "■■』在拥有了■主性■■■久，\x01",
            "那种■■■人们的■■\x01",
            "■为了■方■的■予\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_16B8")

    TalkEnd(0xFF)
    Return()

    # Function_10_11AA end

    def Function_11_16BC(): pass

    label("Function_11_16BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A39")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_70(0x0, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x4, 0x64)
    OP_B0(0x5, 0x64)
    OP_B0(0x6, 0x64)
    OP_B0(0x7, 0x64)
    OP_B0(0x8, 0x64)
    OP_B0(0x9, 0x64)
    OP_70(0x4, 0xF0)
    Sleep(100)
    OP_70(0x5, 0xF0)
    Sleep(100)
    OP_70(0x6, 0xF0)
    Sleep(100)
    OP_70(0x7, 0xF0)
    Sleep(100)
    OP_70(0x8, 0xF0)
    Sleep(100)
    OP_70(0x9, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1, 0x64)
    OP_B0(0x2, 0x64)
    OP_B0(0x3, 0x64)
    OP_70(0x1, 0x168)
    OP_70(0x2, 0x168)
    OP_70(0x3, 0x168)
    OP_73(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #25
        (
            "\x07\x05#1S『关于湖岸的地下设施（２／４）』\x01",
            "　\x01",
            "■■■环■的力量■■■■法实现。\x01",
            "#1S于是我们■■意力■向了城■外部\x01",
            "■■找■■深■■埋■在大地■的七耀脉■■，\x01",
            "并■■图在那■■■■施。\x01",
            "　\x01",
            "■是，我们■经\x01",
            "被置于『■』■监■之下\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #26
        (
            "\x07\x05#1S■环』的■■■■\x01",
            "似乎是■■■的存续放■第■位\x01",
            "而排■■■■能对此■成■胁的■■\x01",
            "　\x01",
            "■■■了■■『■』，\x01",
            "我们在观■七■■的名义下■■■设■■建造。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\x02\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x402, 1)
    OP_A2(0x1E0F)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    OP_6D(44260, -7800, 44300, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 44260, -7800, 44300, 45)
    SetChrPos(0x1, 44260, -7800, 44300, 45)
    SetChrPos(0x2, 44260, -7800, 44300, 45)
    SetChrPos(0x3, 44260, -7800, 44300, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_1BEC")

    label("loc_1A39")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #28
        (
            "\x07\x05#1S『关于湖岸的地下设施（２／４）』\x01",
            "　\x01",
            "■■■环■的力量■■■■法实现。\x01",
            "#1S于是我们■■意力■向了城■外部\x01",
            "■■找■■深■■埋■在大地■的七耀脉■■，\x01",
            "并■■图在那■■■■施。\x01",
            "　\x01",
            "■是，我们■经\x01",
            "被置于『■』■监■之下\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #29
        (
            "\x07\x05#1S■环』的■■■■\x01",
            "似乎是■■■的存续放■第■位\x01",
            "而排■■■■能对此■成■胁的■■\x01",
            "　\x01",
            "■■■了■■『■』，\x01",
            "我们在观■七■■的名义下■■■设■■建造。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1BEC")

    TalkEnd(0xFF)
    Return()

    # Function_11_16BC end

    def Function_12_1BF0(): pass

    label("Function_12_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFB")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x12, 0x78)
    OP_70(0x12, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x16, 0x64)
    OP_B0(0x17, 0x64)
    OP_B0(0x18, 0x64)
    OP_B0(0x19, 0x64)
    OP_70(0x16, 0xF0)
    Sleep(100)
    OP_70(0x17, 0xF0)
    Sleep(100)
    OP_70(0x18, 0xF0)
    Sleep(100)
    OP_70(0x19, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x13, 0x64)
    OP_B0(0x14, 0x64)
    OP_B0(0x15, 0x64)
    OP_70(0x13, 0x168)
    OP_70(0x14, 0x168)
    OP_70(0x15, 0x168)
    OP_73(0x13)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #30
        (
            "\x07\x05#1S『关于湖岸的地下设施（３／４）』\x01",
            "　\x01",
            "设施■■■■雷利亚■东■\x01",
            "地下5■0■■的■方。\x01",
            "#1S■■调■，\x01",
            "那里是七■脉■■■中■地方。\x01",
            "　\x01",
            "延展至城■之下■■地\x01",
            "被郁郁■葱■原生■包围。\x01",
            "#1S■■■足，\x01",
            "没有任■事物对工程■■■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x05#1S■■一边逃避『■』■监视，\x01",
            "一边■结■■■■力量\x01",
            "抓紧■行地下■■的■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #32
        "\x07\x00得到了\x1F\x03\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x403, 1)
    OP_A2(0x1E10)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x12, 360)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)
    OP_6D(-49000, -7800, -49110, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -49000, -7800, -49110, 45)
    SetChrPos(0x1, -49000, -7800, -49110, 45)
    SetChrPos(0x2, -49000, -7800, -49110, 45)
    SetChrPos(0x3, -49000, -7800, -49110, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_206A")

    label("loc_1EFB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #33
        (
            "\x07\x05#1S『关于湖岸的地下设施（３／４）』\x01",
            "　\x01",
            "设施■■■■雷利亚■东■\x01",
            "地下5■0■■的■方。\x01",
            "#1S■■调■，\x01",
            "那里是七■脉■■■中■地方。\x01",
            "　\x01",
            "延展至城■之下■■地\x01",
            "被郁郁■葱■原生■包围。\x01",
            "#1S■■■足，\x01",
            "没有任■事物对工程■■■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #34
        (
            "\x07\x05#1S■■一边逃避『■』■监视，\x01",
            "一边■结■■■■力量\x01",
            "抓紧■行地下■■的■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_206A")

    TalkEnd(0xFF)
    Return()

    # Function_12_1BF0 end

    def Function_13_206E(): pass

    label("Function_13_206E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CA")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x1A, 0x78)
    OP_70(0x1A, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x1E, 0x64)
    OP_B0(0x1F, 0x64)
    OP_B0(0x20, 0x64)
    OP_B0(0x21, 0x64)
    OP_B0(0x22, 0x64)
    OP_B0(0x23, 0x64)
    OP_70(0x1E, 0xF0)
    Sleep(100)
    OP_70(0x1F, 0xF0)
    Sleep(100)
    OP_70(0x20, 0xF0)
    Sleep(100)
    OP_70(0x21, 0xF0)
    Sleep(100)
    OP_70(0x22, 0xF0)
    Sleep(100)
    OP_70(0x23, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1B, 0x64)
    OP_B0(0x1C, 0x64)
    OP_B0(0x1D, 0x64)
    OP_70(0x1B, 0x168)
    OP_70(0x1C, 0x168)
    OP_70(0x1D, 0x168)
    OP_73(0x1B)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #35
        (
            "\x07\x05#1S『关于湖岸的地下设施（４／４）』\x01",
            "　\x01",
            "推进地下■■■建■■期间，\x01",
            "■们在『环■■■■的情况■，\x01",
            "■■面■边\x01",
            "建成■■巨大■■■物。\x01",
            "　\x01",
            "■■■■■相同\x01",
            "朝向■■』■■向的■■■■宁堡』\x01",
            "另■种是为■■■■■\x01",
            "而■■的4个■■■塔■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #36
        (
            "\x07\x05#1S这两■建■■在计■■\x01",
            "分■有着■■■要■任务，\x01",
            "它们■■下■■同■，\x01",
            "是■封印机构■■■■或缺■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x00得到了\x1F\x04\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x404, 1)
    OP_A2(0x1E1A)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1A, 360)
    OP_6F(0x1B, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6F(0x22, 0)
    OP_6F(0x23, 0)
    OP_6D(-49080, -7800, 44450, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -49080, -7800, 44450, 45)
    SetChrPos(0x1, -49080, -7800, 44450, 45)
    SetChrPos(0x2, -49080, -7800, 44450, 45)
    SetChrPos(0x3, -49080, -7800, 44450, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_2555")

    label("loc_23CA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #38
        (
            "\x07\x05#1S『关于湖岸的地下设施（４／４）』\x01",
            "　\x01",
            "推进地下■■■建■■期间，\x01",
            "■们在『环■■■■的情况■，\x01",
            "■■面■边\x01",
            "建成■■巨大■■■物。\x01",
            "　\x01",
            "■■■■■相同\x01",
            "朝向■■』■■向的■■■■宁堡』\x01",
            "另■种是为■■■■■\x01",
            "而■■的4个■■■塔■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #39
        (
            "\x07\x05#1S这两■建■■在计■■\x01",
            "分■有着■■■要■任务，\x01",
            "它们■■下■■同■，\x01",
            "是■封印机构■■■■或缺■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2555")

    TalkEnd(0xFF)
    Return()

    # Function_13_206E end

    def Function_14_2559(): pass

    label("Function_14_2559")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(66500, -210, 0, 0)
    SetChrPos(0x101, 66000, -210, -500, 270)
    SetChrPos(0x102, 66000, -210, 500, 270)
    SetChrPos(0xF8, 67000, -210, -500, 270)
    SetChrPos(0xF9, 67000, -210, 500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    Fade(500)
    OP_6D(64530, -210, -40, 0)
    SetChrPos(0x0, 64530, -210, -40, 270)
    SetChrPos(0x1, 64530, -210, -40, 270)
    SetChrPos(0x2, 64530, -210, -40, 270)
    SetChrPos(0x3, 64530, -210, -40, 270)
    EventEnd(0x0)
    Return()

    # Function_14_2559 end

    def Function_15_2654(): pass

    label("Function_15_2654")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(66500, -210, 0, 0)
    SetChrPos(0x101, 67000, -210, 500, 90)
    SetChrPos(0x102, 67000, -210, -500, 90)
    SetChrPos(0xF8, 66000, -210, 500, 90)
    SetChrPos(0xF9, 66000, -210, -500, 90)
    OP_0D()
    Call(0, 22)
    Call(0, 25)
    NewScene("ED6_DT21/C3601   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2654 end

    def Function_16_26CC(): pass

    label("Function_16_26CC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -7360, 500, 0)
    SetChrPos(0x101, 500, -7360, 0, 180)
    SetChrPos(0x102, -500, -7360, 0, 180)
    SetChrPos(0xF8, 500, -7360, 1000, 180)
    SetChrPos(0xF9, -500, -7360, 1000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    Fade(500)
    OP_6D(30, -7360, -1280, 0)
    SetChrPos(0x0, 30, -7360, -1280, 180)
    SetChrPos(0x1, 30, -7360, -1280, 180)
    SetChrPos(0x2, 30, -7360, -1280, 180)
    SetChrPos(0x3, 30, -7360, -1280, 180)
    EventEnd(0x0)
    Return()

    # Function_16_26CC end

    def Function_17_27C7(): pass

    label("Function_17_27C7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, -7360, 500, 0)
    SetChrPos(0x101, -500, -7360, 1000, 0)
    SetChrPos(0x102, 500, -7360, 1000, 0)
    SetChrPos(0xF8, -500, -7360, 0, 0)
    SetChrPos(0xF9, 500, -7360, 0, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 25)
    NewScene("ED6_DT21/C3601   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_27C7 end

    def Function_18_283F(): pass

    label("Function_18_283F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-66500, -210, 0, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -66000, -210, 500, 90)
    SetChrPos(0x102, -66000, -210, -500, 90)
    SetChrPos(0xF8, -67000, -210, 500, 90)
    SetChrPos(0xF9, -67000, -210, -500, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    Fade(500)
    OP_6D(-64580, -210, 80, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -64580, -210, 80, 90)
    SetChrPos(0x1, -64580, -210, 80, 90)
    SetChrPos(0x2, -64580, -210, 80, 90)
    SetChrPos(0x3, -64580, -210, 80, 90)
    EventEnd(0x0)
    Return()

    # Function_18_283F end

    def Function_19_294C(): pass

    label("Function_19_294C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-66500, -210, 0, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -67000, -210, -500, 270)
    SetChrPos(0x102, -67000, -210, 500, 270)
    SetChrPos(0xF8, -66000, -210, -500, 270)
    SetChrPos(0xF9, -66000, -210, 500, 270)
    OP_0D()
    Call(0, 22)
    Call(0, 25)
    NewScene("ED6_DT21/C3601   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_19_294C end

    def Function_20_29CD(): pass

    label("Function_20_29CD")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -210, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -500, -210, -66000, 0)
    SetChrPos(0x102, 500, -210, -66000, 0)
    SetChrPos(0xF8, -500, -210, -67000, 0)
    SetChrPos(0xF9, 500, -210, -67000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 23)
    Call(0, 24)
    Fade(500)
    OP_6D(60, -210, -64319, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 60, -210, -64319, 0)
    SetChrPos(0x1, 60, -210, -64319, 0)
    SetChrPos(0x2, 60, -210, -64319, 0)
    SetChrPos(0x3, 60, -210, -64319, 0)
    EventEnd(0x0)
    Return()

    # Function_20_29CD end

    def Function_21_2ADA(): pass

    label("Function_21_2ADA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, -210, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 500, -210, -67000, 180)
    SetChrPos(0x102, -500, -210, -67000, 180)
    SetChrPos(0xF8, 500, -210, -66000, 180)
    SetChrPos(0xF9, -500, -210, -66000, 180)
    OP_0D()
    Call(0, 23)
    Call(0, 25)
    NewScene("ED6_DT21/C3603   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2ADA end

    def Function_22_2B5B(): pass

    label("Function_22_2B5B")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_22_2B5B end

    def Function_23_2C4E(): pass

    label("Function_23_2C4E")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_23_2C4E end

    def Function_24_2D41(): pass

    label("Function_24_2D41")


    def lambda_2D47():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D47)

    def lambda_2D59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2D59)

    def lambda_2D6B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2D6B)

    def lambda_2D7D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2D7D)
    Sleep(2500)
    Return()

    # Function_24_2D41 end

    def Function_25_2D8F(): pass

    label("Function_25_2D8F")


    def lambda_2D95():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D95)

    def lambda_2DA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2DA7)

    def lambda_2DB9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2DB9)

    def lambda_2DCB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2DCB)
    Sleep(2000)
    Return()

    # Function_25_2D8F end

    SaveToFile()

Try(main)
