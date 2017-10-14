from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001   ._SN',
        MapName             = 'map1',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 16,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0001   ._SN',
            'ED6_DT01/T0001_1 ._SN',
            'ED6_DT01/T0001_2 ._SN',
            'ED6_DT01/T0001_3 ._SN',
            'ED6_DT01/T0001_4 ._SN',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Villager 1',                           # 9
        'Unya',                                 # 10
        'Map Object 0',                         # 11
        'Treasure Chest',                       # 12
        'Treasure Chest',                       # 13
        '',                                     # 14
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT09/CH10000 ._CH',             # 01
        'ED6_DT09/CH10001 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT09/CH10000P._CP',             # 01
        'ED6_DT09/CH10001P._CP',             # 02
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x100,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 10000,
        Z                   = 0,
        Y                   = -4000,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 10000,
        Y                   = 0,
        Z                   = -1000,
        Range               = 11000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 1000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18000,
        TriggerZ            = 1000,
        TriggerY            = 18000,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_1E7",          # 01, 1
        "Function_2_5D3",          # 02, 2
        "Function_3_5D4",          # 03, 3
        "Function_4_61F",          # 04, 4
        "Function_5_620",          # 05, 5
        "Function_6_625",          # 06, 6
        "Function_7_923",          # 07, 7
        "Function_8_A77",          # 08, 8
        "Function_9_AB3",          # 09, 9
        "Function_10_AC8",         # 0A, 10
        "Function_11_AEC",         # 0B, 11
        "Function_12_D56",         # 0C, 12
        "Function_13_E72",         # 0D, 13
        "Function_14_EF6",         # 0E, 14
        "Function_15_F04",         # 0F, 15
        "Function_16_F0E",         # 10, 16
        "Function_17_F28",         # 11, 17
        "Function_18_119A",        # 12, 18
        "Function_19_11BC",        # 13, 19
        "Function_20_1278",        # 14, 20
        "Function_21_129E",        # 15, 21
        "Function_22_12C2",        # 16, 22
        "Function_23_12E0",        # 17, 23
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Return()

    # Function_0_1E6 end

    def Function_1_1E7(): pass

    label("Function_1_1E7")

    OP_A3(0x21E)
    Event(0, 11)
    OP_62(0x9, 0xFFFFFDA8, 300, 0x80, 0x21, 0xFA, 0x0)
    SetChrFlags(0x9, 0x6)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -4000, 1000, -2000, 0)
    OP_51(0x9, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3")
    OP_A2(0x219)
    RemoveParty(0x0, 0xFF)
    AddParty(0x1, 0x0)
    AddParty(0x0, 0x1)
    AddParty(0x5, 0x2)
    AddParty(0x7, 0x3)
    OP_31(0x3, 0x0, 0x3)
    OP_31(0x4, 0x0, 0x3)
    OP_31(0x6, 0x0, 0x3)
    OP_31(0x2, 0x0, 0x3)
    OP_31(0x0, 0x7, 0x4)
    OP_31(0x0, 0x0, 0x3)
    OP_31(0x1, 0x7, 0x3)
    OP_31(0x1, 0x0, 0x3)
    OP_31(0x0, 0x7, 0x3)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x74)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0xA)
    OP_34(0x0, 0xB)
    OP_34(0x0, 0xD)
    OP_34(0x0, 0x10)
    OP_34(0x0, 0x14)
    OP_34(0x0, 0x18)
    OP_34(0x0, 0x32)
    OP_34(0x0, 0x33)
    OP_34(0x0, 0x34)
    OP_34(0x0, 0x36)
    OP_34(0x0, 0x3E)
    OP_34(0x0, 0x3F)
    OP_34(0x0, 0x4B)
    OP_34(0x0, 0x4C)
    OP_34(0x0, 0x50)
    OP_34(0x0, 0x64)
    OP_34(0x0, 0x69)
    OP_34(0x1, 0x6E)
    OP_34(0x1, 0x6F)
    OP_34(0x1, 0x70)
    OP_34(0x1, 0xA)
    OP_34(0x1, 0xC)
    OP_34(0x1, 0xD)
    OP_34(0x1, 0x14)
    OP_34(0x1, 0x15)
    OP_34(0x1, 0x17)
    OP_34(0x1, 0x32)
    OP_34(0x1, 0x33)
    OP_34(0x1, 0x34)
    OP_34(0x1, 0x36)
    OP_34(0x1, 0x37)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x4B)
    OP_34(0x1, 0x4C)
    OP_34(0x1, 0x50)
    OP_34(0x1, 0x64)
    OP_34(0x1, 0x69)
    OP_34(0x2, 0x78)
    OP_34(0x3, 0x78)
    OP_35(0x0, 0x96)
    OP_35(0x0, 0x97)
    OP_35(0x0, 0x98)
    OP_35(0x0, 0x99)
    OP_35(0x0, 0x9A)
    OP_35(0x1, 0xA0)
    OP_35(0x1, 0xA1)
    OP_35(0x1, 0xA2)
    OP_35(0x1, 0xA3)
    OP_35(0x1, 0xA4)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_35(0x2, 0xAC)
    OP_35(0x3, 0xB4)
    OP_35(0x3, 0xB5)
    OP_35(0x3, 0xB6)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_35(0x5, 0xCB)
    OP_35(0x6, 0xD2)
    OP_35(0x6, 0xD3)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDC)
    OP_36(0x0, 0xE6)
    OP_36(0x0, 0xE7)
    OP_36(0x1, 0xEB)
    OP_36(0x1, 0xEC)
    OP_36(0x2, 0xF0)
    OP_36(0x3, 0xF5)
    OP_36(0x4, 0xFA)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    OP_36(0x6, 0x104)
    OP_36(0x7, 0x109)
    OP_36(0x7, 0x10A)
    OP_41(0x0, 0x1)
    OP_41(0x1, 0x1F)
    OP_41(0x5, 0x97)
    OP_41(0x2, 0x3D)
    OP_41(0x4, 0x79)
    OP_41(0x6, 0xB5)
    OP_41(0x3, 0x5B)
    OP_41(0x7, 0x3E8)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x14)
    AddSepith(0x3, 0x14)
    OP_37(0x0, 0x0)
    OP_37(0x1, 0x0)
    OP_3E(0x258, 1)
    OP_3E(0x259, 1)
    OP_3E(0x25E, 1)
    OP_41(0x0, 0xF1)
    OP_41(0x1, 0xF1)
    OP_41(0x0, 0x10F)
    OP_41(0x1, 0x10F)
    OP_3E(0x1F5, 50)
    OP_3E(0x12D, 2)
    OP_3E(0x12E, 2)
    OP_3E(0x12F, 2)
    OP_3E(0x130, 2)
    OP_3E(0x131, 2)
    OP_3E(0x132, 2)
    OP_3E(0x133, 2)
    OP_3E(0x134, 2)
    OP_3E(0x135, 2)
    OP_3E(0x136, 2)
    OP_3E(0x137, 2)
    OP_3E(0x138, 2)
    OP_3E(0x139, 2)
    OP_3E(0x13A, 2)
    OP_3E(0x13B, 2)
    OP_3E(0x13C, 2)
    OP_3E(0x13D, 2)
    OP_3E(0x13E, 2)
    OP_3E(0x13F, 2)
    OP_3E(0x140, 2)
    OP_3E(0x141, 2)
    OP_3E(0x142, 2)
    OP_3E(0x143, 2)
    OP_3E(0x144, 2)
    OP_3E(0x145, 2)
    OP_3E(0x146, 2)
    OP_3E(0x147, 2)
    OP_3E(0x258, 4)
    OP_3E(0x25B, 4)
    OP_3E(0x25E, 4)
    OP_3E(0x261, 4)
    OP_3E(0x264, 4)
    OP_3E(0x267, 4)
    OP_3E(0x26A, 4)
    OP_3E(0x26D, 4)
    OP_3E(0x270, 4)
    OP_3E(0x273, 4)
    OP_3E(0x276, 4)
    OP_3E(0x279, 1)
    OP_3E(0x27A, 1)
    OP_3E(0x27B, 1)
    OP_3E(0x27C, 1)
    OP_3E(0x285, 1)
    OP_3E(0x286, 1)
    OP_3E(0x287, 1)
    OP_3E(0x27D, 1)
    OP_3E(0x27E, 1)
    OP_3E(0x27F, 1)
    OP_3E(0x280, 1)
    OP_3E(0x281, 1)
    OP_3E(0x282, 1)
    OP_3E(0x283, 1)
    OP_3E(0x28A, 2)
    OP_3E(0x28B, 2)
    OP_3E(0x28D, 4)
    OP_3E(0x294, 4)
    OP_3E(0x296, 4)
    OP_3E(0x2B2, 4)
    OP_3E(0x2BC, 2)
    OP_3E(0x2BD, 2)
    OP_3E(0x2BE, 2)
    OP_3E(0x2C6, 2)
    OP_3E(0x2C8, 2)
    OP_3E(0x2C1, 2)
    OP_3E(0x28C, 2)
    OP_3E(0x291, 2)
    OP_3E(0x2D0, 1)
    OP_3E(0x2D1, 1)
    OP_3E(0x2D2, 1)
    OP_3E(0x2D3, 1)
    OP_3E(0x2D4, 1)
    SetMapFlags(0x1000000)
    SetMapFlags(0x800000)

    label("loc_5C3")

    SetMapFlags(0x1)
    ClearMapFlags(0x20)
    ClearMapFlags(0x400000)
    Return()

    # Function_1_1E7 end

    def Function_2_5D3(): pass

    label("Function_2_5D3")

    Return()

    # Function_2_5D3 end

    def Function_3_5D4(): pass

    label("Function_3_5D4")

    SetChrPos(0xC, 2000, 0, 2000, 0)
    OP_A1(0xC, 0x6)
    Sleep(1)
    SetChrBattleFlags(0x8, 0x20)
    OP_89(0x8, 2000, 2000, 2000, 0)
    Sleep(3000)
    OP_8F(0xC, 0xFA0, 0x3E8, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_3_5D4 end

    def Function_4_61F(): pass

    label("Function_4_61F")

    Return()

    # Function_4_61F end

    def Function_5_620(): pass

    label("Function_5_620")

    Call(0, 11)
    Return()

    # Function_5_620 end

    def Function_6_625(): pass

    label("Function_6_625")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_645")

    ChrTalk(    #0
        0xFE,
        "Local Flags set!\x02",
    )

    CloseMessageWindow()

    label("loc_645")

    OP_A2(0x12)
    SetMessageWindowPos(100, 100, 15, 2)

    AnonymousTalk(    #1
        (
            "#200WSpecify coordinates to display.\x02\x01",

            "#WFor realz!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2 op#A
        (
            "#20A2Wait a moment~\x02",

            "#AIf you don't specify anything,\x01",
            "it will center the screen~\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        "Specify default coordinates to reset.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #4
        0xFE,
        "#010F#1PTop-Left\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#010F#2PTop-Right\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#010F#3PBottom-Left\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#010F#4PBottom-Right\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#010F#5PTop-Center\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#010F#6PBottom-Center\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Did you know you can press\x01",
            "F11 to change stuff too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#010FI'm Aina! And I'm awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x1,
        "#020FOh? Hahahahah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1,
        (
            "#020FHow odd to meet Aina\x01",
            "in such a weird place.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Joshua")

    AnonymousTalk(    #14
        (
            "#000F夏休#4RWelp.#Testing messages..\x02\x01",

            "#4SAaaahhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    AnonymousTalk(    #15
        (
            "#F#2SABCDE#10R a   b   c   d   e#\x02\x01",

            "FGHIJKLMNO#10R FG  HI  JK  LM  NO#PQRSTUVWXY#10R PQ  RS  TU  VW  XY#\x01",
            "and also Z, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_625 end

    def Function_7_923(): pass

    label("Function_7_923")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_947")
    OP_8D(0xFE, 5000, -5000, 15000, 9000, 2000)
    OP_48()
    Jump("Function_7_923")

    label("loc_947")

    Return()

    # Function_7_923 end

    def Function_8_A77(): pass

    label("Function_8_A77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB2")
    OP_70(0x1, 0x32)
    OP_8D(0xFE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x1, 0)
    OP_72(0x1, 0x8)
    Sleep(2000)
    Jump("Function_8_A77")

    label("loc_AB2")

    Return()

    # Function_8_A77 end

    def Function_9_AB3(): pass

    label("Function_9_AB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC7")
    OP_8C(0xFE, 180, 5000)
    OP_48()
    Jump("Function_9_AB3")

    label("loc_AC7")

    Return()

    # Function_9_AB3 end

    def Function_10_AC8(): pass

    label("Function_10_AC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AEB")
    OP_8D(0x0, 10000, 10000, -10000, -10000, 2000)
    Jump("Function_10_AC8")

    label("loc_AEB")

    Return()

    # Function_10_AC8 end

    def Function_11_AEC(): pass

    label("Function_11_AEC")

    OP_16(0x1)
    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("Sara")

    AnonymousTalk(    #16
        "Choose an option.\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D40")

    Menu(
        0,
        10,
        10,
        1,
        (
            "Test Maps\x01",                    # 0
            "Game Maps\x01",                    # 1
            "Characters\x01",                   # 2
            "Monsters\x01",                     # 3
            "Map Objects\x01",                  # 4
            "Battle\x01",                       # 5
            "Battle (Algorithm Test)\x01",      # 6
            "Battle (Map Check)\x01",           # 7
            "Battle (Verify)\x01",              # 8
            "Events\x01",                       # 9
            "Shop Test\x01",                    # 10
            "Save Menu\x01",                    # 11
            "Clear Save Menu\x01",              # 12
            "Absolute Camera Test\x01",         # 13
            "Return to Title\x01",              # 14
            "Movies\x01",                       # 15
            "Cancel\x01",                       # 16
        )
    )

    MenuEnd(0x0)
    OP_16(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C55"),
        (1, "loc_C5C"),
        (2, "loc_C63"),
        (3, "loc_C6A"),
        (4, "loc_C71"),
        (5, "loc_C78"),
        (6, "loc_C7F"),
        (7, "loc_C86"),
        (8, "loc_C8D"),
        (9, "loc_C94"),
        (10, "loc_C9B"),
        (11, "loc_CA7"),
        (12, "loc_CAB"),
        (13, "loc_CAF"),
        (14, "loc_D0A"),
        (15, "loc_D0F"),
        (SWITCH_DEFAULT, "loc_D30"),
    )


    label("loc_C55")

    Call(0, 12)
    Jump("loc_D3D")

    label("loc_C5C")

    Call(3, 2)
    Jump("loc_D3D")

    label("loc_C63")

    Call(3, 0)
    Jump("loc_D3D")

    label("loc_C6A")

    Call(3, 1)
    Jump("loc_D3D")

    label("loc_C71")

    Call(0, 13)
    Jump("loc_D3D")

    label("loc_C78")

    Call(0, 17)
    Jump("loc_D3D")

    label("loc_C7F")

    Call(1, 0)
    Jump("loc_D3D")

    label("loc_C86")

    Call(2, 0)
    Jump("loc_D3D")

    label("loc_C8D")

    Call(2, 47)
    Jump("loc_D3D")

    label("loc_C94")

    Call(4, 0)
    Jump("loc_D3D")

    label("loc_C9B")

    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 19)
    Jump("loc_D3D")

    label("loc_CA7")

    ShowSaveMenu()
    Jump("loc_D3D")

    label("loc_CAB")

    SaveClearData()
    Jump("loc_D3D")

    label("loc_CAF")

    OP_5F(0x0)
    OP_56(0x0)
    Sleep(500)
    ClearMapFlags(0x1)
    OP_66(0x0)
    OP_67(-15000, 10000, -10000, 1000)
    OP_69(0x8, 0x3E8)
    OP_69(0x0, 0x3E8)
    OP_66(0x1)
    OP_67(0, 8000, -10000, 1000)
    OP_6C(45000, 1000)
    SetMapFlags(0x1)
    Sleep(500)
    Jump("loc_D3D")

    label("loc_D0A")

    OP_B4(0x0)
    Jump("loc_D3D")

    label("loc_D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_D1F")
    PlayMovie(0x1, "")
    OP_A3(0x15)
    Jump("loc_D2D")

    label("loc_D1F")

    PlayMovie(0x0, "logo.avi")
    OP_A2(0x15)

    label("loc_D2D")

    Jump("loc_D3D")

    label("loc_D30")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D3D")

    label("loc_D3D")

    Jump("loc_B1D")

    label("loc_D40")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_AEC end

    def Function_12_D56(): pass

    label("Function_12_D56")


    AnonymousTalk(    #17
        "\x06Choose a test map.\x02",
    )


    label("loc_D6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E62")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test Map 0\x01",      # 0
            "Test Map 1\x01",      # 1
            "Test Map 2\x01",      # 2
            "Test Map 3\x01",      # 3
            "Test Map 4\x01",      # 4
            "Test Map 5\x01",      # 5
            "Test Map 6\x01",      # 6
            "Test Map 7\x01",      # 7
            "Cancel\x01",          # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E0D"),
        (1, "loc_E16"),
        (2, "loc_E1F"),
        (3, "loc_E28"),
        (4, "loc_E31"),
        (5, "loc_E3A"),
        (6, "loc_E43"),
        (7, "loc_E4C"),
        (SWITCH_DEFAULT, "loc_E55"),
    )


    label("loc_E0D")

    NewScene("ED6_DT01/T0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E16")

    NewScene("ED6_DT01/T0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E1F")

    NewScene("ED6_DT01/T0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E28")

    NewScene("ED6_DT01/T0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E31")

    NewScene("ED6_DT01/T0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E3A")

    NewScene("ED6_DT01/T0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E43")

    NewScene("ED6_DT01/T0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E4C")

    NewScene("ED6_DT01/T0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E55")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D6C")

    label("loc_E62")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_D56 end

    def Function_13_E72(): pass

    label("Function_13_E72")


    AnonymousTalk(    #18
        "\x06Which?\x02",
    )


    label("loc_E7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE6")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Map Object 1\x01",      # 0
            "Map Object 2\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EC7"),
        (1, "loc_ED0"),
        (SWITCH_DEFAULT, "loc_ED9"),
    )


    label("loc_EC7")

    NewScene("ED6_DT01/T0070   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_ED0")

    NewScene("ED6_DT01/T0071   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_ED9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E7C")

    label("loc_EE6")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_E72 end

    def Function_14_EF6(): pass

    label("Function_14_EF6")

    OP_6B(5000, 3000)
    Call(0, 15)
    Return()

    # Function_14_EF6 end

    def Function_15_F04(): pass

    label("Function_15_F04")

    OP_6C(0, 20000)
    Return()

    # Function_15_F04 end

    def Function_16_F0E(): pass

    label("Function_16_F0E")

    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Return()

    # Function_16_F0E end

    def Function_17_F28(): pass

    label("Function_17_F28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Battle Test\x01",            # 0
            "Corner Check\x01",           # 1
            "Line Attack Check\x01",      # 2
            "Battle Test 2\x01",          # 3
            "10000-10070\x01",            # 4
            "10080-10150\x01",            # 5
            "10160-10220\x01",            # 6
            "00260-00330\x01",            # 7
            "00340-00410\x01",            # 8
            "Last Boss Form 1\x01",       # 9
            "Last Boss Form 2\x01",       # 10
            "Last Boss Form 3\x01",       # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1022"),
        (1, "loc_1032"),
        (2, "loc_1042"),
        (3, "loc_1052"),
        (4, "loc_1062"),
        (5, "loc_1072"),
        (6, "loc_1082"),
        (7, "loc_1092"),
        (8, "loc_10A2"),
        (9, "loc_10B2"),
        (10, "loc_10C8"),
        (11, "loc_10DE"),
        (SWITCH_DEFAULT, "loc_1144"),
    )


    label("loc_1022")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1032")

    Battle(0x7E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1042")

    Battle(0x7E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1052")

    Battle(0x7E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1062")

    Battle(0x7D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1072")

    Battle(0x7D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1082")

    Battle(0x7D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1092")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_10A2")

    Battle(0x7DC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_10B2")

    OP_1D(0x2D)
    Call(2, 48)
    Battle(0x3A1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_10C8")

    OP_1D(0x2E)
    Call(2, 48)
    Battle(0x3A2, 0x100008, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_10DE")

    OP_1D(0x2B)
    Call(2, 48)
    OP_31(0x0, 0xFA, 0x1)
    OP_31(0x1, 0xFA, 0x1)
    OP_31(0x2, 0xFA, 0x1)
    OP_31(0x3, 0xFA, 0x1)
    OP_31(0x4, 0xFA, 0x1)
    OP_31(0x5, 0xFA, 0x1)
    OP_31(0x6, 0xFA, 0x1)
    OP_31(0x7, 0xFA, 0x1)
    OP_31(0x0, 0x5, 0xC8)
    OP_31(0x1, 0x5, 0xC8)
    OP_31(0x2, 0x5, 0xC8)
    OP_31(0x3, 0x5, 0xC8)
    OP_31(0x4, 0x5, 0xC8)
    OP_31(0x5, 0x5, 0xC8)
    OP_31(0x6, 0x5, 0xC8)
    OP_31(0x7, 0x5, 0xC8)
    Battle(0x3B3, 0x10000A, 0x0, 0x0, 0xFF)
    Jump("loc_1147")

    label("loc_1144")

    Jump("loc_1147")

    label("loc_1147")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_115E"),
        (SWITCH_DEFAULT, "loc_1189"),
    )


    label("loc_115E")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jump("loc_1189")

    label("loc_1189")

    Jump("Function_17_F28")

    label("loc_118C")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_F28 end

    def Function_18_119A(): pass

    label("Function_18_119A")


    ChrTalk(    #19
        0x0,
        "Welcome to the Factory!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x0)
    Return()

    # Function_18_119A end

    def Function_19_11BC(): pass

    label("Function_19_11BC")

    SetChrName("Sara")

    AnonymousTalk(    #20
        "\x06Which shop?\x02",
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "Factory\x01",          # 0
            "Weapon Shop\x01",      # 1
            "Tool Shop\x01",        # 2
            "Inn\x01",              # 3
            "Guild\x01",            # 4
            "Read Book\x01",        # 5
            "Cancel\x01",           # 6
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_123F"),
        (1, "loc_1246"),
        (2, "loc_124D"),
        (3, "loc_1254"),
        (4, "loc_125B"),
        (5, "loc_1262"),
        (SWITCH_DEFAULT, "loc_126A"),
    )


    label("loc_123F")

    Call(0, 18)
    Jump("loc_126D")

    label("loc_1246")

    Call(0, 20)
    Jump("loc_126D")

    label("loc_124D")

    Call(0, 21)
    Jump("loc_126D")

    label("loc_1254")

    Call(0, 22)
    Jump("loc_126D")

    label("loc_125B")

    Call(0, 23)
    Jump("loc_126D")

    label("loc_1262")

    OP_B9(0x347, 0x0)
    Jump("loc_126D")

    label("loc_126A")

    Jump("loc_126D")

    label("loc_126D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_11BC end

    def Function_20_1278(): pass

    label("Function_20_1278")


    ChrTalk(    #21
        0x0,
        "Welcome to the Weapon Shop!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x1)
    Return()

    # Function_20_1278 end

    def Function_21_129E(): pass

    label("Function_21_129E")


    ChrTalk(    #22
        0x0,
        "Welcome to the Item Shop!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x2)
    Return()

    # Function_21_129E end

    def Function_22_12C2(): pass

    label("Function_22_12C2")


    ChrTalk(    #23
        0x0,
        "Welcome to the Inn!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x3)
    Return()

    # Function_22_12C2 end

    def Function_23_12E0(): pass

    label("Function_23_12E0")


    ChrTalk(    #24
        0x0,
        "Welcome to the guild!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_2A(0x1, 0x2, 0x3, 0xFFFF)
    Return()

    # Function_23_12E0 end

    SaveToFile()

Try(main)
