from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Guardian',                             # 9
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
        "Function_2_598",          # 02, 2
        "Function_3_5AE",          # 03, 3
        "Function_4_73E",          # 04, 4
        "Function_5_8B1",          # 05, 5
        "Function_6_9E1",          # 06, 6
        "Function_7_B2E",          # 07, 7
        "Function_8_C87",          # 08, 8
        "Function_9_D8F",          # 09, 9
        "Function_10_14DC",        # 0A, 10
        "Function_11_1503",        # 0B, 11
        "Function_12_152A",        # 0C, 12
        "Function_13_1551",        # 0D, 13
        "Function_14_15B3",        # 0E, 14
        "Function_15_1DA0",        # 0F, 15
        "Function_16_1E26",        # 10, 16
        "Function_17_1EB3",        # 11, 17
        "Function_18_1FC0",        # 12, 18
        "Function_19_2041",        # 13, 19
        "Function_20_213C",        # 14, 20
        "Function_21_21B4",        # 15, 21
        "Function_22_2293",        # 16, 22
        "Function_23_2372",        # 17, 23
        "Function_24_23C0",        # 18, 24
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

    OP_E0(0x8, 0x60, 0xEB, 0xFF, 0xFF, 0x90, 0x1, 0x0, 0x0, 0x8, 0xDA, 0xFF, 0xFF)
    OP_E0(0xA, 0x6, 0xEB, 0xFF, 0xFF, 0x90, 0x1, 0x0, 0x0, 0x9C, 0x2C, 0x0, 0x0)
    OP_E0(0xB, 0x68, 0x15, 0x0, 0x0, 0x90, 0x1, 0x0, 0x0, 0x38, 0x2C, 0x0, 0x0)
    OP_E0(0xD, 0xFA, 0x14, 0x0, 0x0, 0x90, 0x1, 0x0, 0x0, 0x2A, 0xDB, 0xFF, 0xFF)
    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 6)), scpexpr(EXPR_END)), "loc_443")
    SetChrFlags(0x9, 0x80)

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 7)), scpexpr(EXPR_END)), "loc_44F")
    SetChrFlags(0xA, 0x80)

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 0)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0xB, 0x80)

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 1)), scpexpr(EXPR_END)), "loc_467")
    SetChrFlags(0xC, 0x80)

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D4, 2)), scpexpr(EXPR_END)), "loc_473")
    SetChrFlags(0xD, 0x80)

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 3)), scpexpr(EXPR_END)), "loc_505")
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
    Jump("loc_58D")

    label("loc_505")

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

    label("loc_58D")

    OP_1B(0x0, 0x0, 0x12)
    OP_1B(0x1, 0x0, 0x14)
    Return()

    # Function_1_341 end

    def Function_2_598(): pass

    label("Function_2_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_598")

    label("loc_5AD")

    Return()

    # Function_2_598 end

    def Function_3_5AE(): pass

    label("Function_3_5AE")

    OP_EA(0x2, 0x8E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_686")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_61F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F70)
    Jump("loc_683")

    label("loc_61F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_683")

    Jump("loc_730")

    label("loc_686")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05As you try to open the empty chest, you break\x01",
            "part of the corner off. Hoping nobody notices,\x01",
            "you put the piece down and briskly walk away..\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_730")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5AE end

    def Function_4_73E(): pass

    label("Function_4_73E")

    OP_EA(0x2, 0x8F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_816")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_7AF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F71)
    Jump("loc_813")

    label("loc_7AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_813")

    Jump("loc_8A3")

    label("loc_816")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You scour every square inch of this chest's\x01",
            "empty innards, desperate to find any scrap of\x01",
            "treasure you missed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_73E end

    def Function_5_8B1(): pass

    label("Function_5_8B1")

    OP_EA(0x2, 0x90, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_989")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_922")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x00\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F72)
    Jump("loc_986")

    label("loc_922")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x00\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x00\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_986")

    Jump("loc_9D3")

    label("loc_989")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Empty. But THAT should come as no surprise.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9D3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8B1 end

    def Function_6_9E1(): pass

    label("Function_6_9E1")

    OP_EA(0x2, 0x91, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A52")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F73)
    Jump("loc_AB6")

    label("loc_A52")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_AB6")

    Jump("loc_B20")

    label("loc_AB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05TREASURE CHEST ADVERTISING FOR THE LOW,\x01",
            "LOW PRICE OF 900 MIRA PER MONTH.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B20")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_9E1 end

    def Function_7_B2E(): pass

    label("Function_7_B2E")

    OP_EA(0x2, 0x92, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_B9F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F74)
    Jump("loc_C03")

    label("loc_B9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_C03")

    Jump("loc_C79")

    label("loc_C06")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05This chest is but an empty husk now. Do not\x01",
            "mourn, for it is the fate of all things.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C79")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B2E end

    def Function_8_C87(): pass

    label("Function_8_C87")

    OP_EA(0x2, 0x93, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D50")
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
    OP_A2(0x1F75)
    Jump("loc_D7D")

    label("loc_D50")


    AnonymousTalk(    #16
        "\x07\x05What were you expecting to find here?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_D7D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C87 end

    def Function_9_D8F(): pass

    label("Function_9_D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 5)), scpexpr(EXPR_END)), "loc_D97")
    Return()

    label("loc_D97")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DBC")
    Call(0, 15)
    Call(0, 16)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_DBC")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1216")
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F07")

    label("loc_EC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F07")

    label("loc_EF0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F07")

    Sleep(1000)

    ChrTalk(    #17
        0x101,
        "#1004F#2PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#1042F#5PJust now, was that--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        "#024F#2PGET DOWN!\x02",
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

    def lambda_FA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FA1)

    def lambda_FB3():
        OP_8F(0xFE, 0x0, 0x2BC, 0x8EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FB3)

    def lambda_FCE():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCE)
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

    def lambda_1027():
        OP_6D(170, 400, 31000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1027)

    def lambda_103F():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_103F)
    SetChrChipByIndex(0x8, 11)

    def lambda_1054():
        OP_8F(0xFE, 0x96, 0x1F4, 0x7896, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1054)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0xFF)
    Battle(0x409, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1093"),
        (2, "loc_1154"),
        (1, "loc_120E"),
        (SWITCH_DEFAULT, "loc_1213"),
    )


    label("loc_1093")

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
    Jump("loc_1213")

    label("loc_1154")

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
    Jump("loc_1213")

    label("loc_120E")

    OP_B4(0x0)
    Jump("loc_1213")

    label("loc_1213")

    Jump("loc_14D8")

    label("loc_1216")

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

    def lambda_1266():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1266)

    def lambda_1278():
        OP_8F(0xFE, 0x0, 0x2BC, 0x8EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1278)

    def lambda_1293():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1293)
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

    def lambda_12EC():
        OP_6D(170, 400, 31000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12EC)

    def lambda_1304():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1304)
    SetChrChipByIndex(0x8, 11)

    def lambda_1319():
        OP_8F(0xFE, 0x96, 0x1F4, 0x7896, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1319)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0xFF)
    Battle(0x409, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1358"),
        (2, "loc_1419"),
        (1, "loc_14D3"),
        (SWITCH_DEFAULT, "loc_14D8"),
    )


    label("loc_1358")

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
    Jump("loc_14D8")

    label("loc_1419")

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
    Jump("loc_14D8")

    label("loc_14D3")

    OP_B4(0x0)
    Jump("loc_14D8")

    label("loc_14D8")

    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_9_D8F end

    def Function_10_14DC(): pass

    label("Function_10_14DC")

    OP_96(0xFE, 0x258, 0x190, 0x7148, 0x190, 0x1770)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_10_14DC end

    def Function_11_1503(): pass

    label("Function_11_1503")

    OP_96(0xFE, 0xFFFFFED4, 0x190, 0x7148, 0x190, 0x1770)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_1503 end

    def Function_12_152A(): pass

    label("Function_12_152A")

    OP_96(0xFE, 0x3E8, 0x190, 0x6AA4, 0x190, 0x1770)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_152A end

    def Function_13_1551(): pass

    label("Function_13_1551")

    OP_96(0xFE, 0xFFFFFD44, 0x190, 0x6AA4, 0x190, 0x1770)
    SetChrSubChip(0xFE, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_158A"),
        (4, "loc_1592"),
        (6, "loc_159A"),
        (7, "loc_15A2"),
        (8, "loc_15AA"),
        (SWITCH_DEFAULT, "loc_15B2"),
    )


    label("loc_158A")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_15B2")

    label("loc_1592")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_15B2")

    label("loc_159A")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_15B2")

    label("loc_15A2")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_15B2")

    label("loc_15AA")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_15B2")

    label("loc_15B2")

    Return()

    # Function_13_1551 end

    def Function_14_15B3(): pass

    label("Function_14_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A77")
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
            "\x07\x05#1S[About the Aureole's Seal 1/4]\x01",
            "When w■ were ■■■■ing in on ■■■■■■ing the\x01",
            "underground ■■■■■■, un■■■■■■st ■■ us, our ■eal\x01",
            "■■an w■s ■■■cover■■ by t■■ Aur■ol■. ■■■ of our\x01",
            "co■rades ■■ll v■■ti■ to ■■e s■■■t ■■■duction of ■he\x01",
            "A■■■ol■'s e■■■■■ic sim■■■■ions, ■nd he w■s lost to\x01",
            "■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x05#1SHowe■er, the s■■■er ■■■in■ in this ■isast■■ was\x01",
            "t■■t ■■■■ co■■ade was not ■■ar■ of the ■■■■ scale\x01",
            "of the p■■■. ■ith the ■■forma■■on it g■■■■■ed from\x01",
            "his ■■■d, the ■ureole ■■■■■■■ ■■■■■■ on ■■■\x01",
            "un■■■gro■■■ ■acilit■ by the ■■■■side, and i■ p■■d\x01",
            "no a■■entio■ to the ■■■enb■■g or the ■evice\x01",
            "Tow■■■. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x07\x00Received #1029i.\x02",
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
    Jump("loc_1D9C")

    label("loc_1A77")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #23
        (
            "\x07\x05#1S[About the Aureole's Seal 1/4]\x01",
            "When w■ were ■■■■ing in on ■■■■■■ing the\x01",
            "underground ■■■■■■, un■■■■■■st ■■ us, our ■eal\x01",
            "■■an w■s ■■■cover■■ by t■■ Aur■ol■. ■■■ of our\x01",
            "co■rades ■■ll v■■ti■ to ■■e s■■■t ■■■duction of ■he\x01",
            "A■■■ol■'s e■■■■■ic sim■■■■ions, ■nd he w■s lost to\x01",
            "■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05#1SHowe■er, the s■■■er ■■■in■ in this ■isast■■ was\x01",
            "t■■t ■■■■ co■■ade was not ■■ar■ of the ■■■■ scale\x01",
            "of the p■■■. ■ith the ■■forma■■on it g■■■■■ed from\x01",
            "his ■■■d, the ■ureole ■■■■■■■ ■■■■■■ on ■■■\x01",
            "un■■■gro■■■ ■acilit■ by the ■■■■side, and i■ p■■d\x01",
            "no a■■entio■ to the ■■■enb■■g or the ■evice\x01",
            "Tow■■■. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1D9C")

    TalkEnd(0xFF)
    Return()

    # Function_14_15B3 end

    def Function_15_1DA0(): pass

    label("Function_15_1DA0")

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
        (0, "loc_1E19"),
        (1, "loc_1E1F"),
        (SWITCH_DEFAULT, "loc_1E25"),
    )


    label("loc_1E19")

    OP_A2(0x1200)
    Jump("loc_1E25")

    label("loc_1E1F")

    OP_A2(0x1201)
    Jump("loc_1E25")

    label("loc_1E25")

    Return()

    # Function_15_1DA0 end

    def Function_16_1E26(): pass

    label("Function_16_1E26")

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

    # Function_16_1E26 end

    def Function_17_1EB3(): pass

    label("Function_17_1EB3")

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

    # Function_17_1EB3 end

    def Function_18_1FC0(): pass

    label("Function_18_1FC0")

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

    # Function_18_1FC0 end

    def Function_19_2041(): pass

    label("Function_19_2041")

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

    # Function_19_2041 end

    def Function_20_213C(): pass

    label("Function_20_213C")

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

    # Function_20_213C end

    def Function_21_21B4(): pass

    label("Function_21_21B4")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_21_21B4 end

    def Function_22_2293(): pass

    label("Function_22_2293")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_22_2293 end

    def Function_23_2372(): pass

    label("Function_23_2372")


    def lambda_2378():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2378)

    def lambda_238A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_238A)

    def lambda_239C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_239C)

    def lambda_23AE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_23AE)
    Sleep(2500)
    Return()

    # Function_23_2372 end

    def Function_24_23C0(): pass

    label("Function_24_23C0")


    def lambda_23C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_23C6)

    def lambda_23D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_23D8)

    def lambda_23EA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_23EA)

    def lambda_23FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_23FC)
    Sleep(2000)
    Return()

    # Function_24_23C0 end

    SaveToFile()

Try(main)
