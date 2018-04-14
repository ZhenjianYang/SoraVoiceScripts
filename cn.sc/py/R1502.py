from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1502   ._SN',
        MapName             = 'Bose',
        Location            = 'R1502.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
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
        '命运编造者',                           # 9
        '拉文努村方向',                         # 10
        '拉文努废坑方向',                       # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH10030 ._CH',             # 00
        'ED6_DT09/CH10031 ._CH',             # 01
        'ED6_DT09/CH10860 ._CH',             # 02
        'ED6_DT09/CH10861 ._CH',             # 03
        'ED6_DT09/CH10310 ._CH',             # 04
        'ED6_DT09/CH10311 ._CH',             # 05
        'ED6_DT09/CH10330 ._CH',             # 06
        'ED6_DT09/CH10331 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10030P._CP',             # 00
        'ED6_DT09/CH10031P._CP',             # 01
        'ED6_DT09/CH10860P._CP',             # 02
        'ED6_DT09/CH10861P._CP',             # 03
        'ED6_DT09/CH10310P._CP',             # 04
        'ED6_DT09/CH10311P._CP',             # 05
        'ED6_DT09/CH10330P._CP',             # 06
        'ED6_DT09/CH10331P._CP',             # 07
    )

    DeclNpc(
        X                   = -8730,
        Z                   = -140,
        Y                   = 1940,
        Direction           = 270,
        Unknown2            = 2,
        Unknown3            = 131072,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4760,
        Z                   = 10,
        Y                   = -38310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -62970,
        Z                   = -30,
        Y                   = 86680,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -31260,
        Z                   = -20,
        Y                   = -41320,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40880,
        Z                   = 20,
        Y                   = -10170,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35910,
        Z                   = -40,
        Y                   = 12760,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88970,
        Z                   = -90,
        Y                   = -16370,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -70020,
        Z                   = -20,
        Y                   = 24980,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81390,
        Z                   = -70,
        Y                   = 41540,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -8730,
        Y                   = -140,
        Z                   = 1940,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -98600,
        TriggerZ            = -90,
        TriggerY            = 21830,
        TriggerRange        = 1000,
        ActorX              = -98170,
        ActorZ              = 1490,
        ActorY              = 22340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -95400,
        TriggerZ            = -120,
        TriggerY            = 32479,
        TriggerRange        = 1000,
        ActorX              = -95800,
        ActorZ              = -120,
        ActorY              = 32080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1440,
        TriggerZ            = -20,
        TriggerY            = 7890,
        TriggerRange        = 1000,
        ActorX              = -790,
        ActorZ              = -20,
        ActorY              = 8100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -96250,
        TriggerZ            = -90,
        TriggerY            = -17480,
        TriggerRange        = 1000,
        ActorX              = -96950,
        ActorZ              = -90,
        ActorY              = -17530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A2",          # 00, 0
        "Function_1_2A3",          # 01, 1
        "Function_2_3A5",          # 02, 2
        "Function_3_3BB",          # 03, 3
        "Function_4_576",          # 04, 4
        "Function_5_577",          # 05, 5
        "Function_6_68E",          # 06, 6
        "Function_7_7A5",          # 07, 7
    )


    def Function_0_2A2(): pass

    label("Function_0_2A2")

    Return()

    # Function_0_2A2 end

    def Function_1_2A3(): pass

    label("Function_1_2A3")

    OP_16(0x2, 0xFA0, 0xFFFD40E0, 0xFFFE4698, 0x230021)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CD")
    OP_B1("R1502_y")
    Jump("loc_2D6")

    label("loc_2CD")

    OP_B1("R1502_n")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x365, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8")
    OP_6F(0x1, 0)
    Jump("loc_2EF")

    label("loc_2E8")

    OP_6F(0x1, 60)

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x365, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301")
    OP_6F(0x2, 0)
    Jump("loc_308")

    label("loc_301")

    OP_6F(0x2, 60)

    label("loc_308")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    OP_64(0x3, 0x1)
    OP_71(0x3, 0x0)
    OP_71(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_354")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_364")
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_37A")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_END)), "loc_374")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_37A")

    label("loc_374")

    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_37A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_392")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_392")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_3A4")

    Return()

    # Function_1_2A3 end

    def Function_2_3A5(): pass

    label("Function_2_3A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3A5")

    label("loc_3BA")

    Return()

    # Function_2_3A5 end

    def Function_3_3BB(): pass

    label("Function_3_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35F, 5)), scpexpr(EXPR_END)), "loc_3C3")
    Return()

    label("loc_3C3")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4A8"),
        (SWITCH_DEFAULT, "loc_4CB"),
    )


    label("loc_4A8")

    Fade(500)
    OP_89(0x0, -15290, -10, 5520, 135)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_4CB")

    Battle(0xEFB, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -15290, -10, 5520, 135)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_504"),
        (1, "loc_507"),
        (SWITCH_DEFAULT, "loc_50A"),
    )


    label("loc_504")

    EventEnd(0x0)
    Return()

    label("loc_507")

    OP_B4(0x0)
    Return()

    label("loc_50A")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x1AFD)
    OP_28(0xB4, 0x4, 0x10)
    OP_28(0xB4, 0x4, 0x2)
    OP_28(0xB4, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_3BB end

    def Function_4_576(): pass

    label("Function_4_576")

    Return()

    # Function_4_576 end

    def Function_5_577(): pass

    label("Function_5_577")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x365, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_5E6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B29)
    Jump("loc_64C")

    label("loc_5E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_64C")

    Jump("loc_680")

    label("loc_64F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_680")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_577 end

    def Function_6_68E(): pass

    label("Function_6_68E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x365, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_766")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_6FD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B2A)
    Jump("loc_763")

    label("loc_6FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_763")

    Jump("loc_797")

    label("loc_766")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_797")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_68E end

    def Function_7_7A5(): pass

    label("Function_7_7A5")

    Return()

    # Function_7_7A5 end

    SaveToFile()

Try(main)
