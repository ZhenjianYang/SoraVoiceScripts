from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2303   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2303.x',
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
        X                   = 60,
        Z                   = 1000,
        Y                   = 820,
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
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7849,
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
        Unknown_18          = 7850,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5440,
        Z                   = 400,
        Y                   = -34850,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7851,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5500,
        Z                   = 400,
        Y                   = -35460,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7852,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = -6170,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7853,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = 7630,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7854,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -7000,
        Y                   = -1000,
        Z                   = 32000,
        Range               = 7000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x84D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
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
        TriggerX            = 210,
        TriggerZ            = 0,
        TriggerY            = -4860,
        TriggerRange        = 1000,
        ActorX              = 40,
        ActorZ              = 0,
        ActorY              = -4050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140,
        TriggerZ            = 0,
        TriggerY            = 190,
        TriggerRange        = 1000,
        ActorX              = 60,
        ActorZ              = 0,
        ActorY              = 820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 100,
        TriggerZ            = 0,
        TriggerY            = 5280,
        TriggerRange        = 1000,
        ActorX              = 80,
        ActorZ              = 0,
        ActorY              = 5940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
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
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_356",          # 00, 0
        "Function_1_375",          # 01, 1
        "Function_2_590",          # 02, 2
        "Function_3_5A6",          # 03, 3
        "Function_4_6EC",          # 04, 4
        "Function_5_84E",          # 05, 5
        "Function_6_A45",          # 06, 6
        "Function_7_BDA",          # 07, 7
        "Function_8_16BA",         # 08, 8
        "Function_9_1E7A",         # 09, 9
        "Function_10_1F00",        # 0A, 10
        "Function_11_1F8D",        # 0B, 11
        "Function_12_209A",        # 0C, 12
        "Function_13_211B",        # 0D, 13
        "Function_14_2216",        # 0E, 14
        "Function_15_228E",        # 0F, 15
        "Function_16_236D",        # 10, 16
        "Function_17_244C",        # 11, 17
        "Function_18_249A",        # 12, 18
    )


    def Function_0_356(): pass

    label("Function_0_356")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_366"),
        (101, "loc_36D"),
        (SWITCH_DEFAULT, "loc_374"),
    )


    label("loc_366")

    Event(0, 11)
    Jump("loc_374")

    label("loc_36D")

    Event(0, 13)
    Jump("loc_374")

    label("loc_374")

    Return()

    # Function_0_356 end

    def Function_1_375(): pass

    label("Function_1_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387")
    OP_6F(0x9, 0)
    Jump("loc_38E")

    label("loc_387")

    OP_6F(0x9, 60)

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0")
    OP_6F(0xA, 0)
    Jump("loc_3A7")

    label("loc_3A0")

    OP_6F(0xA, 60)

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    OP_6F(0xB, 0)
    Jump("loc_3C0")

    label("loc_3B9")

    OP_6F(0xB, 60)

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2")
    OP_6F(0xC, 0)
    Jump("loc_3D9")

    label("loc_3D2")

    OP_6F(0xC, 60)

    label("loc_3D9")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 1)), scpexpr(EXPR_END)), "loc_40D")
    SetChrFlags(0xC, 0x80)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 2)), scpexpr(EXPR_END)), "loc_419")
    SetChrFlags(0xD, 0x80)

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 3)), scpexpr(EXPR_END)), "loc_425")
    SetChrFlags(0xE, 0x80)

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 4)), scpexpr(EXPR_END)), "loc_431")
    SetChrFlags(0xF, 0x80)

    label("loc_431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 5)), scpexpr(EXPR_END)), "loc_43D")
    SetChrFlags(0x10, 0x80)

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D5, 6)), scpexpr(EXPR_END)), "loc_449")
    SetChrFlags(0x11, 0x80)

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 1)), scpexpr(EXPR_END)), "loc_4EC")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x8, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    Jump("loc_585")

    label("loc_4EC")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x8, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)

    label("loc_585")

    OP_1B(0x0, 0x0, 0xC)
    OP_1B(0x1, 0x0, 0xE)
    Return()

    # Function_1_375 end

    def Function_2_590(): pass

    label("Function_2_590")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_590")

    label("loc_5A5")

    Return()

    # Function_2_590 end

    def Function_3_5A6(): pass

    label("Function_3_5A6")

    OP_EA(0x2, 0x98, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4E, 1)"), scpexpr(EXPR_END)), "loc_617")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x4E\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F7C)
    Jump("loc_67B")

    label("loc_617")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x4E\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x4E\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_67B")

    Jump("loc_6DE")

    label("loc_67E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Back for seconds? Have you even used what you\x01",
            "got the first time?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6DE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5A6 end

    def Function_4_6EC(): pass

    label("Function_4_6EC")

    OP_EA(0x2, 0x99, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_75D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F7E)
    Jump("loc_7C1")

    label("loc_75D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_7C1")

    Jump("loc_840")

    label("loc_7C4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Take, take, take, that's all you ever do!\x01",
            "Why not try giving BACK to an empty chest\x01",
            "sometime?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_840")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6EC end

    def Function_5_84E(): pass

    label("Function_5_84E")

    OP_EA(0x2, 0x9A, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_938")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_8A5():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8A5)

    def lambda_8C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8C0)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #6
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x408, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_913"),
        (2, "loc_925"),
        (1, "loc_935"),
        (SWITCH_DEFAULT, "loc_938"),
    )


    label("loc_913")

    OP_A2(0x1F80)
    OP_6F(0xB, 60)
    Sleep(500)
    Jump("loc_938")

    label("loc_925")

    OP_6F(0xB, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_935")

    OP_B4(0x0)
    Return()

    label("loc_938")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_984")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "Found \x1F\x6E\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F7F)
    Jump("loc_9E6")

    label("loc_984")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        (
            "Found \x1F\x6E\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6E\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_9E6")

    Jump("loc_A37")

    label("loc_9E9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05At this point, you need to think outside the box.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A37")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_84E end

    def Function_6_A45(): pass

    label("Function_6_A45")

    OP_EA(0x2, 0x9B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_AB6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F81)
    Jump("loc_B1A")

    label("loc_AB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_B1A")

    Jump("loc_BCC")

    label("loc_B1D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05The chest was more than excited to speak with\x01",
            "you. It watched in stunned silence as you simply\x01",
            "opened its lid, shook your head, and walked away.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BCC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A45 end

    def Function_7_BDA(): pass

    label("Function_7_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 1)), scpexpr(EXPR_END)), "loc_BE2")
    Return()

    label("loc_BE2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C07")
    Call(0, 9)
    Call(0, 10)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_C07")

    Fade(1000)
    OP_6D(60, 400, 34140, 0)
    OP_67(0, 6390, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(134000, 0)
    OP_6E(383, 0)
    SetChrPos(0x101, 540, 400, 35020, 0)
    SetChrPos(0x102, -980, 400, 35070, 0)
    SetChrPos(0x103, 580, 400, 33530, 0)
    SetChrPos(0xF9, -1190, 400, 33740, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1223")
    OP_A2(0x1E18)
    OP_22(0x118, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D14")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D52")

    label("loc_D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D52")

    label("loc_D3B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D52")

    Sleep(1000)

    ChrTalk(    #13
        0x102,
        "#1042F#4PHere they come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "#024F#6PLet's clean them up!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, -240, 2500, 27760, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 3930, 2500, 38750, 225)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -4940, 2500, 38780, 135)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 8)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)

    def lambda_E41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E41)

    def lambda_E53():
        OP_8F(0xFE, 0xFFFFFF10, 0x1F4, 0x6C70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E53)

    def lambda_E6E():
        OP_6D(160, 400, 34890, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E6E)

    def lambda_E86():
        OP_6B(2390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E86)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_EA0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EA0)

    def lambda_EB2():
        OP_8F(0xFE, 0xF5A, 0x1F4, 0x975E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EB2)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_ED7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_ED7)

    def lambda_EE9():
        OP_8F(0xFE, 0xFFFFECB4, 0x1F4, 0x977C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EE9)
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
        (5, "loc_F61"),
        (4, "loc_F69"),
        (6, "loc_F71"),
        (7, "loc_F79"),
        (8, "loc_F81"),
        (SWITCH_DEFAULT, "loc_F89"),
    )


    label("loc_F61")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_F89")

    label("loc_F69")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_F89")

    label("loc_F71")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_F89")

    label("loc_F79")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_F89")

    label("loc_F81")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_F89")

    label("loc_F89")


    def lambda_F8F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F8F)

    def lambda_F9D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F9D)
    Sleep(100)

    def lambda_FB0():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB0)
    OP_8C(0x102, 315, 400)
    OP_0D()
    Sleep(500)

    def lambda_FCB():
        OP_6D(470, 400, 33920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FCB)

    def lambda_FE3():
        OP_6B(1750, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE3)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_FFD():
        OP_8F(0xFE, 0x578, 0x190, 0x8B9C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FFD)

    def lambda_1018():
        OP_8F(0xFE, 0xFFFFF827, 0x190, 0x8C50, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1018)
    Sleep(50)
    SetChrChipByIndex(0x9, 11)

    def lambda_103D():
        OP_8F(0xFE, 0xFFFFFEDE, 0x190, 0x7F58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_103D)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x40B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1084"),
        (2, "loc_1157"),
        (1, "loc_121B"),
        (SWITCH_DEFAULT, "loc_1220"),
    )


    label("loc_1084")

    EventBegin(0x0)
    OP_44(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_44(0xA, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_44(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    OP_6D(320, 400, 33530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 320, 400, 33530, 0)
    SetChrPos(0x1, 320, 400, 33530, 0)
    SetChrPos(0x2, 320, 400, 33530, 0)
    SetChrPos(0x3, 320, 400, 33530, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x1E19)
    Jump("loc_1220")

    label("loc_1157")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6D(340, 400, 25660, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 340, 400, 25660, 0)
    SetChrPos(0x1, 340, 400, 25660, 0)
    SetChrPos(0x2, 340, 400, 25660, 0)
    SetChrPos(0x3, 340, 400, 25660, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Jump("loc_1220")

    label("loc_121B")

    OP_B4(0x0)
    Jump("loc_1220")

    label("loc_1220")

    Jump("loc_16B6")

    label("loc_1223")

    OP_22(0x118, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, -240, 2500, 27760, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 3930, 2500, 38750, 225)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -4940, 2500, 38780, 135)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 8)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)

    def lambda_12D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12D7)

    def lambda_12E9():
        OP_8F(0xFE, 0xFFFFFF10, 0x1F4, 0x6C70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12E9)

    def lambda_1304():
        OP_6D(160, 400, 34890, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1304)

    def lambda_131C():
        OP_6B(2390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_131C)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1336():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1336)

    def lambda_1348():
        OP_8F(0xFE, 0xF5A, 0x1F4, 0x975E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1348)
    Sleep(100)
    OP_22(0x99, 0x0, 0x64)

    def lambda_136D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_136D)

    def lambda_137F():
        OP_8F(0xFE, 0xFFFFECB4, 0x1F4, 0x977C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_137F)
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
        (5, "loc_13F7"),
        (4, "loc_13FF"),
        (6, "loc_1407"),
        (7, "loc_140F"),
        (8, "loc_1417"),
        (SWITCH_DEFAULT, "loc_141F"),
    )


    label("loc_13F7")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_141F")

    label("loc_13FF")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_141F")

    label("loc_1407")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_141F")

    label("loc_140F")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_141F")

    label("loc_1417")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_141F")

    label("loc_141F")


    def lambda_1425():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1425)

    def lambda_1433():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1433)
    Sleep(100)

    def lambda_1446():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1446)
    OP_8C(0x102, 315, 400)
    OP_0D()
    Sleep(500)

    def lambda_1461():
        OP_6D(470, 400, 33920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1461)

    def lambda_1479():
        OP_6B(1750, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1479)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_1493():
        OP_8F(0xFE, 0x578, 0x190, 0x8B9C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1493)

    def lambda_14AE():
        OP_8F(0xFE, 0xFFFFF827, 0x190, 0x8C50, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_14AE)
    Sleep(50)
    SetChrChipByIndex(0x9, 11)

    def lambda_14D3():
        OP_8F(0xFE, 0xFFFFFEDE, 0x190, 0x7F58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14D3)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x40B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_151A"),
        (2, "loc_15ED"),
        (1, "loc_16B1"),
        (SWITCH_DEFAULT, "loc_16B6"),
    )


    label("loc_151A")

    EventBegin(0x0)
    OP_44(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_44(0xA, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_44(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    OP_6D(320, 400, 33530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 320, 400, 33530, 0)
    SetChrPos(0x1, 320, 400, 33530, 0)
    SetChrPos(0x2, 320, 400, 33530, 0)
    SetChrPos(0x3, 320, 400, 33530, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x1E19)
    Jump("loc_16B6")

    label("loc_15ED")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6D(340, 400, 25660, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 340, 400, 25660, 0)
    SetChrPos(0x1, 340, 400, 25660, 0)
    SetChrPos(0x2, 340, 400, 25660, 0)
    SetChrPos(0x3, 340, 400, 25660, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0xF9, 0)
    Jump("loc_16B6")

    label("loc_16B1")

    OP_B4(0x0)
    Jump("loc_16B6")

    label("loc_16B6")

    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_7_BDA end

    def Function_8_16BA(): pass

    label("Function_8_16BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B73")
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

    AnonymousTalk(    #15
        (
            "\x07\x05#1S[About the Aureole's Seal 3/4]\x01",
            "Wh■■■ un■er ■■■ac■ by ■■■ Re■■ri■■ we ■■■■ ■■■e\x01",
            "to ■■ni■h the ■■■■■■, b■■ it t■■k ■■m■ to\x01",
            "secure t■■ ne■e■■ar■ ■■■rgy. ■■■ing the pr■cess\x01",
            "■■ s■■■s we ■■■ c■■el■■■, and a ■■■gle ■■■■■■\x01",
            "bro■■ into ■he ■■■il■■y pr■■er.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #16
        (
            "\x07\x05#1S■■ce ■■side, sto■■■ng it was ■i■■■■ult. The\x01",
            "R■■■■■ie r■■ched the ■■■■■■■ se■■i■ns in ■■\x01",
            "in■■■nt. We we■■ ■■st a ■ai■'s bread■■ f■■m total\x01",
            "■■■aster ■■■n the f■■l powe■ for the s■■■ing\x01",
            "■■■■ation wa■ fina■■y ■athered. Just ■■ the\x01",
            "Re■■■ie set ■pon ■■, we act■■■■ed the ■irst\x01",
            "■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #17
        "\x07\x00Received #1031i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x407, 1)
    OP_A2(0x1E21)
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
    Jump("loc_1E76")

    label("loc_1B73")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #18
        (
            "\x07\x05#1S[About the Aureole's Seal 3/4]\x01",
            "Wh■■■ un■er ■■■ac■ by ■■■ Re■■ri■■ we ■■■■ ■■■e\x01",
            "to ■■ni■h the ■■■■■■, b■■ it t■■k ■■m■ to\x01",
            "secure t■■ ne■e■■ar■ ■■■rgy. ■■■ing the pr■cess\x01",
            "■■ s■■■s we ■■■ c■■el■■■, and a ■■■gle ■■■■■■\x01",
            "bro■■ into ■he ■■■il■■y pr■■er.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #19
        (
            "\x07\x05#1S■■ce ■■side, sto■■■ng it was ■i■■■■ult. The\x01",
            "R■■■■■ie r■■ched the ■■■■■■■ se■■i■ns in ■■\x01",
            "in■■■nt. We we■■ ■■st a ■ai■'s bread■■ f■■m total\x01",
            "■■■aster ■■■n the f■■l powe■ for the s■■■ing\x01",
            "■■■■ation wa■ fina■■y ■athered. Just ■■ the\x01",
            "Re■■■ie set ■pon ■■, we act■■■■ed the ■irst\x01",
            "■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E76")

    TalkEnd(0xFF)
    Return()

    # Function_8_16BA end

    def Function_9_1E7A(): pass

    label("Function_9_1E7A")

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
        (0, "loc_1EF3"),
        (1, "loc_1EF9"),
        (SWITCH_DEFAULT, "loc_1EFF"),
    )


    label("loc_1EF3")

    OP_A2(0x1200)
    Jump("loc_1EFF")

    label("loc_1EF9")

    OP_A2(0x1201)
    Jump("loc_1EFF")

    label("loc_1EFF")

    Return()

    # Function_9_1E7A end

    def Function_10_1F00(): pass

    label("Function_10_1F00")

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

    # Function_10_1F00 end

    def Function_11_1F8D(): pass

    label("Function_11_1F8D")

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
    Call(0, 15)
    Call(0, 17)
    Fade(500)
    OP_6D(-70, 200, -64510, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -70, 200, -64510, 0)
    SetChrPos(0x1, -70, 200, -64510, 0)
    SetChrPos(0x2, -70, 200, -64510, 0)
    SetChrPos(0x3, -70, 200, -64510, 0)
    EventEnd(0x0)
    Return()

    # Function_11_1F8D end

    def Function_12_209A(): pass

    label("Function_12_209A")

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
    Call(0, 15)
    Call(0, 18)
    NewScene("ED6_DT21/C2302   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_12_209A end

    def Function_13_211B(): pass

    label("Function_13_211B")

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
    Call(0, 16)
    Call(0, 17)
    Fade(500)
    OP_6D(90, 200, 64590, 0)
    SetChrPos(0x0, 90, 200, 64590, 180)
    SetChrPos(0x1, 90, 200, 64590, 180)
    SetChrPos(0x2, 90, 200, 64590, 180)
    SetChrPos(0x3, 90, 200, 64590, 180)
    EventEnd(0x0)
    Return()

    # Function_13_211B end

    def Function_14_2216(): pass

    label("Function_14_2216")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, -500, 200, 67000, 0)
    SetChrPos(0x102, 500, 200, 67000, 0)
    SetChrPos(0xF8, -500, 200, 66000, 0)
    SetChrPos(0xF9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 16)
    Call(0, 18)
    NewScene("ED6_DT21/C2304   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2216 end

    def Function_15_228E(): pass

    label("Function_15_228E")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_15_228E end

    def Function_16_236D(): pass

    label("Function_16_236D")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_16_236D end

    def Function_17_244C(): pass

    label("Function_17_244C")


    def lambda_2452():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2452)

    def lambda_2464():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2464)

    def lambda_2476():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2476)

    def lambda_2488():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2488)
    Sleep(2500)
    Return()

    # Function_17_244C end

    def Function_18_249A(): pass

    label("Function_18_249A")


    def lambda_24A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_24A0)

    def lambda_24B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_24B2)

    def lambda_24C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_24C4)

    def lambda_24D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_24D6)
    Sleep(2000)
    Return()

    # Function_18_249A end

    SaveToFile()

Try(main)
