from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5513   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'Agate',                                # 9
        'Mez Beast',                            # 10
        'Mez Beast',                            # 11
        'Sealing Stone 11',                     # 12
        ' ',                                    # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT06/CH20137 ._CH',             # 00
        'ED6_DT07/CH00151 ._CH',             # 01
        'ED6_DT29/CH14750 ._CH',             # 02
        'ED6_DT29/CH14751 ._CH',             # 03
        'ED6_DT29/CH14530 ._CH',             # 04
        'ED6_DT29/CH14531 ._CH',             # 05
        'ED6_DT29/CH14540 ._CH',             # 06
        'ED6_DT29/CH14541 ._CH',             # 07
        'ED6_DT29/CH14770 ._CH',             # 08
        'ED6_DT29/CH14771 ._CH',             # 09
        'ED6_DT26/CH20621 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT06/CH20137P._CP',             # 00
        'ED6_DT07/CH00151P._CP',             # 01
        'ED6_DT29/CH14750P._CP',             # 02
        'ED6_DT29/CH14751P._CP',             # 03
        'ED6_DT29/CH14530P._CP',             # 04
        'ED6_DT29/CH14531P._CP',             # 05
        'ED6_DT29/CH14540P._CP',             # 06
        'ED6_DT29/CH14541P._CP',             # 07
        'ED6_DT29/CH14770P._CP',             # 08
        'ED6_DT29/CH14771P._CP',             # 09
        'ED6_DT26/CH20621P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x49,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 10370,
        Z                   = 0,
        Y                   = -15200,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32070,
        Z                   = 1250,
        Y                   = -36200,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22310,
        Z                   = 0,
        Y                   = -34560,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 73450,
        TriggerZ            = 0,
        TriggerY            = -73160,
        TriggerRange        = 1000,
        ActorX              = 73450,
        ActorZ              = 2000,
        ActorY              = -73160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 32950,
        TriggerZ            = 0,
        TriggerY            = -13410,
        TriggerRange        = 1000,
        ActorX              = 32950,
        ActorZ              = 1000,
        ActorY              = -13410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71300,
        TriggerZ            = 0,
        TriggerY            = 13500,
        TriggerRange        = 1000,
        ActorX              = 71500,
        ActorZ              = 3000,
        ActorY              = 14500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_262",          # 00, 0
        "Function_1_297",          # 01, 1
        "Function_2_33E",          # 02, 2
        "Function_3_469",          # 03, 3
        "Function_4_655",          # 04, 4
        "Function_5_6AE",          # 05, 5
        "Function_6_6C5",          # 06, 6
        "Function_7_6D6",          # 07, 7
        "Function_8_1164",         # 08, 8
        "Function_9_1B51",         # 09, 9
        "Function_10_1B75",        # 0A, 10
        "Function_11_1B9E",        # 0B, 11
        "Function_12_1BC7",        # 0C, 12
        "Function_13_1BF0",        # 0D, 13
        "Function_14_1C45",        # 0E, 14
        "Function_15_1CAD",        # 0F, 15
        "Function_16_1D15",        # 10, 16
        "Function_17_1F97",        # 11, 17
        "Function_18_1FF0",        # 12, 18
        "Function_19_220F",        # 13, 19
        "Function_20_22C8",        # 14, 20
    )


    def Function_0_262(): pass

    label("Function_0_262")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_296")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_296")

    Return()

    # Function_0_262 end

    def Function_1_297(): pass

    label("Function_1_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8")
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x8A, 0x0)

    label("loc_2A8")

    OP_82(0x8B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2BB")
    OP_82(0x8C, 0x0)
    Jump("loc_2BE")

    label("loc_2BB")

    OP_82(0x8D, 0x0)

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0")
    OP_6F(0x1B, 0)
    Jump("loc_2D7")

    label("loc_2D0")

    OP_6F(0x1B, 60)

    label("loc_2D7")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31D")
    OP_43(0x14, 0x0, 0x0, 0x3)
    Jump("loc_33D")

    label("loc_31D")

    OP_44(0x14, 0x3)
    OP_24(0x10D, 0x0)
    OP_23(0x10D)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)

    label("loc_33D")

    Return()

    # Function_1_297 end

    def Function_2_33E(): pass

    label("Function_2_33E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15F, 1)"), scpexpr(EXPR_END)), "loc_3AC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x5F\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29D8)
    Jump("loc_414")

    label("loc_3AC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x5F\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x5F\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_414")

    Jump("loc_45B")

    label("loc_417")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I thought we could be friends...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8D, 0x0)

    label("loc_45B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_33E end

    def Function_3_469(): pass

    label("Function_3_469")

    OP_44(0x14, 0x3)
    OP_24(0x10D, 0x0)
    OP_23(0x10D)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    Call(0, 4)
    OP_43(0x14, 0x3, 0x0, 0x5)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x80, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x81, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x82, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x83, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x84, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x85, 0x1, 0x44C)
    Call(0, 4)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C1(0x86, 0x1, 0x44C)
    Call(0, 4)
    Return()

    # Function_3_469 end

    def Function_4_655(): pass

    label("Function_4_655")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_67A"),
        (1, "loc_67D"),
        (2, "loc_685"),
        (3, "loc_68D"),
        (4, "loc_695"),
        (5, "loc_69D"),
        (SWITCH_DEFAULT, "loc_6A5"),
    )


    label("loc_67A")

    Jump("loc_6AD")

    label("loc_67D")

    Sleep(500)
    Jump("loc_6AD")

    label("loc_685")

    Sleep(1000)
    Jump("loc_6AD")

    label("loc_68D")

    Sleep(1500)
    Jump("loc_6AD")

    label("loc_695")

    Sleep(2000)
    Jump("loc_6AD")

    label("loc_69D")

    Sleep(2500)
    Jump("loc_6AD")

    label("loc_6A5")

    Sleep(3000)
    Jump("loc_6AD")

    label("loc_6AD")

    Return()

    # Function_4_655 end

    def Function_5_6AE(): pass

    label("Function_5_6AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C4")
    OP_22(0x10D, 0x0, 0x64)
    Sleep(7000)
    Jump("Function_5_6AE")

    label("loc_6C4")

    Return()

    # Function_5_6AE end

    def Function_6_6C5(): pass

    label("Function_6_6C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 5)), scpexpr(EXPR_END)), "loc_6CD")
    Return()

    label("loc_6CD")

    Call(0, 7)
    Call(0, 8)
    Return()

    # Function_6_6C5 end

    def Function_7_6D6(): pass

    label("Function_7_6D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    SetChrPos(0x109, 70870, 0, -30370, 0)
    SetChrPos(0x102, 72150, 0, -30500, 0)
    SetChrPos(0xF0, 70630, 0, -31920, 0)
    SetChrPos(0xF1, 72050, 0, -31950, 0)
    OP_6D(72310, 0, -29470, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(279, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_820")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_887")

    label("loc_820")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_848")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_887")

    label("loc_848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_870")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_887")

    label("loc_870")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_887")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B4")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91B")

    label("loc_8B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91B")

    label("loc_8DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91B")

    label("loc_904")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_91B")

    Sleep(1000)

    def lambda_926():
        OP_6D(72800, 2200, -17770, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_926)

    def lambda_93E():
        OP_67(0, 5700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_93E)

    def lambda_956():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_956)

    def lambda_966():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_966)

    def lambda_976():
        OP_6E(299, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_976)
    WaitChrThread(0xEE, 0x2)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 71340, 2100, -19250, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 69800, 2000, -17200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 73320, 2000, -17200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_A4D():
        OP_6B(2420, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A4D)
    OP_22(0x85, 0x1, 0x64)

    def lambda_A62():

        label("loc_A62")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_A62")

    QueueWorkItem2(0x109, 0, lambda_A62)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, 71340, -1000, -19250, 180)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x0, 0x0, 0xD)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 69800, -2000, -17200, 180)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x11, 0x0, 0x0, 0xE)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 73320, -2000, -17200, 180)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x12, 0x0, 0x0, 0xF)
    WaitChrThread(0x10, 0x0)
    OP_1D(0xC4)
    Fade(1000)
    OP_44(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    ClearChrFlags(0x10, 0x20)
    Sleep(500)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #3
        0x10,
        "#557F#5P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4F")

    ChrTalk(    #4
        0x107,
        "#065F#1POh, no!\x02",
    )

    CloseMessageWindow()

    label("loc_B4F")


    ChrTalk(    #5
        0x102,
        "#1506F#1PAgate!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(72600, 1250, -22740, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    OP_43(0x109, 0x0, 0x0, 0x9)
    OP_43(0x102, 0x0, 0x0, 0xA)
    OP_43(0xF0, 0x0, 0x0, 0xB)
    OP_43(0xF1, 0x0, 0x0, 0xC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C06")

    ChrTalk(    #6
        0x105,
        "#1163F#12PAgate...\x02",
    )

    CloseMessageWindow()

    label("loc_C06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4E")

    ChrTalk(    #7
        0x10A,
        "#1316F#12PCrap. We're up against Agate this time?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C9F")

    label("loc_C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9F")

    ChrTalk(    #8
        0x10B,
        (
            "#413F#12POh, boy. We're up against the Heavy Blade\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D01")

    ChrTalk(    #9
        0x108,
        (
            "#070F#12PHaha... Now, this looks like it's going to\x01",
            "be a fight to remember.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D60")

    label("loc_D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(    #10
        0x103,
        (
            "#1534F#12PWell, well. This looks like it's going to be\x01",
            "a fight to remember.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC1")

    ChrTalk(    #11
        0x104,
        (
            "#1541F#12PHe looks even more wild and untamed than\x01",
            "even my dreams. Very nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(    #12
        0x10D,
        (
            "#277F#12PAgate's reputation precedes him... He's sure\x01",
            "to be a worthy foe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6A")

    label("loc_E21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6A")

    ChrTalk(    #13
        0x10E,
        "#178F#12PHe'll be a worthy foe, that much is certain.\x02",
    )

    CloseMessageWindow()

    label("loc_E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(    #14
        0x109,
        (
            "#1065F#5PThis fight isn't gonna be the easiest,\x01",
            "but it's not anything we can't handle.\x02\x03",

            "#1069FYou ready to take him down, Tita?\x02\x03",

            "Together, we're gonna rescue him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x107,
        "#062F#12PYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF2")

    label("loc_F37")


    ChrTalk(    #16
        0x109,
        (
            "#1065F#5PThis fight isn't gonna be the easiest,\x01",
            "but it's not anything we can't handle.\x02\x03",

            "#1069FLet's do this, guys!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(430, 240, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #17
        "\x07\x00#4SRight!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_FF2")

    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1006():
        OP_6D(72200, 1050, -23340, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1006)

    def lambda_101E():
        OP_67(0, 5330, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_101E)

    def lambda_1036():
        OP_6B(2440, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1036)

    def lambda_1046():
        OP_6E(300, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1046)
    SetChrChipByIndex(0x10, 1)

    def lambda_105B():
        OP_8F(0xFE, 0x117B0, 0x0, 0xFFFF9FAC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_105B)

    def lambda_1076():
        OP_8F(0xFE, 0x1162A, 0x1F4, 0xFFFFA628, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1076)
    Sleep(10)

    def lambda_1096():
        OP_8F(0xFE, 0x11B3E, 0xFA, 0xFFFFA4B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1096)
    Sleep(10)
    SetChrChipByIndex(0x11, 9)

    def lambda_10BB():

        label("loc_10BB")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_10BB")

    QueueWorkItem2(0x11, 3, lambda_10BB)

    def lambda_10CE():
        OP_8F(0xFE, 0x1121A, 0x3E8, 0xFFFFA9AC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_10CE)

    def lambda_10E9():
        OP_8F(0xFE, 0x1162A, 0x1F4, 0xFFFFA628, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_10E9)
    Sleep(10)
    SetChrChipByIndex(0x12, 9)

    def lambda_110E():

        label("loc_110E")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_110E")

    QueueWorkItem2(0x12, 3, lambda_110E)

    def lambda_1121():
        OP_8F(0xFE, 0x11AF8, 0x3E8, 0xFFFFA8C6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1121)

    def lambda_113C():
        OP_8F(0xFE, 0x11B3E, 0xFA, 0xFFFFA4B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_113C)
    WaitChrThread(0x109, 0x1)
    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_7_6D6 end

    def Function_8_1164(): pass

    label("Function_8_1164")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    SetChrPos(0xEE, 70690, 0, -24800, 0)
    SetChrPos(0xEF, 72070, 0, -25030, 0)
    SetChrPos(0xF0, 70250, 0, -26400, 0)
    SetChrPos(0xF1, 71930, 0, -26490, 0)
    SetChrChipByIndex(0xEE, 11)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 13)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 15)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 17)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_6D(73050, 1000, -21630, 0)
    OP_67(0, 3960, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 71340, 3200, -19250, 0)
    PlayEffect(0x7, 0x7, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_13A6():
        OP_6D(71930, 1550, -21000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13A6)

    def lambda_13BE():
        OP_67(0, 3460, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13BE)

    def lambda_13D6():
        OP_6B(2820, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_13D6)

    def lambda_13E6():
        OP_6E(347, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_13E6)
    OP_8E(0x109, 0x11648, 0x7D0, 0xFFFFB028, 0x7D0, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x13, 0x11684, 0xCE4, 0xFFFFB1CC, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Found \x1F\x5C\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35C, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #19
        0x109,
        (
            "#1075F#5PWhew... Well, that's that.\x02\x03",

            "#1840FFor the love of Aidios, though. He's a damn tank.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1611")

    ChrTalk(    #20
        0x107,
        (
            "#560F#11PN-Now we can free him, right?\x02\x03",

            "#067FLet's hurry back to the garden, please! Quickly!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #21
        0x109,
        "#1066F#5POkay, okay. We're going.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1501F#11PHaha... Well, it's not like we have any reason\x01",
            "to stay here any longer. Let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_1611")


    ChrTalk(    #23
        0x102,
        (
            "#1513F#11PHe certainly is...though I wouldn't expect any less.\x02\x03",

            "#1500FStill, now we should be able to have him fighting\x01",
            "on our side.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_170D")

    ChrTalk(    #24
        0x10A,
        (
            "#819F#11PHeehee. I'm sure Tita'll be stoked to hear\x01",
            "about this. Let's go back and tell her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_170D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178B")

    ChrTalk(    #25
        0x103,
        (
            "#1536F#11PI'm sure Tita will be over the moon to hear\x01",
            "about this. We should head back and let her\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_178B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181E")

    ChrTalk(    #26
        0x105,
        (
            "#1168F#11PI'm sure Tita will be really happy to hear about\x01",
            "this. We should return to the garden and let her\x01",
            "know right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_181E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1892")

    ChrTalk(    #27
        0x10E,
        (
            "#171F#11PI'm sure Tita will be delighted. We should go\x01",
            "and tell her the good news right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_1892")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1907")

    ChrTalk(    #28
        0x104,
        (
            "#1541F#11PI'm sure Tita will be delighted. We should go\x01",
            "and tell her the good news right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_1907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198A")

    ChrTalk(    #29
        0x108,
        (
            "#071F#11PHaha... Tita's gonna be thrilled to hear about\x01",
            "this. We should go back and let her know right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_198A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A06")

    ChrTalk(    #30
        0x10B,
        (
            "#211F#11PWell, I'm guessing that Tita's gonna be\x01",
            "super happy to hear this. We should go\x01",
            "let her know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_1A06")

    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #31
        0x109,
        (
            "#1065F#5PYeah... We should head back and let Tita know.\x01",
            "I'm sure she'll be happy to hear about this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7C")

    OP_A2(0x290D)
    OP_28(0x34, 0x1, 0x4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(71500, 2000, -20000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71500, 2000, -20000, 180)
    SetChrPos(0x1, 71500, 2000, -20000, 180)
    SetChrPos(0x2, 71500, 2000, -20000, 180)
    SetChrPos(0x3, 71500, 2000, -20000, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_1164 end

    def Function_9_1B51(): pass

    label("Function_9_1B51")

    OP_8E(0xFE, 0x11418, 0x0, 0xFFFF973C, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_9_1B51 end

    def Function_10_1B75(): pass

    label("Function_10_1B75")

    Sleep(100)
    OP_8E(0xFE, 0x119C2, 0x0, 0xFFFF96E2, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_10_1B75 end

    def Function_11_1B9E(): pass

    label("Function_11_1B9E")

    Sleep(24)
    OP_8E(0xFE, 0x11288, 0x0, 0xFFFF9048, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_1B9E end

    def Function_12_1BC7(): pass

    label("Function_12_1BC7")

    Sleep(330)
    OP_8E(0xFE, 0x11A62, 0x0, 0xFFFF90CA, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_1BC7 end

    def Function_13_1BF0(): pass

    label("Function_13_1BF0")

    PlayEffect(0x1, 0x3, 0xFF, 71340, 2100, -19250, 0, 0, 0, 600, 700, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_1BF0 end

    def Function_14_1C45(): pass

    label("Function_14_1C45")

    PlayEffect(0x1, 0x4, 0xFF, 69800, 2000, -17200, 0, 0, 0, 800, 900, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1C80():

        label("loc_1C80")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1C80")

    QueueWorkItem2(0xFE, 3, lambda_1C80)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x578, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_14_1C45 end

    def Function_15_1CAD(): pass

    label("Function_15_1CAD")

    PlayEffect(0x1, 0x5, 0xFF, 73320, 2000, -17200, 0, 0, 0, 800, 900, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1CE8():

        label("loc_1CE8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1CE8")

    QueueWorkItem2(0xFE, 3, lambda_1CE8)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x578, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_1CAD end

    def Function_16_1D15(): pass

    label("Function_16_1D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE4")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3584)
    Sleep(500)
    Jump("loc_1DE7")

    label("loc_1DE4")

    TalkBegin(0xFF)

    label("loc_1DE7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #32
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F66")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E7F"),
        (1, "loc_1EFA"),
        (2, "loc_1F28"),
        (SWITCH_DEFAULT, "loc_1F56"),
    )


    label("loc_1E7F")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F63")

    label("loc_1EFA")

    OP_A9(0x21)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #33
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1F63")

    label("loc_1F28")

    OP_A9(0x7)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1F63")

    label("loc_1F56")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F63")

    label("loc_1F63")

    Jump("loc_1E23")

    label("loc_1F66")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F93")
    OP_A2(0x2591)
    EventEnd(0x1)
    Jump("loc_1F96")

    label("loc_1F93")

    TalkEnd(0xFF)

    label("loc_1F96")

    Return()

    # Function_16_1D15 end

    def Function_17_1F97(): pass

    label("Function_17_1F97")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_17_1F97 end

    def Function_18_1FF0(): pass

    label("Function_18_1FF0")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 72240, 0, 12500, 0)
    SetChrPos(0x1, 70570, 0, 12430, 0)
    SetChrPos(0x2, 71940, 0, 10790, 0)
    SetChrPos(0x3, 70470, 0, 10730, 0)
    OP_6D(71160, 0, 12790, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C6")
    OP_28(0xC, 0x4, 0x2)
    OP_82(0x8C, 0x2)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_20C6")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x05#40WFood is the basis of all...\x01",
            "Man can only tread the right\x01",
            "path with food in his stomach...\x01",
            "#500W \x01",
            "#40WOnly when you have committed\x01",
            "twenty kinds of food to memory\x01",
            "shall this door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2203")
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2200")
    Call(0, 19)

    label("loc_2200")

    Jump("loc_2203")

    label("loc_2203")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_18_1FF0 end

    def Function_19_220F(): pass

    label("Function_19_220F")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1D)
    Sleep(500)

    def lambda_2278():
        OP_6B(3280, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2278)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_23(0x85)
    OP_E3(0x0, 0xD, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_220F end

    def Function_20_22C8(): pass

    label("Function_20_22C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 72240, 0, 12500, 0)
    SetChrPos(0x1, 70570, 0, 12430, 0)
    SetChrPos(0x2, 71940, 0, 10790, 0)
    SetChrPos(0x3, 70470, 0, 10730, 0)
    OP_6D(71160, 0, 12790, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_20_22C8 end

    SaveToFile()

Try(main)
