from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1705   ._SN',
        MapName             = 'Bose',
        Location            = 'C1705.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'Renne',                                # 9
        'Vogel+',                               # 10
        'Vogel+',                               # 11
        'Vogel+',                               # 12
        'Vogel+',                               # 13
        'Vogel+',                               # 14
        'Vogel+',                               # 15
        'Gospel',                               # 16
        'Pater-Mater',                          # 17
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
        'ED6_DT27/CH03510 ._CH',             # 00
        'ED6_DT29/CH12910 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT27/CH04510 ._CH',             # 03
        'ED6_DT26/CH20306 ._CH',             # 04
        'ED6_DT27/CH04000 ._CH',             # 05
        'ED6_DT27/CH04010 ._CH',             # 06
        'ED6_DT27/CH04012 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
        'ED6_DT29/CH12910P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT27/CH04510P._CP',             # 03
        'ED6_DT26/CH20306P._CP',             # 04
        'ED6_DT27/CH04000P._CP',             # 05
        'ED6_DT27/CH04010P._CP',             # 06
        'ED6_DT27/CH04012P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 458754,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_267",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_2D5",          # 03, 3
        "Function_4_484",          # 04, 4
        "Function_5_917",          # 05, 5
        "Function_6_924",          # 06, 6
        "Function_7_2B46",         # 07, 7
        "Function_8_42C1",         # 08, 8
        "Function_9_4CBA",         # 09, 9
        "Function_10_4CF3",        # 0A, 10
        "Function_11_4D22",        # 0B, 11
        "Function_12_4E01",        # 0C, 12
        "Function_13_4E87",        # 0D, 13
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_266")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_24A")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_266")

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_266")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_266")

    Return()

    # Function_0_20A end

    def Function_1_267(): pass

    label("Function_1_267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 5)), scpexpr(EXPR_END)), "loc_27A")
    OP_B1("C1705_y")
    Jump("loc_283")

    label("loc_27A")

    OP_B1("C1705_n")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_294")
    OP_22(0xEB, 0x1, 0x50)

    label("loc_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3FD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x453), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BE")

    Return()

    # Function_1_267 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2BF")

    label("loc_2D4")

    Return()

    # Function_2_2BF end

    def Function_3_2D5(): pass

    label("Function_3_2D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-210, 0, -3180, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, 70, 0, 8530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)

    def lambda_398():
        OP_6D(240, 0, 10710, 4000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_398)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0xF, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(30, 0, 14990, 0)
    OP_67(0, 2470, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(0, 0)
    OP_6E(465, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#263F#5PHeeheehee... Renne here.\x02\x03",

            "#1305FI'm ready, so we can start\x01",
            "whenever.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2D5 end

    def Function_4_484(): pass

    label("Function_4_484")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    SetChrPos(0x8, 70, 0, 8530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_6F(0x3, 60)
    OP_6F(0x4, 60)
    OP_6F(0x5, 60)
    OP_6F(0x6, 60)
    OP_6F(0x7, 60)
    OP_70(0x3, 0x3C)
    OP_70(0x4, 0x3C)
    OP_70(0x5, 0x3C)
    OP_70(0x6, 0x3C)
    OP_70(0x7, 0x3C)
    SetChrPos(0xF, 0, 1100, 13760, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 2)
    SetChrSubChip(0xF, 14)
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_B0(0x3, 0x50)
    OP_B0(0x4, 0x50)
    OP_B0(0x5, 0x50)
    OP_B0(0x6, 0x50)
    OP_B0(0x7, 0x50)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_79(0x0, 0x1)
    OP_79(0x1, 0x1)
    OP_79(0x2, 0x1)
    OP_79(0x3, 0x1)
    OP_79(0x4, 0x1)
    OP_7B()
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 0x17ED0, 0x38E28, 0x0)
    OP_6D(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp049_03.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    Sleep(2000)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Weissmann")

    AnonymousTalk(    #1
        (
            "\x07\x00#1155FLadies! Gentlemen!\x01",
            "Our blessed celebration is ready!\x02\x03",

            "Now, go! Enjoy it to your fullest!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 60, -1, -1)
    SetChrName("Bleublanc")

    AnonymousTalk(    #2
        "\x07\x00#231FExcellent!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 60, -1, -1)
    SetChrName("Luciola")

    AnonymousTalk(    #3
        "\x07\x00#241FWe, the Enforcers of Ouroboros--\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 330, -1, -1)
    SetChrName("Walter")

    AnonymousTalk(    #4
        "\x07\x00#252FBy order of an Anguis--\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 330, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #5
        (
            "\x07\x00#1306FWe shall now liberate you of\x01",
            "your shackles!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_DB()
    OP_AD(0x2400AA, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_DC()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_484 end

    def Function_5_917(): pass

    label("Function_5_917")

    Call(0, 6)
    Call(0, 7)
    Call(0, 8)
    Return()

    # Function_5_917 end

    def Function_6_924(): pass

    label("Function_6_924")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_945")
    Call(0, 12)
    Call(0, 13)

    label("loc_945")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x9, 0x4)
    Call(0, 11)
    OP_D2(0x270246, 0x270250, 0xA)
    OP_D2(0x270244, 0x27024E, 0xB)
    OP_D2(0x290391, 0x290395, 0xC)
    OP_6D(-150, 8440, -4110, 0)
    OP_67(0, 2640, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(68000, 0)
    OP_6E(413, 0)
    SetChrPos(0x8, -450, 950, 12440, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0xF8, 820, -1750, -7480, 0)
    SetChrPos(0xF9, -750, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_70(0x5, 0x8)
    OP_70(0x6, 0x8)
    OP_70(0x7, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AB6():
        OP_6D(430, 0, -2500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AB6)

    def lambda_ACE():
        OP_67(0, 8960, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ACE)

    def lambda_AE6():
        OP_6B(2300, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AE6)

    def lambda_AF6():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AF6)

    def lambda_B06():
        OP_6E(315, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B06)
    FadeToBright(1000, 0)
    Sleep(4000)
    ClearChrFlags(0x101, 0x80)

    def lambda_B29():
        OP_8E(0xFE, 0x2E4, 0x0, 0xFFFFF808, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B29)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_B4E():
        OP_8E(0xFE, 0xFFFFFD76, 0x0, 0xFFFFF827, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4E)
    Sleep(600)
    ClearChrFlags(0xF8, 0x80)

    def lambda_B73():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFF240, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B73)
    Sleep(100)
    ClearChrFlags(0xF9, 0x80)

    def lambda_B98():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xFFFFF1FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B98)
    WaitChrThread(0xF9, 0x1)

    NpcTalk(    #6
        0x8,
        "Girl's Voice",
        (
            "You're really rude, you know?\x01",
            "I was soooo sick of waiting!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5E")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C9C")

    label("loc_C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C85")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C9C")

    label("loc_C85")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C9C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D06")

    label("loc_CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEF")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D06")

    label("loc_CEF")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D06")

    Sleep(1000)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_D18():
        OP_6D(40, 950, 12620, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D18)

    def lambda_D30():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D30)

    def lambda_D48():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D48)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Fade(500)
    OP_6D(0, 950, 9500, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(0, 0)
    OP_6E(247, 0)
    SetChrPos(0x101, 150, -1750, -7480, 0)
    SetChrPos(0x102, -1000, -1750, -7480, 0)
    SetChrPos(0xF8, 900, -1750, -7480, 0)
    SetChrPos(0xF9, -200, -1750, -7480, 0)

    def lambda_DE8():
        OP_8E(0xFE, 0x96, 0x0, 0x157C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE8)
    Sleep(300)

    def lambda_E08():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x11BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E08)
    Sleep(300)

    def lambda_E28():
        OP_8E(0xFE, 0x384, 0x0, 0x10CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_E28)
    Sleep(300)

    def lambda_E48():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xC1C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_E48)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x101,
        "#1002F#5PRenne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#263F#6PHeehee!\x02\x03",

            "Estelle, you're a baaaaaad girl,\x01",
            "running away from the Ark while\x01",
            "little Renne was away. \x02\x03",

            "#1305FBut it's okay! You came here to\x01",
            "play in the end, so all is forgiven.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1019")

    ChrTalk(    #9
        0x107,
        "#063FRenne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#1306F#6PHee, Tita! Did you come all this way\x01",
            "to play, too?\x02\x03",

            "I'm sorry I don't have any ice cream,\x01",
            "but we'll still have lots of fun. I PROMISE.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #11
        0x107,
        "#065FUm... Umm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1066")

    label("loc_1019")


    ChrTalk(    #12
        0x101,
        (
            "#1019F#5PI think you and I have different\x01",
            "definitions of 'play,' Renne.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1066")


    ChrTalk(    #13
        0x8,
        (
            "#263F#6PAlso... Heeheehee.\x01",
            "You finally show yourself, huh?\x02\x03",

            "#260FYou left me waiting for a long\x01",
            "time, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1035F#5PI never thought I would meet you\x01",
            "again, here, of all places.\x02\x03",

            "#1040FYou... You've grown a bit, Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#261F#6POf course I have!\x01",
            "I'm eleven years old now.\x02\x03",

            "#265FAnd Estelle was right--you got\x01",
            "really handsome while you were\x01",
            "away, Joshua.\x02\x03",

            "It's a little weird seeing you\x01",
            "without the cold eyes, but...\x02\x03",

            "#261FI suppose you aren't so bad now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1053F#5PReally? Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1007F#5PFor the love of... Why do you always\x01",
            "try to act so grown-up, Renne?\x02\x03",

            "#1015FOkay. Renne?\x02\x03",

            "You know we're here to stop\x01",
            "the society's plan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#263F#6PYes, I'm aware.\x02\x03",

            "#269FAnd I hate being bored, so I'd be\x01",
            "glad to play with you for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 14)

    def lambda_1374():
        OP_99(0x8, 0xE, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1374)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_138E():
        OP_99(0x8, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_138E)
    Sleep(200)
    Fade(500)

    def lambda_13A8():
        OP_6B(4000, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_13A8)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_13C7():
        OP_99(0x8, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13C7)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1440")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_147E")

    label("loc_1440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1467")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_147E")

    label("loc_1467")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_147E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14E8")

    label("loc_14AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D1")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14E8")

    label("loc_14D1")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14E8")

    Sleep(1000)

    ChrTalk(    #19
        0x8,
        (
            "#1306F#6PHeh heh. Try to enjoy yourselves,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1042F#5PRenne, that's enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1007F#5PSorry, but we're not here to fight\x01",
            "you.\x02\x03",

            "#1002FI want to do something way more\x01",
            "important. I want to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#264F#6PTalk?\x02\x03",

            "#261FOooh, is it story time?\x01",
            "Is it a fairy tale?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1003F#5PNo. It's about your invitation\x01",
            "to join the society.\x02\x03",

            "#1025FI appreciate the offer, but I refuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#268F#6P*siiiiigh* Well, you found Joshua on\x01",
            "your own, so I guess that doesn't come\x01",
            "as a huge surprise.\x02\x03",

            "#269FSuuure you don't wanna think it over\x01",
            "a little more, though?\x02\x03",

            "No matter how hard you try, Estelle,\x01",
            "you'll never stop Ouroboros.\x02\x03",

            "Joshua should know that best of all,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#1043F#5PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#265F#6PBesides, if you join the society,\x01",
            "we can make you even stronger!\x02\x03",

            "You could be an Enforcer like me,\x01",
            "you know?\x02\x03",

            "#261FHeeehee! Wouldn't that be neat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015F#5PHmm. I'll admit the idea of becoming\x01",
            "stronger is tempting. But...\x02\x03",

            "#1007FBut it wouldn't be real strength.\x02\x03",

            "Not to me, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "#264F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1006F#5PI want to become stronger.\x02\x03",

            "Strong enough to protect those\x01",
            "important to me, like my mom.\x02\x03",

            "Strong enough to protect MYSELF,\x01",
            "so this guy over here can stop fretting\x01",
            "over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1044F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1007F#5PIf I join the society, though, I'd cease\x01",
            "to be...me.\x02\x03",

            "I might get stronger, sure. Maybe\x01",
            "a LOT stronger. But it wouldn't be as\x01",
            "who I really am.\x02\x03",

            "#1025FI just don't think there'd be any point.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #32
        0x8,
        (
            "#262F#6P...I don't understand. At all.\x02\x03",

            "Estelle, what you're saying doesn't\x01",
            "make any sense.\x02\x03",

            "'Who you really are'?\x01",
            "What's that supposed to mean?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x0, 0x0, 0x17DE, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #33
        0x101,
        (
            "#1025F#5PRenne, I really like you.\x02\x03",

            "You act all grown up, you love pranks,\x01",
            "you're more sympathetic than I'd expect,\x01",
            "given the circumstances...\x02\x03",

            "#1016FYou deceived me on a lot of things,\x01",
            "but I can't bring myself to hate you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#264F#6PUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1003F#5PBut that's why.\x02\x03",

            "#1007FThat's why I don't want you to be\x01",
            "in the society.\x02\x03",

            "#1002FIf you were an adult, choosing of\x01",
            "your own free will, I could respect\x01",
            "that, at least.\x02\x03",

            "But what they've done to you.\x01",
            "What they're DOING to you.\x01",
            "It's fundamentally wrong.\x02\x03",

            "#1003FIf you grow into an adult the way\x01",
            "you are now, you'll never, ever be\x01",
            "able to turn back.\x02\x03",

            "So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#1300F#6P...\x02\x03",

            "#266FI've changed my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1004F#5PEh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#1042F#5PNo!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    Sleep(100)
    Fade(500)
    OP_6D(250, 0, 7960, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(1230, 0)
    OP_6C(32000, 0)
    OP_6E(609, 0)
    OP_8C(0x101, 0, 0)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_1E9F():
        OP_6B(1100, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E9F)

    def lambda_1EAF():
        OP_96(0xFE, 0xFFFFFE5C, 0x1F4, 0x1FCC, 0x4B0, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EAF)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    OP_8C(0x8, 225, 0)

    def lambda_1EE8():
        OP_99(0xFE, 0x1, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1EE8)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    SetChrSubChip(0x102, 2)
    SetChrChipByIndex(0x102, 7)

    def lambda_1F0A():
        OP_96(0x102, 0xFFFFFEC0, 0x0, 0x19FA, 0x1F4, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F0A)
    Sleep(100)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_1F32():
        OP_99(0xFE, 0x5, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F32)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x1, 0xFF, 0x102, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x9B, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_1FA1():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1FA1)

    def lambda_1FBB():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1FBB)

    def lambda_1FD5():
        OP_96(0xFE, 0x258, 0x0, 0x26F2, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FD5)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)

    def lambda_1FFD():
        OP_8F(0xFE, 0xFFFFFC7C, 0x0, 0x14E6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FFD)

    def lambda_2018():
        OP_8F(0xFE, 0x96, 0x0, 0x170C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2018)

    def lambda_2033():
        OP_6B(1330, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2033)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x4)
    WaitChrThread(0x102, 0x1)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #39
        0x101,
        "#1020F#2PRenne!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_2094():
        OP_96(0xFE, 0x3F2, 0x3B6, 0x2F94, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2094)
    OP_8C(0x8, 180, 0)
    Fade(500)
    OP_6D(390, 950, 9200, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(8000, 0)
    OP_6E(357, 0)
    WaitChrThread(0x8, 0x1)
    OP_22(0x1F9, 0x0, 0x64)
    OP_99(0x8, 0x7, 0xD, 0x5DC)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    Sleep(500)

    ChrTalk(    #40
        0x8,
        (
            "#1305F#6PHeheh. Now that's the Joshua\x01",
            "I remember.\x02\x03",

            "Quick reflexes.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x102, 0x8, 0xC, 0x7D0)
    Sleep(500)

    ChrTalk(    #41
        0x102,
        (
            "#1035F#5PThat wasn't too bad either.\x02\x03",

            "#1042FThey didn't call you the 'Angel of Slaughter'\x01",
            "for nothing, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#263F#6PYes. That's right.\x01",
            "The Angel of Slaughter is strong.\x02\x03",

            "Much stronger and more useful than\x01",
            "the Black Fang who can only bite from\x01",
            "the shadows.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #43
        0x101,
        (
            "#1020F#5PWh-Wh-What the hell?!\x01",
            "What was that for?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#1306F#6PHeehee. I said I've changed my mind.\x02\x03",

            "#261FIf you won't be my ally, Estelle,\x01",
            "I'll gut you like a fish after all.\x02\x03",

            "Joshua, too. And everyone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        (
            "#1019F#5PGuh... One of the first things my dad\x01",
            "ever taught me was that gutting fish is\x01",
            "for grown-ups.\x02\x03",

            "#1005FOkay, I've had enough! Missy, you have\x01",
            "earned yourself a hell of a lot of spankings!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #46
        0x102,
        (
            "#1042F#5PEstelle, calm down!\x01",
            "We can't underestimate--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1005F#5PNO, Joshua!\x01",
            "She needs to be taught a lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#263F#6PHeh heh. You're so naive.\x02\x03",

            "I liked that part of you, Estelle.\x01",
            "But now...\x02\x03",

            "#1302FNow I HATE it. I HATE you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2559():
        OP_6D(470, 0, 7210, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2559)

    def lambda_2571():
        OP_67(0, 5260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2571)

    def lambda_2589():
        OP_6B(3340, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2589)

    def lambda_2599():
        OP_6C(25000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2599)

    def lambda_25A9():
        OP_6E(301, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_25A9)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 6)
    Sleep(1000)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    SetChrPos(0x9, -2140, 1250, 9460, 135)
    SetChrPos(0xA, 3240, 1250, 8880, 225)
    SetChrPos(0xB, 5080, 1250, 4410, 270)
    SetChrPos(0xC, 440, 1000, -330, 0)
    SetChrPos(0xD, -5680, 1250, 1470, 45)
    SetChrPos(0xE, -5200, 1250, 5190, 90)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_26E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26E0)

    def lambda_26F2():
        OP_8F(0xFE, 0xFFFFF7A4, 0xFA, 0x24F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26F2)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_271C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_271C)

    def lambda_272E():
        OP_8F(0xFE, 0xCA8, 0xFA, 0x22B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_272E)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_2758():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2758)

    def lambda_276A():
        OP_8F(0xFE, 0x13D8, 0xFA, 0x113A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_276A)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_2794():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2794)

    def lambda_27A6():
        OP_8F(0xFE, 0x1B8, 0x0, 0xFFFFFEB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_27A6)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_27D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27D0)

    def lambda_27E2():
        OP_8F(0xFE, 0xFFFFE9D0, 0xFA, 0x5BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_27E2)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_280C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_280C)

    def lambda_281E():
        OP_8F(0xFE, 0xFFFFEBB0, 0xFA, 0x1446, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_281E)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288D")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CB")

    label("loc_288D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B4")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CB")

    label("loc_28B4")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_28CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F2")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2930")

    label("loc_28F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2919")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2930")

    label("loc_2919")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2930")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    OP_0D()

    def lambda_295A():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_295A)

    def lambda_2968():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2968)
    OP_8C(0xF8, 90, 600)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #49
        0x8,
        (
            "#263F#6PI am the Angel of Slaughter.\x02\x03",

            "#1304FAnd now, it's time to be an angel\x01",
            "and slaughter you. DIE.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29F2():
        OP_6D(600, 0, 6760, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29F2)

    def lambda_2A0A():
        OP_6B(2500, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A0A)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 2)

    def lambda_2A29():
        OP_96(0xFE, 0x28, 0x0, 0x19B4, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A29)
    Sleep(50)
    SetChrChipByIndex(0x9, 12)

    def lambda_2A51():
        OP_8F(0xFE, 0xFFFFFC36, 0x0, 0x1AD6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A51)
    SetChrChipByIndex(0xA, 12)

    def lambda_2A71():
        OP_8F(0xFE, 0x460, 0x0, 0x19DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A71)
    SetChrChipByIndex(0xB, 12)

    def lambda_2A91():
        OP_8F(0xFE, 0x712, 0x0, 0x11BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A91)
    SetChrChipByIndex(0xC, 12)

    def lambda_2AB1():
        OP_8F(0xFE, 0x0, 0x0, 0x96A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2AB1)
    SetChrChipByIndex(0xD, 12)

    def lambda_2AD1():
        OP_8F(0xFE, 0xFFFFF8D0, 0x0, 0xD66, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2AD1)
    SetChrChipByIndex(0xE, 12)

    def lambda_2AF1():
        OP_8F(0xFE, 0xFFFFF876, 0x0, 0x13D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2AF1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    Battle(0x3FD, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2B40"),
        (SWITCH_DEFAULT, "loc_2B45"),
    )


    label("loc_2B40")

    OP_B4(0x0)
    Jump("loc_2B45")

    label("loc_2B45")

    Return()

    # Function_6_924 end

    def Function_7_2B46(): pass

    label("Function_7_2B46")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x9, 0x4)
    Call(0, 11)
    OP_D2(0x270246, 0x270250, 0xA)
    OP_D2(0x270244, 0x27024E, 0xB)
    OP_D2(0x27023F, 0x270249, 0xD)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_70(0x5, 0x8)
    OP_70(0x6, 0x8)
    OP_70(0x7, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, 600, 0, 4500, 0)
    SetChrPos(0x102, -600, 0, 3600, 0)
    SetChrPos(0xF8, 1300, 0, 3200, 0)
    SetChrPos(0xF9, 0, 0, 2200, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0xF8, 1)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 1)
    SetChrChipByIndex(0xF9, 9)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1220, 950, 12420, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    OP_6D(400, 950, 9010, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(4000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x8,
        (
            "#264F#6PYou actually broke all my toys.\x02\x03",

            "#1305FHeheh. You really aren't bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1019F#5PE-Enough of this, damn it!\x02\x03",

            "#1005FDo you really enjoy this?!\x01",
            "Is this really all you can think about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#263F#6PHee-hee-heh-heh. Of course.\x02\x03",

            "#1306FI love looking down on people's suffering.\x02\x03",

            "It lifts me up. Fills my chest. Makes me\x01",
            "happy.\x02\x03",

            "#261FI love hearing people scream in agony.\x02\x03",

            "It helps me sleep like the angel I am\x01",
            "at night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1020F#5PN-N-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#1043F#5PSo you're still--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "#1302F#6PSILENCE, FANG.\x02",
    )

    CloseMessageWindow()

    def lambda_2F65():
        OP_6B(3800, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F65)
    Sleep(500)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #56
        0x8,
        (
            "#1305F#6PHey. Estelle.\x01",
            "I've got a fairy tale of my own, you know.\x02\x03",

            "A long time ago in a land far, far away,\x01",
            "a little girl named Renne had a fake mama\x01",
            "and papa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1026F#5PA what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#263F#6PA fake mama and papa.\x02\x03",

            "#260FRenne loved them a lot, but one day, they\x01",
            "said they had a problem and had to go away\x01",
            "for a while.\x02\x03",

            "They gave Renne away to other grown-ups\x01",
            "who were very bad people.\x02\x03",

            "#261FThey were crying when they gave Renne away.\x01",
            "They said, 'We'll come back for you, sweetie!'\x01",
            "over and over. But they never did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1026F#5PBut what--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#268F#6PAfter Renne was given away to those people,\x01",
            "she was made to do many unpleasant things.\x02\x03",

            "Renne got used to most of it...but she never\x01",
            "got used to being hurt.\x02\x03",

            "#1300FThere were other kids the same age there,\x01",
            "too, but most of them got sick and died.\x02\x03",

            "#1305FThat went on for about half a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1022F#5PTh-This can't be...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3317")

    ChrTalk(    #62
        0x107,
        "#065FHow awful...\x02",
    )

    CloseMessageWindow()

    label("loc_3317")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3334")

    ChrTalk(    #63
        0x109,
        "#1067F...\x02",
    )

    CloseMessageWindow()

    label("loc_3334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_335F")

    ChrTalk(    #64
        0x106,
        "#057FSons of bitches...\x02",
    )

    CloseMessageWindow()

    label("loc_335F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3387")

    ChrTalk(    #65
        0x103,
        "#522FHow terrible...\x02",
    )

    CloseMessageWindow()

    label("loc_3387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A5")

    ChrTalk(    #66
        0x105,
        "#049FNo...\x02",
    )

    CloseMessageWindow()

    label("loc_33A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C8")

    ChrTalk(    #67
        0x108,
        "#077FInhuman...\x02",
    )

    CloseMessageWindow()

    label("loc_33C8")


    ChrTalk(    #68
        0x8,
        (
            "#265F#6PIn the end, 'Mama' and 'Papa' were fake.\x02\x03",

            "If they were a real mama and papa,\x01",
            "they would have come for Renne when\x01",
            "she got hurt.\x02\x03",

            "#261FRight, Estelle? That's how your papa\x01",
            "and mama act, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1027F#5PI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#263F#6PAww, don't be sad. It all ended up\x01",
            "okay.\x02\x03",

            "#1305FJoshua and Loewe came for Renne\x01",
            "instead.\x02\x03",

            "They slaughtered all the bad grown-ups.\x01",
            "Stabbed them, burned them.\x01",
            "It was wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1026F#5PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1043F#5PThe society occasionally finds cause\x01",
            "to crush 'lesser' criminal organizations.\x02\x03",

            "Mostly for the purpose of absorbing their\x01",
            "resources into Ouroboros itself.\x02\x03",

            "#1035FWe found her during one such mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1026F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#263F#6PThey brought Renne home.\x01",
            "Home to Ouroboros. Renne learned\x01",
            "so much when she came home.\x02\x03",

            "#260FJoshua taught her to be sneaky.\x01",
            "Loewe taught her to fight and kill.\x02\x03",

            "She learned all sorts of other\x01",
            "things from everyone else, too.\x02\x03",

            "#265FAnd the nice people at the Thirteen\x01",
            "Factories taught her how to be friends\x01",
            "with dolls, just like Pedro.\x02\x03",

            "#261FAnd that's when she met her REAL\x01",
            "papa and mama in one!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 11)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(500)

    def lambda_3843():

        label("loc_3843")

        OP_7C(0x0, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_3843")

    QueueWorkItem2(0x10, 3, lambda_3843)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    OP_22(0x113, 0x0, 0x46)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 10580, 14000, 9330, 225)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 201)
    OP_70(0x0, 0xDC)
    Sleep(500)
    OP_72(0x0, 0x4)
    Sleep(500)
    Fade(500)
    OP_6D(10320, 10980, 5440, 0)
    OP_67(0, -3080, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(359000, 0)
    OP_6E(390, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 1200, 0, 1600, 45)
    SetChrPos(0x102, 600, 0, 2100, 45)
    SetChrPos(0xF8, 800, 0, 300, 45)
    SetChrPos(0xF9, -750, 0, 1800, 45)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x1)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_24(0x113, 0x50)

    def lambda_39DC():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_39DC)
    Sleep(100)
    OP_24(0x113, 0x5A)

    def lambda_3A00():
        OP_6D(10350, 5820, 6780, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A00)

    def lambda_3A18():
        OP_67(0, 6200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A18)

    def lambda_3A30():
        OP_6B(2320, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A30)

    def lambda_3A40():
        OP_6E(390, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A40)
    Play3DEffect(0x2, 0x0, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFD44, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x2, 0x1, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFD44, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)

    def lambda_3ABA():
        OP_8F(0xFE, 0x2954, 0x3E8, 0x2472, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3ABA)
    Sleep(100)
    OP_24(0x113, 0x64)

    def lambda_3ADE():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3ADE)
    Sleep(100)

    def lambda_3AFE():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AFE)
    Sleep(4000)
    Fade(500)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)
    PlayEffect(0x1, 0x2, 0x10, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)

    def lambda_3B6B():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B6B)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_72(0x0, 0x20)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_23(0x113)
    Fade(500)
    OP_6D(10600, 250, 14510, 0)
    OP_67(0, 4040, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(35000, 0)
    OP_6E(227, 0)
    OP_6F(0x0, 221)
    OP_70(0x0, 0xF0)
    OP_7C(0x0, 0x12C, 0x1388, 0x3E8)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)
    OP_D8(0x0, 0x1F4)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1500)
    Sleep(500)

    ChrTalk(    #75
        0x101,
        "#1020F#5PGyah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C92")

    ChrTalk(    #76
        0x109,
        "#1069F#5PIt's that huge friggin' archaism!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D9B")

    label("loc_3C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CD0")

    ChrTalk(    #77
        0x106,
        "#054F#5PIt's that huge archaism weapon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D9B")

    label("loc_3CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D0C")

    ChrTalk(    #78
        0x107,
        "#065F#5PAah! It's that huge archaism!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D9B")

    label("loc_3D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D51")

    ChrTalk(    #79
        0x103,
        "#024F#5PIt's that giant archaism from Grancel!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D9B")

    label("loc_3D51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D9B")

    ChrTalk(    #80
        0x105,
        "#042F#5PIt's that enormous archaism we saw in Grancel!\x02",
    )

    CloseMessageWindow()

    label("loc_3D9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE1")

    ChrTalk(    #81
        0x108,
        "#077F#5PIt's about to attack, so on your guard!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EDB")

    label("loc_3DE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E1F")

    ChrTalk(    #82
        0x105,
        "#042F#5PCan we really fight that thing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EDB")

    label("loc_3E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E5A")

    ChrTalk(    #83
        0x103,
        "#523F#5PI hope we can fend it off...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EDB")

    label("loc_3E5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E98")

    ChrTalk(    #84
        0x107,
        "#065F#5PI-I think it's gonna attack us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EDB")

    label("loc_3E98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EDB")

    ChrTalk(    #85
        0x106,
        "#054F#5PAw, hell! Get ready, it's gonna attack!\x02",
    )

    CloseMessageWindow()

    label("loc_3EDB")


    ChrTalk(    #86
        0x102,
        (
            "#1046F#5PThat's a Gordias-class tactical archaism!\x01",
            "The Pater-Mater! \x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 13)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3F44():
        OP_6D(10070, 250, 13790, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F44)
    OP_96(0x8, 0xFE6, 0xE10, 0x1BB2, 0xFA0, 0x1F40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0x8, 0x10)
    OP_8C(0x8, 225, 400)
    ClearChrFlags(0x8, 0x10)
    Sleep(500)

    ChrTalk(    #87
        0x8,
        (
            "#1306F#6PA kid like me being in the society is\x01",
            "wrong, you say?\x02\x03",

            "If I become an adult the way I am now,\x01",
            "I'll never be able to go back, you say?\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x20)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_22(0x115, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    Sleep(500)

    def lambda_4068():
        OP_6D(12860, 250, 16720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4068)

    def lambda_4080():
        OP_67(0, 3800, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4080)

    def lambda_4098():
        OP_6B(5000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4098)

    def lambda_40A8():
        OP_6C(35000, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40A8)

    def lambda_40B8():
        OP_6E(227, 1000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_40B8)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 13)

    def lambda_40D7():
        OP_99(0xFE, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_40D7)
    OP_96(0x8, 0x1C98, 0xC80, 0x2774, 0x9C4, 0x1F40)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 6)
    SetChrChipByIndex(0x8, 3)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #88
        0x8,
        (
            "#1301F#6PLies! LIES!!!\x02\x03",

            "I only met my real papa and mama\x01",
            "after the society took me in!\x02\x03",

            "I became the happiest girl in the world!\x01",
            "I got my happy ending!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1002F#5PRenne, Renne, listen to--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#263F#6PIf you deny that, Estelle...then you're\x01",
            "my worst enemy.\x02\x03",

            "#1304FI'll enjoy your screams as Pater-Mater\x01",
            "crushes you into paste. Die. DIE, DIE!!!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Battle(0x453, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_42BB"),
        (SWITCH_DEFAULT, "loc_42C0"),
    )


    label("loc_42BB")

    OP_B4(0x0)
    Jump("loc_42C0")

    label("loc_42C0")

    Return()

    # Function_7_2B46 end

    def Function_8_42C1(): pass

    label("Function_8_42C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x9, 0x4)
    Call(0, 11)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_70(0x5, 0x8)
    OP_70(0x6, 0x8)
    OP_70(0x7, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x0, 0x4)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 10580, 500, 9330, 225)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x1)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, 1200, 0, 1200, 45)
    SetChrPos(0x102, 870, 0, 2560, 45)
    SetChrPos(0xF8, -50, 0, 110, 45)
    SetChrPos(0xF9, -450, 0, 1740, 45)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1220, 950, 12420, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 7)
    SetChrChipByIndex(0x8, 3)
    ClearChrFlags(0x8, 0x1)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_6D(4920, 2480, 5190, 0)
    OP_67(0, 3420, -10000, 0)
    OP_6B(4470, 0)
    OP_6C(15000, 0)
    OP_6E(243, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4599")

    ChrTalk(    #91
        0x109,
        (
            "#1070FGuh... It's like fighting a boulder!\x01",
            "A boulder with GUNS!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4687")

    label("loc_4599")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45DF")

    ChrTalk(    #92
        0x106,
        (
            "#057FGrh... Might as well be hackin'\x01",
            "at a rock!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4687")

    label("loc_45DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4609")

    ChrTalk(    #93
        0x107,
        "#561FIt's so tough!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4687")

    label("loc_4609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4652")

    ChrTalk(    #94
        0x103,
        (
            "#523FUgh, this is like trying to fight\x01",
            "a mountain!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4687")

    label("loc_4652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4687")

    ChrTalk(    #95
        0x105,
        "#043FIt's practically invincible!\x02",
    )

    CloseMessageWindow()

    label("loc_4687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46E2")

    ChrTalk(    #96
        0x108,
        (
            "#077FIt's even more powerful than the\x01",
            "archaism in the Grancel ruins!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486B")

    label("loc_46E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4746")

    ChrTalk(    #97
        0x105,
        (
            "#043FIt's even more powerful than the one\x01",
            "we fought beneath Grancel Castle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486B")

    label("loc_4746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_479E")

    ChrTalk(    #98
        0x103,
        (
            "#523FIt's even stronger than the thing we\x01",
            "fought beneath Grancel!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486B")

    label("loc_479E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_480A")

    ChrTalk(    #99
        0x107,
        (
            "#065FIt's got even more armor and power\x01",
            "than the archaism we fought under\x01",
            "the castle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486B")

    label("loc_480A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_486B")

    ChrTalk(    #100
        0x106,
        (
            "#057FIt's even stronger than that thing we\x01",
            "found beneath Grancel. How the...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486B")


    ChrTalk(    #101
        0x8,
        (
            "#1302F#4PHow are you still not DEAD?\x02\x03",

            "#263FFine. I'm bored now.\x02\x03",

            "#1304FPater-Mater! Full output!\x01",
            "BURN ESTELL--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_1F(0x5A, 0x7D0)
    Fade(500)
    OP_6B(4270, 0)
    OP_82(0x0, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49D0")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4A0E")

    label("loc_49D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F7")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4A0E")

    label("loc_49F7")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4A0E")

    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A72")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4AB0")

    label("loc_4A72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A99")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4AB0")

    label("loc_4A99")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4AB0")

    Sleep(1000)

    def lambda_4ABB():
        OP_6D(2470, 950, 15540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4ABB)

    def lambda_4AD3():
        OP_67(0, 3980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AD3)

    def lambda_4AEB():
        OP_6B(4400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AEB)
    WaitChrThread(0x101, 0x0)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    Sleep(500)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    Sleep(100)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3C)
    Sleep(100)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    Sleep(100)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x3C)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_4B87():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B87)

    def lambda_4B95():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B95)
    Sleep(100)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)

    def lambda_4BBC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4BBC)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #102
        0x8,
        "#264F#8PHuh...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1F(0x64, 0x7D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_4C34():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4C34)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1707   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_42C1 end

    def Function_9_4CBA(): pass

    label("Function_9_4CBA")

    OP_96(0xFE, 0x258, 0x0, 0x26F2, 0x1F4, 0x2710)
    OP_96(0xFE, 0x3F2, 0x3B6, 0x2F94, 0x5DC, 0x2710)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x4)
    Return()

    # Function_9_4CBA end

    def Function_10_4CF3(): pass

    label("Function_10_4CF3")

    OP_96(0xFE, 0x1CC, 0x0, 0x1BB2, 0x3E8, 0x2EE0)
    OP_96(0xFE, 0x2E4, 0x0, 0x198C, 0x3E8, 0x2EE0)
    Return()

    # Function_10_4CF3 end

    def Function_11_4D22(): pass

    label("Function_11_4D22")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_4D43"),
        (5, "loc_4D50"),
        (4, "loc_4D5D"),
        (6, "loc_4D6A"),
        (7, "loc_4D77"),
        (8, "loc_4D84"),
        (SWITCH_DEFAULT, "loc_4D91"),
    )


    label("loc_4D43")

    OP_D2(0x701D0, 0x701DC, 0x8)
    Jump("loc_4D91")

    label("loc_4D50")

    OP_D2(0x70218, 0x70224, 0x8)
    Jump("loc_4D91")

    label("loc_4D5D")

    OP_D2(0x70200, 0x7020C, 0x8)
    Jump("loc_4D91")

    label("loc_4D6A")

    OP_D2(0x70230, 0x7023C, 0x8)
    Jump("loc_4D91")

    label("loc_4D77")

    OP_D2(0x70248, 0x70254, 0x8)
    Jump("loc_4D91")

    label("loc_4D84")

    OP_D2(0x270176, 0x270183, 0x8)
    Jump("loc_4D91")

    label("loc_4D91")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_4DB2"),
        (5, "loc_4DBF"),
        (4, "loc_4DCC"),
        (6, "loc_4DD9"),
        (7, "loc_4DE6"),
        (8, "loc_4DF3"),
        (SWITCH_DEFAULT, "loc_4E00"),
    )


    label("loc_4DB2")

    OP_D2(0x701D0, 0x701DC, 0x9)
    Jump("loc_4E00")

    label("loc_4DBF")

    OP_D2(0x70218, 0x70224, 0x9)
    Jump("loc_4E00")

    label("loc_4DCC")

    OP_D2(0x70200, 0x7020C, 0x9)
    Jump("loc_4E00")

    label("loc_4DD9")

    OP_D2(0x70230, 0x7023C, 0x9)
    Jump("loc_4E00")

    label("loc_4DE6")

    OP_D2(0x70248, 0x70254, 0x9)
    Jump("loc_4E00")

    label("loc_4DF3")

    OP_D2(0x270176, 0x270183, 0x9)
    Jump("loc_4E00")

    label("loc_4E00")

    Return()

    # Function_11_4D22 end

    def Function_12_4E01(): pass

    label("Function_12_4E01")

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
        (0, "loc_4E7A"),
        (1, "loc_4E80"),
        (SWITCH_DEFAULT, "loc_4E86"),
    )


    label("loc_4E7A")

    OP_A2(0x1200)
    Jump("loc_4E86")

    label("loc_4E80")

    OP_A2(0x1201)
    Jump("loc_4E86")

    label("loc_4E86")

    Return()

    # Function_12_4E01 end

    def Function_13_4E87(): pass

    label("Function_13_4E87")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_13_4E87 end

    SaveToFile()

Try(main)
