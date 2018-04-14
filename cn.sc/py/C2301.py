from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2301   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2301.x',
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
        '守护者',                               # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12730 ._CH',             # 00
        'ED6_DT29/CH12731 ._CH',             # 01
        'ED6_DT29/CH12740 ._CH',             # 02
        'ED6_DT29/CH12741 ._CH',             # 03
        'ED6_DT29/CH12750 ._CH',             # 04
        'ED6_DT29/CH12751 ._CH',             # 05
        'ED6_DT29/CH12760 ._CH',             # 06
        'ED6_DT29/CH12761 ._CH',             # 07
        'ED6_DT29/CH12770 ._CH',             # 08
        'ED6_DT29/CH12771 ._CH',             # 09
        'ED6_DT29/CH12780 ._CH',             # 0A
        'ED6_DT29/CH12781 ._CH',             # 0B
        'ED6_DT29/CH12790 ._CH',             # 0C
        'ED6_DT29/CH12791 ._CH',             # 0D
        'ED6_DT27/CH04000 ._CH',             # 0E
        'ED6_DT27/CH04010 ._CH',             # 0F
        'ED6_DT07/CH00120 ._CH',             # 10
        'ED6_DT07/CH00150 ._CH',             # 11
        'ED6_DT07/CH00140 ._CH',             # 12
        'ED6_DT07/CH00160 ._CH',             # 13
        'ED6_DT07/CH00170 ._CH',             # 14
        'ED6_DT27/CH04080 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT29/CH12730P._CP',             # 00
        'ED6_DT29/CH12731P._CP',             # 01
        'ED6_DT29/CH12740P._CP',             # 02
        'ED6_DT29/CH12741P._CP',             # 03
        'ED6_DT29/CH12750P._CP',             # 04
        'ED6_DT29/CH12751P._CP',             # 05
        'ED6_DT29/CH12760P._CP',             # 06
        'ED6_DT29/CH12761P._CP',             # 07
        'ED6_DT29/CH12770P._CP',             # 08
        'ED6_DT29/CH12771P._CP',             # 09
        'ED6_DT29/CH12780P._CP',             # 0A
        'ED6_DT29/CH12781P._CP',             # 0B
        'ED6_DT29/CH12790P._CP',             # 0C
        'ED6_DT29/CH12791P._CP',             # 0D
        'ED6_DT27/CH04000P._CP',             # 0E
        'ED6_DT27/CH04010P._CP',             # 0F
        'ED6_DT07/CH00120P._CP',             # 10
        'ED6_DT07/CH00150P._CP',             # 11
        'ED6_DT07/CH00140P._CP',             # 12
        'ED6_DT07/CH00160P._CP',             # 13
        'ED6_DT07/CH00170P._CP',             # 14
        'ED6_DT27/CH04080P._CP',             # 15
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -4440,
        Z                   = 400,
        Y                   = -40370,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7838,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4560,
        Z                   = 400,
        Y                   = -40400,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7839,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 350,
        Z                   = 200,
        Y                   = -7490,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7840,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 310,
        Z                   = 50,
        Y                   = 8930,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7841,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 510,
        Z                   = 0,
        Y                   = 370,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7842,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -4000,
        Y                   = 0,
        Z                   = 29000,
        Range               = 4000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x7EFD,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -5380,
        TriggerZ            = 400,
        TriggerY            = -9620,
        TriggerRange        = 1000,
        ActorX              = -5850,
        ActorZ              = 400,
        ActorY              = -10080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5300,
        TriggerZ            = 400,
        TriggerY            = -110,
        TriggerRange        = 1000,
        ActorX              = -5980,
        ActorZ              = 400,
        ActorY              = -50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5470,
        TriggerZ            = 400,
        TriggerY            = 11520,
        TriggerRange        = 1000,
        ActorX              = -5880,
        ActorZ              = 400,
        ActorY              = 11930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5580,
        TriggerZ            = 400,
        TriggerY            = 11420,
        TriggerRange        = 1000,
        ActorX              = 6050,
        ActorZ              = 400,
        ActorY              = 11880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5280,
        TriggerZ            = 400,
        TriggerY            = 300,
        TriggerRange        = 1000,
        ActorX              = 5970,
        ActorZ              = 400,
        ActorY              = 50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5470,
        TriggerZ            = 400,
        TriggerY            = -9530,
        TriggerRange        = 1000,
        ActorX              = 6030,
        ActorZ              = 400,
        ActorY              = -10090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 38890,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 0,
        ActorY              = 38890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_341",          # 01, 1
        "Function_2_538",          # 02, 2
        "Function_3_54E",          # 03, 3
        "Function_4_665",          # 04, 4
        "Function_5_77C",          # 05, 5
        "Function_6_893",          # 06, 6
        "Function_7_9AA",          # 07, 7
        "Function_8_AC1",          # 08, 8
        "Function_9_BBD",          # 09, 9
        "Function_10_1303",        # 0A, 10
        "Function_11_132A",        # 0B, 11
        "Function_12_1351",        # 0C, 12
        "Function_13_1378",        # 0D, 13
        "Function_14_13DA",        # 0E, 14
        "Function_15_184E",        # 0F, 15
        "Function_16_18D5",        # 10, 16
        "Function_17_1962",        # 11, 17
        "Function_18_1A6F",        # 12, 18
        "Function_19_1AF0",        # 13, 19
        "Function_20_1BEB",        # 14, 20
        "Function_21_1C63",        # 15, 21
        "Function_22_1D56",        # 16, 22
        "Function_23_1E49",        # 17, 23
        "Function_24_1E97",        # 18, 24
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_332"),
        (101, "loc_339"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_332")

    Event(0, 17)
    Jump("loc_340")

    label("loc_339")

    Event(0, 19)
    Jump("loc_340")

    label("loc_340")

    Return()

    # Function_0_322 end

    def Function_1_341(): pass

    label("Function_1_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353")
    OP_6F(0x8, 0)
    Jump("loc_35A")

    label("loc_353")

    OP_6F(0x8, 60)

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C")
    OP_6F(0x9, 0)
    Jump("loc_373")

    label("loc_36C")

    OP_6F(0x9, 60)

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385")
    OP_6F(0xA, 0)
    Jump("loc_38C")

    label("loc_385")

    OP_6F(0xA, 60)

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    OP_6F(0xB, 0)
    Jump("loc_3A5")

    label("loc_39E")

    OP_6F(0xB, 60)

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7")
    OP_6F(0xC, 0)
    Jump("loc_3BE")

    label("loc_3B7")

    OP_6F(0xC, 60)

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")
    OP_6F(0xD, 0)
    Jump("loc_3D7")

    label("loc_3D0")

    OP_6F(0xD, 60)

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 6)), scpexpr(EXPR_END)), "loc_3E3")
    SetChrFlags(0x9, 0x80)

    label("loc_3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 7)), scpexpr(EXPR_END)), "loc_3EF")
    SetChrFlags(0xA, 0x80)

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 0)), scpexpr(EXPR_END)), "loc_3FB")
    SetChrFlags(0xB, 0x80)

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 1)), scpexpr(EXPR_END)), "loc_407")
    SetChrFlags(0xC, 0x80)

    label("loc_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 2)), scpexpr(EXPR_END)), "loc_413")
    SetChrFlags(0xD, 0x80)

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 3)), scpexpr(EXPR_END)), "loc_4A5")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    Jump("loc_52D")

    label("loc_4A5")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)

    label("loc_52D")

    OP_1B(0x0, 0x0, 0x12)
    OP_1B(0x1, 0x0, 0x14)
    Return()

    # Function_1_341 end

    def Function_2_538(): pass

    label("Function_2_538")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_538")

    label("loc_54D")

    Return()

    # Function_2_538 end

    def Function_3_54E(): pass

    label("Function_3_54E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_5BD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F70)
    Jump("loc_623")

    label("loc_5BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_623")

    Jump("loc_657")

    label("loc_626")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_657")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_54E end

    def Function_4_665(): pass

    label("Function_4_665")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_6D4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F71)
    Jump("loc_73A")

    label("loc_6D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_73A")

    Jump("loc_76E")

    label("loc_73D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_76E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_665 end

    def Function_5_77C(): pass

    label("Function_5_77C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_854")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_7EB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F72)
    Jump("loc_851")

    label("loc_7EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_851")

    Jump("loc_885")

    label("loc_854")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_885")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_77C end

    def Function_6_893(): pass

    label("Function_6_893")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_902")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F73)
    Jump("loc_968")

    label("loc_902")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_968")

    Jump("loc_99C")

    label("loc_96B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_99C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_893 end

    def Function_7_9AA(): pass

    label("Function_7_9AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_A19")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F74)
    Jump("loc_A7F")

    label("loc_A19")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_A7F")

    Jump("loc_AB3")

    label("loc_A82")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9AA end

    def Function_8_AC1(): pass

    label("Function_8_AC1")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B91")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_6F(0xD, 30)
    AddSepith(0x1, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        (
            "\x07\x00得到了\x07\x02#57I水之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F75)
    Jump("loc_BAB")

    label("loc_B91")


    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_BAB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_AC1 end

    def Function_9_BBD(): pass

    label("Function_9_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 5)), scpexpr(EXPR_END)), "loc_BC5")
    Return()

    label("loc_BC5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BEA")
    Call(0, 15)
    Call(0, 16)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_BEA")

    Fade(1000)
    OP_6D(170, 400, 34390, 0)
    OP_67(0, 5030, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, 600, 400, 31000, 0)
    SetChrPos(0x102, -300, 400, 31000, 0)
    SetChrPos(0x103, 1000, 400, 29300, 0)
    SetChrPos(0xF9, -700, 400, 29300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103D")
    OP_A2(0x1E14)
    OP_22(0x118, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF7")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D35")

    label("loc_CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D35")

    label("loc_D1E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D35")

    Sleep(1000)

    ChrTalk(    #17
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#1042F#6P刚才那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        "#024F#6P……退下！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 2500, 36580, 180)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)

    def lambda_DC8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DC8)

    def lambda_DDA():
        OP_8F(0xFE, 0x0, 0x2BC, 0x8EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DDA)

    def lambda_DF5():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF5)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x103, 0x0, 0x0, 0xC)
    Sleep(100)
    OP_43(0x102, 0x0, 0x0, 0xB)
    Sleep(100)
    OP_43(0x101, 0x0, 0x0, 0xA)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_E4E():
        OP_6D(170, 400, 31000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E4E)

    def lambda_E66():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E66)
    SetChrChipByIndex(0x8, 11)

    def lambda_E7B():
        OP_8F(0xFE, 0x96, 0x1F4, 0x7896, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E7B)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0xFF)
    Battle(0x409, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_EBA"),
        (2, "loc_F7B"),
        (1, "loc_1035"),
        (SWITCH_DEFAULT, "loc_103A"),
    )


    label("loc_EBA")

    EventBegin(0x0)
    OP_44(0x8, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6D(460, 400, 30560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 460, 400, 30560, 0)
    SetChrPos(0x1, 460, 400, 30560, 0)
    SetChrPos(0x2, 460, 400, 30560, 0)
    SetChrPos(0x3, 460, 400, 30560, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x1E15)
    Jump("loc_103A")

    label("loc_F7B")

    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    OP_6D(-30, 400, 25940, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 400, 25940, 0)
    SetChrPos(0x1, 0, 400, 25940, 0)
    SetChrPos(0x2, 0, 400, 25940, 0)
    SetChrPos(0x3, 0, 400, 25940, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Jump("loc_103A")

    label("loc_1035")

    OP_B4(0x0)
    Jump("loc_103A")

    label("loc_103A")

    Jump("loc_12FF")

    label("loc_103D")

    OP_22(0x118, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 2500, 36580, 180)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)

    def lambda_108D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_108D)

    def lambda_109F():
        OP_8F(0xFE, 0x0, 0x2BC, 0x8EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_109F)

    def lambda_10BA():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10BA)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x103, 0x0, 0x0, 0xC)
    Sleep(100)
    OP_43(0x102, 0x0, 0x0, 0xB)
    Sleep(100)
    OP_43(0x101, 0x0, 0x0, 0xA)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_1113():
        OP_6D(170, 400, 31000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1113)

    def lambda_112B():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_112B)
    SetChrChipByIndex(0x8, 11)

    def lambda_1140():
        OP_8F(0xFE, 0x96, 0x1F4, 0x7896, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1140)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0xFF)
    Battle(0x409, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_117F"),
        (2, "loc_1240"),
        (1, "loc_12FA"),
        (SWITCH_DEFAULT, "loc_12FF"),
    )


    label("loc_117F")

    EventBegin(0x0)
    OP_44(0x8, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6D(460, 400, 30560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 460, 400, 30560, 0)
    SetChrPos(0x1, 460, 400, 30560, 0)
    SetChrPos(0x2, 460, 400, 30560, 0)
    SetChrPos(0x3, 460, 400, 30560, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x1E15)
    Jump("loc_12FF")

    label("loc_1240")

    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    OP_6D(-30, 400, 25940, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 400, 25940, 0)
    SetChrPos(0x1, 0, 400, 25940, 0)
    SetChrPos(0x2, 0, 400, 25940, 0)
    SetChrPos(0x3, 0, 400, 25940, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Jump("loc_12FF")

    label("loc_12FA")

    OP_B4(0x0)
    Jump("loc_12FF")

    label("loc_12FF")

    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_9_BBD end

    def Function_10_1303(): pass

    label("Function_10_1303")

    OP_96(0xFE, 0x258, 0x190, 0x7148, 0x190, 0x1770)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_10_1303 end

    def Function_11_132A(): pass

    label("Function_11_132A")

    OP_96(0xFE, 0xFFFFFED4, 0x190, 0x7148, 0x190, 0x1770)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_132A end

    def Function_12_1351(): pass

    label("Function_12_1351")

    OP_96(0xFE, 0x3E8, 0x190, 0x6AA4, 0x190, 0x1770)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_1351 end

    def Function_13_1378(): pass

    label("Function_13_1378")

    OP_96(0xFE, 0xFFFFFD44, 0x190, 0x6AA4, 0x190, 0x1770)
    SetChrSubChip(0xFE, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_13B1"),
        (4, "loc_13B9"),
        (6, "loc_13C1"),
        (7, "loc_13C9"),
        (8, "loc_13D1"),
        (SWITCH_DEFAULT, "loc_13D9"),
    )


    label("loc_13B1")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_13D9")

    label("loc_13B9")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_13D9")

    label("loc_13C1")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_13D9")

    label("loc_13C9")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_13D9")

    label("loc_13D1")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_13D9")

    label("loc_13D9")

    Return()

    # Function_13_1378 end

    def Function_14_13DA(): pass

    label("Function_14_13DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E0")
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
    OP_70(0x4, 0xF0)
    Sleep(100)
    OP_70(0x5, 0xF0)
    Sleep(100)
    OP_70(0x6, 0xF0)
    Sleep(100)
    OP_70(0x7, 0xF0)
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

    AnonymousTalk(    #20
        (
            "\x07\x05#1S关于『环』的封印（１／４）\x01",
            "　\x01",
            "地■■■的建造■■完■■时候\x01",
            "■知■■中\x01",
            "『■■得知■『■■■■』\x01",
            "　\x01",
            "■因是■■同■禁不住『■』的诱■，\x01",
            "精神被■介■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x05#1S不过■那个同胞\x01",
            "并没有■■可以得知计划全貌■地■\x01",
            "■■不幸■■■■\x01",
            "　\x01",
            "『■』■■■■长城■■■■■\x01",
            "和『设■■■，\x01",
            "只捉■■湖■的■■■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\x05\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x405, 1)
    OP_A2(0x1E1B)
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
    OP_6D(350, 200, 36760, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 350, 200, 36760, 0)
    SetChrPos(0x1, 350, 200, 36760, 0)
    SetChrPos(0x2, 350, 200, 36760, 0)
    SetChrPos(0x3, 350, 200, 36760, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_184A")

    label("loc_16E0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #23
        (
            "\x07\x05#1S关于『环』的封印（１／４）\x01",
            "　\x01",
            "地■■■的建造■■完■■时候\x01",
            "■知■■中\x01",
            "『■■得知■『■■■■』\x01",
            "　\x01",
            "■因是■■同■禁不住『■』的诱■，\x01",
            "精神被■介■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05#1S不过■那个同胞\x01",
            "并没有■■可以得知计划全貌■地■\x01",
            "■■不幸■■■■\x01",
            "　\x01",
            "『■』■■■■长城■■■■■\x01",
            "和『设■■■，\x01",
            "只捉■■湖■的■■■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_184A")

    TalkEnd(0xFF)
    Return()

    # Function_14_13DA end

    def Function_15_184E(): pass

    label("Function_15_184E")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18C8"),
        (1, "loc_18CE"),
        (SWITCH_DEFAULT, "loc_18D4"),
    )


    label("loc_18C8")

    OP_A2(0x1200)
    Jump("loc_18D4")

    label("loc_18CE")

    OP_A2(0x1201)
    Jump("loc_18D4")

    label("loc_18D4")

    Return()

    # Function_15_184E end

    def Function_16_18D5(): pass

    label("Function_16_18D5")

    FadeToDark(0, 0, -1)
    OP_6D(-48940, 490, -13310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_16_18D5 end

    def Function_17_1962(): pass

    label("Function_17_1962")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 200, -66000, 0)
    SetChrPos(0x102, 500, 200, -66000, 0)
    SetChrPos(0xF8, -500, 200, -67000, 0)
    SetChrPos(0xF9, 500, 200, -67000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 21)
    Call(0, 23)
    Fade(500)
    OP_6D(-70, 200, -64510, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -70, 200, -64510, 0)
    SetChrPos(0x1, -70, 200, -64510, 0)
    SetChrPos(0x2, -70, 200, -64510, 0)
    SetChrPos(0x3, -70, 200, -64510, 0)
    EventEnd(0x0)
    Return()

    # Function_17_1962 end

    def Function_18_1A6F(): pass

    label("Function_18_1A6F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 200, -67000, 180)
    SetChrPos(0x102, -500, 200, -67000, 180)
    SetChrPos(0xF8, 500, 200, -66000, 180)
    SetChrPos(0xF9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 21)
    Call(0, 24)
    NewScene("ED6_DT21/C2300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1A6F end

    def Function_19_1AF0(): pass

    label("Function_19_1AF0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, 500, 200, 66000, 180)
    SetChrPos(0x102, -500, 200, 66000, 180)
    SetChrPos(0xF8, 500, 200, 67000, 180)
    SetChrPos(0xF9, -500, 200, 67000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 23)
    Fade(500)
    OP_6D(80, 200, 64560, 0)
    SetChrPos(0x0, 80, 200, 64560, 180)
    SetChrPos(0x1, 80, 200, 64560, 180)
    SetChrPos(0x2, 80, 200, 64560, 180)
    SetChrPos(0x3, 80, 200, 64560, 180)
    EventEnd(0x0)
    Return()

    # Function_19_1AF0 end

    def Function_20_1BEB(): pass

    label("Function_20_1BEB")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, -500, 200, 67000, 0)
    SetChrPos(0x102, 500, 200, 67000, 0)
    SetChrPos(0xF8, -500, 200, 66000, 0)
    SetChrPos(0xF9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    NewScene("ED6_DT21/C2302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_1BEB end

    def Function_21_1C63(): pass

    label("Function_21_1C63")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_21_1C63 end

    def Function_22_1D56(): pass

    label("Function_22_1D56")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_22_1D56 end

    def Function_23_1E49(): pass

    label("Function_23_1E49")


    def lambda_1E4F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E4F)

    def lambda_1E61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1E61)

    def lambda_1E73():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1E73)

    def lambda_1E85():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1E85)
    Sleep(2500)
    Return()

    # Function_23_1E49 end

    def Function_24_1E97(): pass

    label("Function_24_1E97")


    def lambda_1E9D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E9D)

    def lambda_1EAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1EAF)

    def lambda_1EC1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1EC1)

    def lambda_1ED3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1ED3)
    Sleep(2000)
    Return()

    # Function_24_1E97 end

    SaveToFile()

Try(main)
