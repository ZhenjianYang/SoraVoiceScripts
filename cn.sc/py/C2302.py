from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2302   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2302.x',
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
        '守护者',                               # 10
        '守护者',                               # 11
        '守护者',                               # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        X                   = 20,
        Z                   = 1000,
        Y                   = -40050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5500,
        Z                   = 400,
        Y                   = -45890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7843,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5600,
        Z                   = 400,
        Y                   = -45590,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7844,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5440,
        Z                   = 400,
        Y                   = -34850,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7845,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5500,
        Z                   = 400,
        Y                   = -35460,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7846,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = -6170,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7847,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = 7630,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7848,
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
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = -40000,
        TriggerRange        = 1000,
        ActorX              = 20,
        ActorZ              = 0,
        ActorY              = -40050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
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
        TriggerX            = 5470,
        TriggerZ            = 400,
        TriggerY            = -9530,
        TriggerRange        = 1000,
        ActorX              = 6030,
        ActorZ              = 400,
        ActorY              = -10090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
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
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_399",          # 01, 1
        "Function_2_583",          # 02, 2
        "Function_3_599",          # 03, 3
        "Function_4_769",          # 04, 4
        "Function_5_880",          # 05, 5
        "Function_6_997",          # 06, 6
        "Function_7_A93",          # 07, 7
        "Function_8_BAA",          # 08, 8
        "Function_9_160F",         # 09, 9
        "Function_10_1B0B",        # 0A, 10
        "Function_11_1B92",        # 0B, 11
        "Function_12_1C1F",        # 0C, 12
        "Function_13_1D2C",        # 0D, 13
        "Function_14_1DAD",        # 0E, 14
        "Function_15_1EA8",        # 0F, 15
        "Function_16_1F20",        # 10, 16
        "Function_17_2013",        # 11, 17
        "Function_18_2106",        # 12, 18
        "Function_19_2154",        # 13, 19
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_38A"),
        (101, "loc_391"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_38A")

    Event(0, 12)
    Jump("loc_398")

    label("loc_391")

    Event(0, 14)
    Jump("loc_398")

    label("loc_398")

    Return()

    # Function_0_37A end

    def Function_1_399(): pass

    label("Function_1_399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB")
    OP_6F(0x8, 0)
    Jump("loc_3B2")

    label("loc_3AB")

    OP_6F(0x8, 60)

    label("loc_3B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4")
    OP_6F(0x9, 0)
    Jump("loc_3CB")

    label("loc_3C4")

    OP_6F(0x9, 60)

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD")
    OP_6F(0xA, 0)
    Jump("loc_3E4")

    label("loc_3DD")

    OP_6F(0xA, 60)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    OP_6F(0xB, 0)
    Jump("loc_3FD")

    label("loc_3F6")

    OP_6F(0xB, 60)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F")
    OP_6F(0xC, 0)
    Jump("loc_416")

    label("loc_40F")

    OP_6F(0xC, 60)

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 3)), scpexpr(EXPR_END)), "loc_422")
    SetChrFlags(0xC, 0x80)

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 4)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0xD, 0x80)

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 5)), scpexpr(EXPR_END)), "loc_43A")
    SetChrFlags(0xE, 0x80)

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 6)), scpexpr(EXPR_END)), "loc_446")
    SetChrFlags(0xF, 0x80)

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 7)), scpexpr(EXPR_END)), "loc_452")
    SetChrFlags(0x10, 0x80)

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 0)), scpexpr(EXPR_END)), "loc_45E")
    SetChrFlags(0x11, 0x80)

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 4)), scpexpr(EXPR_END)), "loc_4F0")
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
    Jump("loc_578")

    label("loc_4F0")

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

    label("loc_578")

    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xF)
    Return()

    # Function_1_399 end

    def Function_2_583(): pass

    label("Function_2_583")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_598")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_583")

    label("loc_598")

    Return()

    # Function_2_583 end

    def Function_3_599(): pass

    label("Function_3_599")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_5EB():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5EB)

    def lambda_606():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_606)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x408, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_653"),
        (2, "loc_665"),
        (1, "loc_675"),
        (SWITCH_DEFAULT, "loc_678"),
    )


    label("loc_653")

    OP_A2(0x1F77)
    OP_6F(0x8, 60)
    Sleep(500)
    Jump("loc_678")

    label("loc_665")

    OP_6F(0x8, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_675")

    OP_B4(0x0)
    Return()

    label("loc_678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E, 1)"), scpexpr(EXPR_END)), "loc_6C7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x2E\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F76)
    Jump("loc_729")

    label("loc_6C7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x2E\x00\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x2E\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_729")

    Jump("loc_75B")

    label("loc_72C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_75B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_599 end

    def Function_4_769(): pass

    label("Function_4_769")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_841")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_7D8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F78)
    Jump("loc_83E")

    label("loc_7D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_83E")

    Jump("loc_872")

    label("loc_841")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_872")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_769 end

    def Function_5_880(): pass

    label("Function_5_880")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_958")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_8EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F79)
    Jump("loc_955")

    label("loc_8EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_955")

    Jump("loc_989")

    label("loc_958")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_989")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_880 end

    def Function_6_997(): pass

    label("Function_6_997")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A67")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    OP_6F(0xB, 30)
    AddSepith(0x1, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
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
    OP_A2(0x1F7A)
    Jump("loc_A81")

    label("loc_A67")


    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A81")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_997 end

    def Function_7_A93(): pass

    label("Function_7_A93")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_B02")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F7B)
    Jump("loc_B68")

    label("loc_B02")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_B68")

    Jump("loc_B9C")

    label("loc_B6B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A93 end

    def Function_8_BAA(): pass

    label("Function_8_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 7)), scpexpr(EXPR_END)), "loc_BB2")
    Return()

    label("loc_BB2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD7")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_BD7")

    Fade(1000)
    OP_6D(-130, 400, 28900, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(219000, 0)
    OP_6E(404, 0)
    SetChrPos(0x101, 900, 400, 29590, 0)
    SetChrPos(0x102, -620, 400, 29500, 0)
    SetChrPos(0x103, 1050, 400, 28150, 0)
    SetChrPos(0xF9, -780, 400, 28040, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AE")
    OP_A2(0x1E16)
    OP_22(0x118, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE4")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D22")

    label("loc_CE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D22")

    label("loc_D0B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D22")

    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1020F#5P又是了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        "#024F#5P……来了！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 180, 2500, 37290, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -4960, 2500, 35560, 135)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 4840, 2500, 35260, 225)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 8)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)

    def lambda_E02():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E02)

    def lambda_E14():
        OP_8F(0xFE, 0xB4, 0x1F4, 0x91AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E14)

    def lambda_E2F():
        OP_6D(-180, 400, 32420, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E2F)

    def lambda_E47():
        OP_6B(2490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E47)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_E61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E61)

    def lambda_E73():
        OP_8F(0xFE, 0xFFFFECA0, 0x1F4, 0x8AE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E73)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_E98():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E98)

    def lambda_EAA():
        OP_8F(0xFE, 0x12E8, 0x1F4, 0x89BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EAA)
    Sleep(300)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xB, 0x2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 15)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x103, 16)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_F22"),
        (4, "loc_F2A"),
        (6, "loc_F32"),
        (7, "loc_F3A"),
        (8, "loc_F42"),
        (SWITCH_DEFAULT, "loc_F4A"),
    )


    label("loc_F22")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_F4A")

    label("loc_F2A")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_F4A")

    label("loc_F32")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_F4A")

    label("loc_F3A")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_F4A")

    label("loc_F42")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_F4A")

    label("loc_F4A")

    OP_0D()
    Sleep(500)

    def lambda_F56():
        OP_6D(100, 400, 29000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F56)

    def lambda_F6E():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6E)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_F88():
        OP_8F(0xFE, 0xFFFFFB8C, 0x190, 0x79AE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F88)

    def lambda_FA3():
        OP_8F(0xFE, 0x9A6, 0x190, 0x7BD4, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FA3)
    Sleep(50)
    SetChrChipByIndex(0x9, 11)

    def lambda_FC8():
        OP_8F(0xFE, 0x1E0, 0x190, 0x7A58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FC8)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x40A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_100F"),
        (2, "loc_10E2"),
        (1, "loc_11A6"),
        (SWITCH_DEFAULT, "loc_11AB"),
    )


    label("loc_100F")

    EventBegin(0x0)
    OP_44(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_44(0xA, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_44(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
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
    OP_A2(0x1E17)
    Jump("loc_11AB")

    label("loc_10E2")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6D(190, 400, 25640, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 400, 25640, 0)
    SetChrPos(0x1, 0, 400, 25640, 0)
    SetChrPos(0x2, 0, 400, 25640, 0)
    SetChrPos(0x3, 0, 400, 25640, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Jump("loc_11AB")

    label("loc_11A6")

    OP_B4(0x0)
    Jump("loc_11AB")

    label("loc_11AB")

    Jump("loc_160B")

    label("loc_11AE")

    OP_22(0x118, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 180, 2500, 37290, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -4960, 2500, 35560, 135)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 4840, 2500, 35260, 225)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 8)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)

    def lambda_1262():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1262)

    def lambda_1274():
        OP_8F(0xFE, 0xB4, 0x1F4, 0x91AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1274)

    def lambda_128F():
        OP_6D(-180, 400, 32420, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_128F)

    def lambda_12A7():
        OP_6B(2490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A7)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_12C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12C1)

    def lambda_12D3():
        OP_8F(0xFE, 0xFFFFECA0, 0x1F4, 0x8AE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12D3)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_12F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12F8)

    def lambda_130A():
        OP_8F(0xFE, 0x12E8, 0x1F4, 0x89BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_130A)
    Sleep(300)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xB, 0x2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 15)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x103, 16)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_1382"),
        (4, "loc_138A"),
        (6, "loc_1392"),
        (7, "loc_139A"),
        (8, "loc_13A2"),
        (SWITCH_DEFAULT, "loc_13AA"),
    )


    label("loc_1382")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_13AA")

    label("loc_138A")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_13AA")

    label("loc_1392")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_13AA")

    label("loc_139A")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_13AA")

    label("loc_13A2")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_13AA")

    label("loc_13AA")

    OP_0D()
    Sleep(500)

    def lambda_13B6():
        OP_6D(100, 400, 29000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13B6)

    def lambda_13CE():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CE)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_13E8():
        OP_8F(0xFE, 0xFFFFFB8C, 0x190, 0x79AE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_13E8)

    def lambda_1403():
        OP_8F(0xFE, 0x9A6, 0x190, 0x7BD4, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1403)
    Sleep(50)
    SetChrChipByIndex(0x9, 11)

    def lambda_1428():
        OP_8F(0xFE, 0x1E0, 0x190, 0x7A58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1428)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x40A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_146F"),
        (2, "loc_1542"),
        (1, "loc_1606"),
        (SWITCH_DEFAULT, "loc_160B"),
    )


    label("loc_146F")

    EventBegin(0x0)
    OP_44(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_44(0xA, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_44(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
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
    OP_A2(0x1E17)
    Jump("loc_160B")

    label("loc_1542")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6D(190, 400, 25640, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 400, 25640, 0)
    SetChrPos(0x1, 0, 400, 25640, 0)
    SetChrPos(0x2, 0, 400, 25640, 0)
    SetChrPos(0x3, 0, 400, 25640, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Jump("loc_160B")

    label("loc_1606")

    OP_B4(0x0)
    Jump("loc_160B")

    label("loc_160B")

    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_8_BAA end

    def Function_9_160F(): pass

    label("Function_9_160F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1959")
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

    AnonymousTalk(    #17
        (
            "\x07\x05#1S『关于‘环’的封印（２／４）』\x01",
            "　\x01",
            "得知■■■划的■环■\x01",
            "■取了■制手段。\x01",
            "　\x01",
            "『■』诞生出■■\x01",
            "■被称为『■想■■』\x01",
            "的自■■护者\x01",
            "向躲在■■中的我们■■\x01",
            "　\x01",
            "──不■，■■的■\x01",
            "设施■建造■■下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #18
        (
            "\x07\x05#1S■■地上设施相连\x01",
            "■■■■■一■。\x01",
            "■■想■■■的攻■\x01",
            "■法■达\x01",
            "■■500■■。\x01",
            "　\x01",
            "■■，■幻想■■■的攻■\x01",
            "却日■不■。\x01",
            "躲在里面■我们\x01",
            "那道坚固■防■线也■近了■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\x06\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x406, 1)
    OP_A2(0x1E1C)
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
    OP_6D(280, 200, 36690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 280, 200, 36690, 0)
    SetChrPos(0x1, 280, 200, 36690, 0)
    SetChrPos(0x2, 280, 200, 36690, 0)
    SetChrPos(0x3, 280, 200, 36690, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_1B07")

    label("loc_1959")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #20
        (
            "\x07\x05#1S『关于‘环’的封印（２／４）』\x01",
            "　\x01",
            "得知■■■划的■环■\x01",
            "■取了■制手段。\x01",
            "　\x01",
            "『■』诞生出■■\x01",
            "■被称为『■想■■』\x01",
            "的自■■护者\x01",
            "向躲在■■中的我们■■\x01",
            "　\x01",
            "──不■，■■的■\x01",
            "设施■建造■■下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x05#1S■■地上设施相连\x01",
            "■■■■■一■。\x01",
            "■■想■■■的攻■\x01",
            "■法■达\x01",
            "■■500■■。\x01",
            "　\x01",
            "■■，■幻想■■■的攻■\x01",
            "却日■不■。\x01",
            "躲在里面■我们\x01",
            "那道坚固■防■线也■近了■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1B07")

    TalkEnd(0xFF)
    Return()

    # Function_9_160F end

    def Function_10_1B0B(): pass

    label("Function_10_1B0B")

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
        (0, "loc_1B85"),
        (1, "loc_1B8B"),
        (SWITCH_DEFAULT, "loc_1B91"),
    )


    label("loc_1B85")

    OP_A2(0x1200)
    Jump("loc_1B91")

    label("loc_1B8B")

    OP_A2(0x1201)
    Jump("loc_1B91")

    label("loc_1B91")

    Return()

    # Function_10_1B0B end

    def Function_11_1B92(): pass

    label("Function_11_1B92")

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

    # Function_11_1B92 end

    def Function_12_1C1F(): pass

    label("Function_12_1C1F")

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
    Call(0, 16)
    Call(0, 18)
    Fade(500)
    OP_6D(-80, 200, -64580, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -80, 200, -64580, 0)
    SetChrPos(0x1, -80, 200, -64580, 0)
    SetChrPos(0x2, -80, 200, -64580, 0)
    SetChrPos(0x3, -80, 200, -64580, 0)
    EventEnd(0x0)
    Return()

    # Function_12_1C1F end

    def Function_13_1D2C(): pass

    label("Function_13_1D2C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 200, -66000, 180)
    SetChrPos(0x102, -500, 200, -66000, 180)
    SetChrPos(0xF8, 500, 200, -67000, 180)
    SetChrPos(0xF9, -500, 200, -67000, 180)
    OP_0D()
    Call(0, 16)
    Call(0, 19)
    NewScene("ED6_DT21/C2301   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1D2C end

    def Function_14_1DAD(): pass

    label("Function_14_1DAD")

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
    Call(0, 17)
    Call(0, 18)
    Fade(500)
    OP_6D(70, 200, 64580, 0)
    SetChrPos(0x0, 70, 200, 64580, 180)
    SetChrPos(0x1, 70, 200, 64580, 180)
    SetChrPos(0x2, 70, 200, 64580, 180)
    SetChrPos(0x3, 70, 200, 64580, 180)
    EventEnd(0x0)
    Return()

    # Function_14_1DAD end

    def Function_15_1EA8(): pass

    label("Function_15_1EA8")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, -500, 200, 67000, 0)
    SetChrPos(0x102, 500, 200, 67000, 0)
    SetChrPos(0xF8, -500, 200, 66000, 0)
    SetChrPos(0xF9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 17)
    Call(0, 19)
    NewScene("ED6_DT21/C2303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1EA8 end

    def Function_16_1F20(): pass

    label("Function_16_1F20")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_16_1F20 end

    def Function_17_2013(): pass

    label("Function_17_2013")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_17_2013 end

    def Function_18_2106(): pass

    label("Function_18_2106")


    def lambda_210C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_210C)

    def lambda_211E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_211E)

    def lambda_2130():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2130)

    def lambda_2142():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2142)
    Sleep(2500)
    Return()

    # Function_18_2106 end

    def Function_19_2154(): pass

    label("Function_19_2154")


    def lambda_215A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_215A)

    def lambda_216C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_216C)

    def lambda_217E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_217E)

    def lambda_2190():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2190)
    Sleep(2000)
    Return()

    # Function_19_2154 end

    SaveToFile()

Try(main)
