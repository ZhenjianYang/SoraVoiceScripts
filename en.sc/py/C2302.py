from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Guardian',                             # 10
        'Guardian',                             # 11
        'Guardian',                             # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        "Function_2_5AB",          # 02, 2
        "Function_3_5C1",          # 03, 3
        "Function_4_7CD",          # 04, 4
        "Function_5_8EE",          # 05, 5
        "Function_6_A1B",          # 06, 6
        "Function_7_B43",          # 07, 7
        "Function_8_CA5",          # 08, 8
        "Function_9_1712",         # 09, 9
        "Function_10_1EC1",        # 0A, 10
        "Function_11_1F47",        # 0B, 11
        "Function_12_1FD4",        # 0C, 12
        "Function_13_20E1",        # 0D, 13
        "Function_14_2162",        # 0E, 14
        "Function_15_225D",        # 0F, 15
        "Function_16_22D5",        # 10, 16
        "Function_17_23B4",        # 11, 17
        "Function_18_2493",        # 12, 18
        "Function_19_24E1",        # 13, 19
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

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 3)), scpexpr(EXPR_END)), "loc_44A")
    SetChrFlags(0xC, 0x80)

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 4)), scpexpr(EXPR_END)), "loc_456")
    SetChrFlags(0xD, 0x80)

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 5)), scpexpr(EXPR_END)), "loc_462")
    SetChrFlags(0xE, 0x80)

    label("loc_462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 6)), scpexpr(EXPR_END)), "loc_46E")
    SetChrFlags(0xF, 0x80)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 7)), scpexpr(EXPR_END)), "loc_47A")
    SetChrFlags(0x10, 0x80)

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 0)), scpexpr(EXPR_END)), "loc_486")
    SetChrFlags(0x11, 0x80)

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 4)), scpexpr(EXPR_END)), "loc_518")
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
    Jump("loc_5A0")

    label("loc_518")

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

    label("loc_5A0")

    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xF)
    Return()

    # Function_1_399 end

    def Function_2_5AB(): pass

    label("Function_2_5AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5AB")

    label("loc_5C0")

    Return()

    # Function_2_5AB end

    def Function_3_5C1(): pass

    label("Function_3_5C1")

    OP_EA(0x2, 0xB, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_618():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_618)

    def lambda_633():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_633)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x408, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_686"),
        (2, "loc_698"),
        (1, "loc_6A8"),
        (SWITCH_DEFAULT, "loc_6AB"),
    )


    label("loc_686")

    OP_A2(0x1F77)
    OP_6F(0x8, 60)
    Sleep(500)
    Jump("loc_6AB")

    label("loc_698")

    OP_6F(0x8, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_6A8")

    OP_B4(0x0)
    Return()

    label("loc_6AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E, 1)"), scpexpr(EXPR_END)), "loc_6F7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x2E\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F76)
    Jump("loc_759")

    label("loc_6F7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x2E\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x2E\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_759")

    Jump("loc_7BF")

    label("loc_75C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05Whatever riches once lay in this chest,\x01",
            "it's just an empty vessel now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5C1 end

    def Function_4_7CD(): pass

    label("Function_4_7CD")

    OP_EA(0x2, 0x94, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_83E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F78)
    Jump("loc_8A2")

    label("loc_83E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_8A2")

    Jump("loc_8E0")

    label("loc_8A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Mnhh... Five more minutes...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8E0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7CD end

    def Function_5_8EE(): pass

    label("Function_5_8EE")

    OP_EA(0x2, 0x95, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_95F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F79)
    Jump("loc_9C3")

    label("loc_95F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_9C3")

    Jump("loc_A0D")

    label("loc_9C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05This chest seems happy to see you again.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A0D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8EE end

    def Function_6_A1B(): pass

    label("Function_6_A1B")

    OP_EA(0x2, 0x96, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE4")
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
            "Found\x01",
            "#2C#57IWater Sepith x300\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F7A)
    Jump("loc_B31")

    label("loc_AE4")


    AnonymousTalk(    #11
        (
            "\x07\x05This chest is out of service.\x01",
            "Please come back during business hours.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B31")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A1B end

    def Function_7_B43(): pass

    label("Function_7_B43")

    OP_EA(0x2, 0x97, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_BB4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F7B)
    Jump("loc_C18")

    label("loc_BB4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_C18")

    Jump("loc_C97")

    label("loc_C1B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05As you open the empty chest, it creaks loudly,\x01",
            "probably cursing you out in its native tongue.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C97")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B43 end

    def Function_8_CA5(): pass

    label("Function_8_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 7)), scpexpr(EXPR_END)), "loc_CAD")
    Return()

    label("loc_CAD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD2")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_CD2")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B1")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDF")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E1D")

    label("loc_DDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E06")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E1D")

    label("loc_E06")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E1D")

    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1020F#6PMore of them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        "#024F#6PHere they come!\x02",
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

    def lambda_F05():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F05)

    def lambda_F17():
        OP_8F(0xFE, 0xB4, 0x1F4, 0x91AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F17)

    def lambda_F32():
        OP_6D(-180, 400, 32420, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F32)

    def lambda_F4A():
        OP_6B(2490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F4A)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_F64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F64)

    def lambda_F76():
        OP_8F(0xFE, 0xFFFFECA0, 0x1F4, 0x8AE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F76)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_F9B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F9B)

    def lambda_FAD():
        OP_8F(0xFE, 0x12E8, 0x1F4, 0x89BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FAD)
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
        (5, "loc_1025"),
        (4, "loc_102D"),
        (6, "loc_1035"),
        (7, "loc_103D"),
        (8, "loc_1045"),
        (SWITCH_DEFAULT, "loc_104D"),
    )


    label("loc_1025")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_104D")

    label("loc_102D")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_104D")

    label("loc_1035")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_104D")

    label("loc_103D")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_104D")

    label("loc_1045")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_104D")

    label("loc_104D")

    OP_0D()
    Sleep(500)

    def lambda_1059():
        OP_6D(100, 400, 29000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1059)

    def lambda_1071():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1071)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_108B():
        OP_8F(0xFE, 0xFFFFFB8C, 0x190, 0x79AE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_108B)

    def lambda_10A6():
        OP_8F(0xFE, 0x9A6, 0x190, 0x7BD4, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10A6)
    Sleep(50)
    SetChrChipByIndex(0x9, 11)

    def lambda_10CB():
        OP_8F(0xFE, 0x1E0, 0x190, 0x7A58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10CB)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x40A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1112"),
        (2, "loc_11E5"),
        (1, "loc_12A9"),
        (SWITCH_DEFAULT, "loc_12AE"),
    )


    label("loc_1112")

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
    Jump("loc_12AE")

    label("loc_11E5")

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
    Jump("loc_12AE")

    label("loc_12A9")

    OP_B4(0x0)
    Jump("loc_12AE")

    label("loc_12AE")

    Jump("loc_170E")

    label("loc_12B1")

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

    def lambda_1365():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1365)

    def lambda_1377():
        OP_8F(0xFE, 0xB4, 0x1F4, 0x91AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1377)

    def lambda_1392():
        OP_6D(-180, 400, 32420, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1392)

    def lambda_13AA():
        OP_6B(2490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AA)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_13C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13C4)

    def lambda_13D6():
        OP_8F(0xFE, 0xFFFFECA0, 0x1F4, 0x8AE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_13D6)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_13FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13FB)

    def lambda_140D():
        OP_8F(0xFE, 0x12E8, 0x1F4, 0x89BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_140D)
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
        (5, "loc_1485"),
        (4, "loc_148D"),
        (6, "loc_1495"),
        (7, "loc_149D"),
        (8, "loc_14A5"),
        (SWITCH_DEFAULT, "loc_14AD"),
    )


    label("loc_1485")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_14AD")

    label("loc_148D")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_14AD")

    label("loc_1495")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_14AD")

    label("loc_149D")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_14AD")

    label("loc_14A5")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_14AD")

    label("loc_14AD")

    OP_0D()
    Sleep(500)

    def lambda_14B9():
        OP_6D(100, 400, 29000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14B9)

    def lambda_14D1():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D1)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_14EB():
        OP_8F(0xFE, 0xFFFFFB8C, 0x190, 0x79AE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14EB)

    def lambda_1506():
        OP_8F(0xFE, 0x9A6, 0x190, 0x7BD4, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1506)
    Sleep(50)
    SetChrChipByIndex(0x9, 11)

    def lambda_152B():
        OP_8F(0xFE, 0x1E0, 0x190, 0x7A58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_152B)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x40A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1572"),
        (2, "loc_1645"),
        (1, "loc_1709"),
        (SWITCH_DEFAULT, "loc_170E"),
    )


    label("loc_1572")

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
    Jump("loc_170E")

    label("loc_1645")

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
    Jump("loc_170E")

    label("loc_1709")

    OP_B4(0x0)
    Jump("loc_170E")

    label("loc_170E")

    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_8_CA5 end

    def Function_9_1712(): pass

    label("Function_9_1712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB7")
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
            "\x07\x05#1S[About the Aureole's Seal 2/4]\x01",
            "The ■■■■ol ■, ha ■■ng ■ea■■■d ■■ ■■■ ■lan, too■ to\x01",
            "fo■■e. The Aureole m■n■■es■■d ■■■■■ies as i■■\x01",
            "defend■■■, and ■et t■■m ■■■■ ■■ in ■h■ ■ac■■■ty.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #18
        (
            "\x07\x05#1S■■■eve■, we w■■e saved ■y our ■■■i■■■n to ■■■■■\x01",
            "the f■■■l■■■ ■n■■■gro■■d. Jus■ on■ si■■le ■h■■nel\x01",
            "co■■ecte■ the ■■■■■■ to the sur■■c■. The\x01",
            "Rev■■■es' ■■■ack■ cou■d not ■■■ch ■o■n ■■0 ar■e\x01",
            "■en■■■h the surface.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #19
        (
            "\x07\x05#1STh■ ■■■ac■s by the ■■■■■■■ ■■■■ on ■■■ o■, day\x01",
            "and ■■■h■ w■■■out ■■us■. Ev■■■ua■■■ our d■■■n■ive\x01",
            "■■■■ bega■ ■■ r■■■h it■ l■mi■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #20
        "\x07\x00Received #1030i.\x02",
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
    Jump("loc_1EBD")

    label("loc_1BB7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #21
        (
            "\x07\x05#1S[About the Aureole's Seal 2/4]\x01",
            "The ■■■■ol ■, ha ■■ng ■ea■■■d ■■ ■■■ ■lan, too■ to\x01",
            "fo■■e. The Aureole m■n■■es■■d ■■■■■ies as i■■\x01",
            "defend■■■, and ■et t■■m ■■■■ ■■ in ■h■ ■ac■■■ty.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #22
        (
            "\x07\x05#1S■■■eve■, we w■■e saved ■y our ■■■i■■■n to ■■■■■\x01",
            "the f■■■l■■■ ■n■■■gro■■d. Jus■ on■ si■■le ■h■■nel\x01",
            "co■■ecte■ the ■■■■■■ to the sur■■c■. The\x01",
            "Rev■■■es' ■■■ack■ cou■d not ■■■ch ■o■n ■■0 ar■e\x01",
            "■en■■■h the surface.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #23
        (
            "\x07\x05#1STh■ ■■■ac■s by the ■■■■■■■ ■■■■ on ■■■ o■, day\x01",
            "and ■■■h■ w■■■out ■■us■. Ev■■■ua■■■ our d■■■n■ive\x01",
            "■■■■ bega■ ■■ r■■■h it■ l■mi■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1EBD")

    TalkEnd(0xFF)
    Return()

    # Function_9_1712 end

    def Function_10_1EC1(): pass

    label("Function_10_1EC1")

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
        (0, "loc_1F3A"),
        (1, "loc_1F40"),
        (SWITCH_DEFAULT, "loc_1F46"),
    )


    label("loc_1F3A")

    OP_A2(0x1200)
    Jump("loc_1F46")

    label("loc_1F40")

    OP_A2(0x1201)
    Jump("loc_1F46")

    label("loc_1F46")

    Return()

    # Function_10_1EC1 end

    def Function_11_1F47(): pass

    label("Function_11_1F47")

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

    # Function_11_1F47 end

    def Function_12_1FD4(): pass

    label("Function_12_1FD4")

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

    # Function_12_1FD4 end

    def Function_13_20E1(): pass

    label("Function_13_20E1")

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

    # Function_13_20E1 end

    def Function_14_2162(): pass

    label("Function_14_2162")

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

    # Function_14_2162 end

    def Function_15_225D(): pass

    label("Function_15_225D")

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

    # Function_15_225D end

    def Function_16_22D5(): pass

    label("Function_16_22D5")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_16_22D5 end

    def Function_17_23B4(): pass

    label("Function_17_23B4")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_17_23B4 end

    def Function_18_2493(): pass

    label("Function_18_2493")


    def lambda_2499():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2499)

    def lambda_24AB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_24AB)

    def lambda_24BD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_24BD)

    def lambda_24CF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_24CF)
    Sleep(2500)
    Return()

    # Function_18_2493 end

    def Function_19_24E1(): pass

    label("Function_19_24E1")


    def lambda_24E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_24E7)

    def lambda_24F9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_24F9)

    def lambda_250B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_250B)

    def lambda_251D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_251D)
    Sleep(2000)
    Return()

    # Function_19_24E1 end

    SaveToFile()

Try(main)
