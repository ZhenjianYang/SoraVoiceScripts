from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0811   ._SN',
        MapName             = 'Event',
        Location            = 'E0811.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Merkabah',                             # 9
        'Arseille',                             # 10
        'Estelle',                              # 11
        'Pater-Mater',                          # 12
        'Renne',                                # 13
        'Dummy Camera',                         # 14
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
        'ED6_DT27/CH03510 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
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
        NpcIndex            = 0x1CC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_24F",          # 01, 1
        "Function_2_255",          # 02, 2
        "Function_3_7D1",          # 03, 3
        "Function_4_7ED",          # 04, 4
        "Function_5_80D",          # 05, 5
        "Function_6_866",          # 06, 6
        "Function_7_A93",          # 07, 7
        "Function_8_AAA",          # 08, 8
        "Function_9_1024",         # 09, 9
        "Function_10_10A8",        # 0A, 10
        "Function_11_10D2",        # 0B, 11
        "Function_12_122E",        # 0C, 12
        "Function_13_168F",        # 0D, 13
        "Function_14_16EC",        # 0E, 14
        "Function_15_1AD2",        # 0F, 15
        "Function_16_1C93",        # 10, 16
        "Function_17_1D42",        # 11, 17
        "Function_18_2197",        # 12, 18
        "Function_19_21F0",        # 13, 19
        "Function_20_2249",        # 14, 20
        "Function_21_22A2",        # 15, 21
        "Function_22_2600",        # 16, 22
        "Function_23_2659",        # 17, 23
        "Function_24_2ABD",        # 18, 24
        "Function_25_2C83",        # 19, 25
        "Function_26_2F7A",        # 1A, 26
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_19A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1C2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_1C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1EA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_204")
    OP_A3(0x2508)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_24E")

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_21E")
    OP_A3(0x2507)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)
    Jump("loc_24E")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_22F")
    OP_A3(0x2506)
    Event(0, 8)
    Jump("loc_24E")

    label("loc_22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_240")
    OP_A3(0x2505)
    Event(0, 6)
    Jump("loc_24E")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24E")
    OP_A3(0x2504)
    Event(0, 2)

    label("loc_24E")

    Return()

    # Function_0_172 end

    def Function_1_24F(): pass

    label("Function_1_24F")

    OP_22(0x1C3, 0x0, 0x64)
    Return()

    # Function_1_24F end

    def Function_2_255(): pass

    label("Function_2_255")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    OP_A1(0x10, 0x1)
    SetChrPos(0x10, 6790, 0, -37700, 0)
    ClearChrFlags(0x10, 0x100)
    OP_D1(16, 0, 0, 0, 0)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x3C)
    OP_E5(0x0, 0x1, 0x0, 262144)
    OP_E5(0x0, 0x1, 0x1, 262144)
    OP_E5(0x0, 0x1, 0x2, 262144)
    OP_E5(0x0, 0x1, 0x3, 262144)
    OP_E5(0x0, 0x1, 0x4, 262144)
    OP_E5(0x0, 0x1, 0x5, 262144)
    OP_E5(0x0, 0x1, 0x6, 262144)
    OP_E5(0x0, 0x1, 0x7, 262144)
    OP_E5(0x0, 0x1, 0x8, 262144)
    OP_E5(0x0, 0x1, 0x9, 262144)
    OP_E5(0x0, 0x1, 0xA, 262144)
    OP_E5(0x0, 0x1, 0xB, 262144)
    OP_E5(0x0, 0x1, 0xC, 262144)
    OP_E5(0x0, 0x1, 0xD, 262144)
    OP_E5(0x0, 0x1, 0xE, 262144)
    OP_E5(0x0, 0x1, 0xF, 262144)
    OP_E5(0x0, 0x1, 0x10, 262144)
    OP_E5(0x0, 0x1, 0x11, 262144)
    OP_E5(0x0, 0x1, 0x12, 262144)
    OP_E5(0x0, 0x1, 0x14, 262144)
    OP_E5(0x0, 0x1, 0x15, 262144)
    OP_E5(0x0, 0x1, 0x16, 262144)
    OP_E5(0x0, 0x1, 0x17, 262144)
    OP_E5(0x0, 0x1, 0x18, 262144)
    OP_E5(0x0, 0x1, 0x19, 262144)
    OP_E5(0x0, 0x1, 0x1A, 262144)
    OP_E5(0x0, 0x1, 0x1B, 262144)
    OP_E5(0x0, 0x1, 0x1C, 262144)
    OP_E5(0x0, 0x1, 0x1D, 262144)
    OP_E5(0x0, 0x1, 0x1E, 262144)
    OP_E5(0x0, 0x1, 0x1F, 262144)
    OP_E5(0x0, 0x1, 0x20, 262144)
    OP_E5(0x2, 0x1, 0x0, 100)
    OP_E5(0x2, 0x1, 0x1, 100)
    OP_E5(0x2, 0x1, 0x2, 100)
    OP_E5(0x2, 0x1, 0x3, 100)
    OP_E5(0x2, 0x1, 0x4, 100)
    OP_E5(0x2, 0x1, 0x5, 100)
    OP_E5(0x2, 0x1, 0x6, 100)
    OP_E5(0x2, 0x1, 0x7, 100)
    OP_E5(0x2, 0x1, 0x8, 100)
    OP_E5(0x2, 0x1, 0x9, 100)
    OP_E5(0x2, 0x1, 0xA, 100)
    OP_E5(0x2, 0x1, 0xB, 100)
    OP_E5(0x2, 0x1, 0xC, 100)
    OP_E5(0x2, 0x1, 0xD, 100)
    OP_E5(0x2, 0x1, 0xE, 100)
    OP_E5(0x2, 0x1, 0xF, 100)
    OP_E5(0x2, 0x1, 0x10, 100)
    OP_E5(0x2, 0x1, 0x11, 100)
    OP_E5(0x2, 0x1, 0x12, 100)
    OP_E5(0x2, 0x1, 0x14, 100)
    OP_E5(0x2, 0x1, 0x15, 100)
    OP_E5(0x2, 0x1, 0x16, 100)
    OP_E5(0x2, 0x1, 0x17, 100)
    OP_E5(0x2, 0x1, 0x18, 100)
    OP_E5(0x2, 0x1, 0x19, 100)
    OP_E5(0x2, 0x1, 0x1A, 100)
    OP_E5(0x2, 0x1, 0x1B, 100)
    OP_E5(0x2, 0x1, 0x1C, 100)
    OP_E5(0x2, 0x1, 0x1D, 100)
    OP_E5(0x2, 0x1, 0x1E, 100)
    OP_E5(0x2, 0x1, 0x1F, 100)
    OP_E5(0x2, 0x1, 0x20, 100)
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 180, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 180, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 180, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    OP_22(0x2D5, 0x1, 0x3C)
    StopSound(0x249F0, 0x75300, 0x0)
    OP_6D(5440, 24600, 108020, 0)
    OP_67(0, -8520, -10000, 0)
    OP_6B(6750, 0)
    OP_6C(320000, 0)
    OP_6E(607, 0)

    def lambda_5B4():
        OP_6D(5440, 25000, 108020, 10000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_5B4)

    def lambda_5CC():
        OP_67(0, -2500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5CC)

    def lambda_5E4():
        OP_6B(9860, 12000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5E4)

    def lambda_5F4():
        OP_6C(355000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_5F4)

    def lambda_604():
        OP_6E(846, 12000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_604)
    FadeToBright(2000, 0)

    def lambda_61D():
        OP_91(0xFE, 0x0, 0x13880, 0x7A120, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61D)
    OP_22(0x2D5, 0x1, 0x3C)
    OP_0D()
    OP_43(0x10, 0x2, 0x0, 0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Masked Person")

    AnonymousTalk(    #0 op#A op#5
        "\x07\x02#50AAfter all, I have only just awoken.\x07\x00\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(3000, 0, -1)
    Sleep(1000)
    OP_24(0x2D5, 0x5A)
    OP_24(0x1C3, 0x5A)
    Sleep(300)
    OP_24(0x2D5, 0x50)
    OP_24(0x1C3, 0x50)
    Sleep(300)
    OP_24(0x2D5, 0x46)
    OP_24(0x1C3, 0x46)
    Sleep(300)
    OP_24(0x2D5, 0x3C)
    OP_24(0x1C3, 0x3C)
    Sleep(300)
    OP_24(0x2D5, 0x32)
    OP_24(0x1C3, 0x32)
    Sleep(300)
    OP_24(0x2D5, 0x28)
    OP_24(0x1C3, 0x28)
    Sleep(300)
    OP_24(0x2D5, 0x1E)
    OP_24(0x1C3, 0x1E)
    Sleep(300)
    OP_24(0x2D5, 0x14)
    OP_24(0x1C3, 0x14)
    Sleep(300)
    OP_24(0x2D5, 0xA)
    OP_24(0x1C3, 0xA)
    Sleep(300)
    OP_24(0x2D5, 0x0)
    OP_24(0x1C3, 0x0)
    OP_23(0x2D5)
    OP_23(0x1C3)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    OP_44(0x15, 0x0)
    OP_44(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_44(0x15, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_20(0x0)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x10)
    OP_48()
    Sleep(500)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_3_op.avi", 0xC9, 0x0)

    label("loc_780")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79A")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_797")
    Jump("loc_79A")

    label("loc_797")

    Jump("loc_780")

    label("loc_79A")

    FadeToDark(2000, 0, -1)
    OP_20(0x7D0)
    OP_21()
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_255 end

    def Function_3_7D1(): pass

    label("Function_3_7D1")


    def lambda_7D7():
        OP_91(0xFE, 0x0, 0x13880, 0x7A120, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7D7)
    Return()

    # Function_3_7D1 end

    def Function_4_7ED(): pass

    label("Function_4_7ED")

    OP_24(0x2D5, 0x46)
    Sleep(200)
    OP_24(0x2D5, 0x50)
    Sleep(200)
    OP_24(0x2D5, 0x5A)
    Sleep(200)
    OP_24(0x2D5, 0x64)
    Return()

    # Function_4_7ED end

    def Function_5_80D(): pass

    label("Function_5_80D")

    OP_24(0x2D5, 0x5A)
    Sleep(300)
    OP_24(0x2D5, 0x50)
    Sleep(300)
    OP_24(0x2D5, 0x46)
    Sleep(300)
    OP_24(0x2D5, 0x3C)
    Sleep(300)
    OP_24(0x2D5, 0x32)
    Sleep(300)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x2D5, 0x14)
    Sleep(100)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x2D5, 0x0)
    OP_23(0x2D5)
    Return()

    # Function_5_80D end

    def Function_6_866(): pass

    label("Function_6_866")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    OP_A1(0x10, 0x1)
    SetChrPos(0x10, -38450, 40000, 63740, 270)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x3C)
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    OP_76(0x2, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_6D(60870, 50600, 40720, 0)
    OP_67(0, 5540, -10000, 0)
    OP_6B(9450, 0)
    OP_6C(315000, 0)
    OP_6E(302, 0)
    StopSound(0x249F0, 0x75300, 0x0)
    OP_22(0x2D5, 0x1, 0x3C)
    Sleep(2000)

    def lambda_9C9():
        OP_6D(-13500, 59600, 38500, 10000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_9C9)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    OP_43(0x10, 0x2, 0x0, 0x7)
    WaitChrThread(0xEE, 0x0)

    def lambda_9FC():
        OP_6B(5700, 12000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9FC)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x69, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS536._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(4000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    Sleep(1500)
    OP_43(0x10, 0x2, 0x0, 0x5)
    OP_0D()
    WaitChrThread(0x10, 0x2)
    OP_44(0x10, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_866 end

    def Function_7_A93(): pass

    label("Function_7_A93")

    OP_24(0x2D5, 0x46)
    Sleep(200)
    OP_24(0x2D5, 0x50)
    Sleep(200)
    OP_24(0x2D5, 0x5A)
    Return()

    # Function_7_A93 end

    def Function_8_AAA(): pass

    label("Function_8_AAA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    OP_A1(0x10, 0x1)
    SetChrPos(0x10, -38450, 30000, 63740, 270)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x3C)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x3C)
    OP_E5(0x0, 0x1, 0x0, 262144)
    OP_E5(0x0, 0x1, 0x1, 262144)
    OP_E5(0x0, 0x1, 0x2, 262144)
    OP_E5(0x0, 0x1, 0x3, 262144)
    OP_E5(0x0, 0x1, 0x4, 262144)
    OP_E5(0x0, 0x1, 0x5, 262144)
    OP_E5(0x0, 0x1, 0x6, 262144)
    OP_E5(0x0, 0x1, 0x7, 262144)
    OP_E5(0x0, 0x1, 0x8, 262144)
    OP_E5(0x0, 0x1, 0x9, 262144)
    OP_E5(0x0, 0x1, 0xA, 262144)
    OP_E5(0x0, 0x1, 0xB, 262144)
    OP_E5(0x0, 0x1, 0xC, 262144)
    OP_E5(0x0, 0x1, 0xD, 262144)
    OP_E5(0x0, 0x1, 0xE, 262144)
    OP_E5(0x0, 0x1, 0xF, 262144)
    OP_E5(0x0, 0x1, 0x10, 262144)
    OP_E5(0x0, 0x1, 0x11, 262144)
    OP_E5(0x0, 0x1, 0x12, 262144)
    OP_E5(0x0, 0x1, 0x14, 262144)
    OP_E5(0x0, 0x1, 0x15, 262144)
    OP_E5(0x0, 0x1, 0x16, 262144)
    OP_E5(0x0, 0x1, 0x17, 262144)
    OP_E5(0x0, 0x1, 0x18, 262144)
    OP_E5(0x0, 0x1, 0x19, 262144)
    OP_E5(0x0, 0x1, 0x1A, 262144)
    OP_E5(0x0, 0x1, 0x1B, 262144)
    OP_E5(0x0, 0x1, 0x1C, 262144)
    OP_E5(0x0, 0x1, 0x1D, 262144)
    OP_E5(0x0, 0x1, 0x1E, 262144)
    OP_E5(0x0, 0x1, 0x1F, 262144)
    OP_E5(0x0, 0x1, 0x20, 262144)
    OP_E5(0x2, 0x1, 0x0, 600)
    OP_E5(0x2, 0x1, 0x1, 600)
    OP_E5(0x2, 0x1, 0x2, 600)
    OP_E5(0x2, 0x1, 0x3, 600)
    OP_E5(0x2, 0x1, 0x4, 600)
    OP_E5(0x2, 0x1, 0x5, 600)
    OP_E5(0x2, 0x1, 0x6, 600)
    OP_E5(0x2, 0x1, 0x7, 600)
    OP_E5(0x2, 0x1, 0x8, 600)
    OP_E5(0x2, 0x1, 0x9, 300)
    OP_E5(0x2, 0x1, 0xA, 600)
    OP_E5(0x2, 0x1, 0xB, 600)
    OP_E5(0x2, 0x1, 0xC, 600)
    OP_E5(0x2, 0x1, 0xD, 600)
    OP_E5(0x2, 0x1, 0xE, 600)
    OP_E5(0x2, 0x1, 0xF, 600)
    OP_E5(0x2, 0x1, 0x10, 600)
    OP_E5(0x2, 0x1, 0x11, 600)
    OP_E5(0x2, 0x1, 0x12, 600)
    OP_E5(0x2, 0x1, 0x14, 600)
    OP_E5(0x2, 0x1, 0x15, 600)
    OP_E5(0x2, 0x1, 0x16, 600)
    OP_E5(0x2, 0x1, 0x17, 600)
    OP_E5(0x2, 0x1, 0x18, 600)
    OP_E5(0x2, 0x1, 0x19, 600)
    OP_E5(0x2, 0x1, 0x1A, 600)
    OP_E5(0x2, 0x1, 0x1B, 600)
    OP_E5(0x2, 0x1, 0x1C, 600)
    OP_E5(0x2, 0x1, 0x1D, 600)
    OP_E5(0x2, 0x1, 0x1E, 600)
    OP_E5(0x2, 0x1, 0x1F, 600)
    OP_E5(0x2, 0x1, 0x20, 600)
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    StopSound(0x249F0, 0x75300, 0x0)
    OP_6D(-37160, 30000, 60760, 0)
    OP_67(0, 7840, -10000, 0)
    OP_6B(9740, 0)
    OP_6C(121000, 0)
    OP_6E(438, 0)

    def lambda_DEC():
        OP_6D(-45900, 25000, 61100, 6000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_DEC)

    def lambda_E04():
        OP_67(0, 3700, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E04)

    def lambda_E1C():
        OP_6B(7000, 6000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E1C)

    def lambda_E2C():
        OP_6E(438, 6000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_E2C)

    def lambda_E3C():
        OP_6C(140000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_E3C)
    OP_22(0x2D5, 0x1, 0x64)
    OP_22(0x159, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_76(0x2, 0x0, 0x1, 0xFFFFFFF8, 0x0, 0x0, 0x0, 0x0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(1500)
    OP_44(0x15, 0x0)
    OP_44(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_44(0x15, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_76(0x2, 0x0, 0x1, 0xFFFFFFF3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_6D(-93300, 30000, 64430, 0)
    OP_67(0, 1410, -10000, 0)
    OP_6B(2600, 0)
    OP_F7(0x64, 0x1, 0x0)
    OP_6C(264000, 0)
    OP_6E(972, 0)
    SetChrPos(0x10, -38450, 28000, 59740, 270)

    def lambda_F51():
        OP_6D(-92560, 30000, 70000, 7000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_F51)

    def lambda_F69():
        OP_67(0, 590, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F69)

    def lambda_F81():
        OP_6B(8500, 7000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_F81)

    def lambda_F91():
        OP_6C(268000, 12000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_F91)

    def lambda_FA1():
        OP_6E(900, 7000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_FA1)
    OP_F7(0x64, 0x2, 0x0)
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_22(0x2D3, 0x0, 0x64)
    Sleep(2000)
    OP_43(0x10, 0x2, 0x0, 0x9)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    OP_43(0x10, 0x2, 0x0, 0x9)
    Sleep(3000)
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    OP_AD(0x2400E2, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0700   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_AAA end

    def Function_9_1024(): pass

    label("Function_9_1024")

    OP_24(0x2D5, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x2D5, 0x50)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x2D5, 0x46)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x2D5, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x2D5, 0x32)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x2D5, 0x28)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x2D5, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x2D5, 0x14)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x2D5, 0xA)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_24(0x2D5, 0x0)
    OP_24(0x77, 0x0)
    OP_23(0x2D5)
    OP_23(0x77)
    Return()

    # Function_9_1024 end

    def Function_10_10A8(): pass

    label("Function_10_10A8")

    OP_22(0x77, 0x1, 0x3C)
    Sleep(200)
    OP_24(0x77, 0x46)
    Sleep(200)
    OP_24(0x77, 0x50)
    Sleep(200)
    OP_24(0x77, 0x5A)
    Sleep(200)
    OP_24(0x77, 0x64)
    Return()

    # Function_10_10A8 end

    def Function_11_10D2(): pass

    label("Function_11_10D2")


    def lambda_10D8():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D8)
    Sleep(50)

    def lambda_10F8():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10F8)
    Sleep(50)

    def lambda_1118():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1118)
    Sleep(50)

    def lambda_1138():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1138)
    Sleep(50)

    def lambda_1158():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1158)
    Sleep(50)

    def lambda_1178():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1178)
    Sleep(50)

    def lambda_1198():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1198)
    Sleep(50)

    def lambda_11B8():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11B8)
    Sleep(50)

    def lambda_11D8():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11D8)
    Sleep(50)

    def lambda_11F8():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11F8)
    Sleep(50)

    def lambda_1218():
        OP_8F(0xFE, 0xFFFA31DE, 0x61A8, 0xF8FC, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1218)
    Return()

    # Function_11_10D2 end

    def Function_12_122E(): pass

    label("Function_12_122E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x1C3)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x11, 0x3)
    SetChrPos(0x11, -25640, 20480, -20000, 0)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\mp205_00.eff")
    LoadEffect(0x1, "map\\mp205_01.eff")
    LoadEffect(0x2, "map\\mp205_02.eff")
    LoadEffect(0x3, "map\\mp205_03.eff")
    LoadEffect(0x4, "map\\mp205_04.eff")
    LoadEffect(0x5, "map\\mp201_01.eff")
    LoadEffect(0x6, "map\\mp305_00.eff")
    PlayEffect(0x5, 0xFF, 0x11, 0, 1500, 16000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x11, 7300, -1600, 12000, 180, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x11, -7300, -1600, 12000, 180, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x5, 0x11, 0, 0, 40500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x0, 0xFF, -25640, 20480, 52840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6D(-24140, 23020, 80080, 0)
    OP_67(0, 1310, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(131000, 0)
    OP_6E(753, 0)

    def lambda_1450():
        OP_67(0, 5310, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1450)

    def lambda_1468():
        OP_6B(5000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1468)
    Sleep(1000)
    OP_22(0x125, 0x1, 0x64)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_1487():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x110D0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1487)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_14B0():

        label("loc_14B0")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_14B0")

    QueueWorkItem2(0xEF, 3, lambda_14B0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)
    Fade(250)
    OP_6D(-25170, 22960, -60000, 0)
    OP_67(0, 9880, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(41000, 0)
    OP_6E(800, 0)
    SetChrPos(0x11, -25640, 20480, -60000, 0)
    OP_43(0x11, 0x3, 0x0, 0xD)

    def lambda_153E():
        OP_67(0, 7880, -10000, 16000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_153E)

    def lambda_1556():
        OP_6B(4450, 16000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1556)
    OP_0D()
    Sleep(1000)
    Fade(2000)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -25640, 20480, 52840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(2000)
    Fade(2000)
    OP_82(0x1, 0x0)
    PlayEffect(0x2, 0x2, 0xFF, -25640, 20480, 52840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(2000)
    Fade(2000)
    OP_82(0x2, 0x0)
    PlayEffect(0x3, 0x3, 0xFF, -25640, 20480, 52840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(2000)
    Fade(2000)
    OP_82(0x3, 0x0)
    PlayEffect(0x4, 0x4, 0xFF, -25640, 20480, 52840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_122E end

    def Function_13_168F(): pass

    label("Function_13_168F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16EB")
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x1F4, 0x0)
    OP_91(0xFE, 0x3E8, 0x3E8, 0x0, 0x1F4, 0x0)
    OP_91(0xFE, 0x0, 0xFFFFFC18, 0x3E8, 0x1F4, 0x0)
    OP_91(0xFE, 0xFFFFFC18, 0xFFFFFC18, 0xFFFFFC18, 0x1F4, 0x0)
    Jump("Function_13_168F")

    label("loc_16EB")

    Return()

    # Function_13_168F end

    def Function_14_16EC(): pass

    label("Function_14_16EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x1C3)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x11, 0x3)
    SetChrPos(0x11, -25640, 20480, 302840, 0)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_6D(-25650, 22980, 318220, 0)
    OP_67(0, 5130, -10000, 0)
    OP_6B(5400, 0)
    OP_6C(143000, 0)
    OP_6E(700, 0)
    LoadEffect(0x4, "map\\mp205_04.eff")
    LoadEffect(0x5, "map\\mp201_01.eff")
    LoadEffect(0x6, "map\\mp305_00.eff")
    PlayEffect(0x5, 0x1, 0x11, 0, 1500, 16000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x11, 7300, -1600, 12000, 180, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x3, 0x11, -7300, -1600, 12000, 180, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x5, 0x11, 0, 0, 40500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x0, 0xFF, -25640, 20480, 52840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x125, 0x1, 0x64)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_18D1():
        OP_6B(4500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_18D1)
    ClearMapFlags(0x10)

    def lambda_18E6():

        label("loc_18E6")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_18E6")

    QueueWorkItem2(0xEF, 3, lambda_18E6)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    def lambda_1910():
        OP_6D(-25140, 22000, 323040, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1910)

    def lambda_1928():
        OP_67(0, -6000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1928)

    def lambda_1940():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1940)

    def lambda_1950():
        OP_6C(131000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1950)

    def lambda_1960():
        OP_6E(830, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1960)
    Sleep(500)
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_D8(0x3, 0x3E8)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x3, 601)
    OP_70(0x3, 0x384)
    Sleep(1500)
    OP_22(0x111, 0x0, 0x64)
    OP_73(0x3)
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 901)
    OP_70(0x3, 0x5DC)
    WaitChrThread(0xEE, 0x0)
    OP_22(0x159, 0x0, 0x64)
    Sleep(1000)

    def lambda_19C2():
        OP_6D(-24410, 22000, 329530, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_19C2)

    def lambda_19DA():
        OP_67(0, 110, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_19DA)

    def lambda_19F2():
        OP_6B(2300, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_19F2)

    def lambda_1A02():
        OP_6C(83000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1A02)

    def lambda_1A12():
        OP_6E(1540, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1A12)
    OP_43(0x11, 0x0, 0x0, 0xF)
    Sleep(3000)
    OP_43(0xF1, 0x0, 0x0, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_84(0x4)
    OP_84(0x5)
    OP_84(0x6)
    OP_44(0x11, 0x0)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_C4(0x0, 0x10)
    OP_48()
    Sleep(1)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_dt48.dat", 0x0, 0x1)

    label("loc_1A83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A9D")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_1A9A")
    Jump("loc_1A9D")

    label("loc_1A9A")

    Jump("loc_1A83")

    label("loc_1A9D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    OP_20(0x7D0)
    Sleep(2000)
    OP_21()
    OP_A2(0x2509)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_16EC end

    def Function_15_1AD2(): pass

    label("Function_15_1AD2")


    def lambda_1AD8():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AD8)
    Sleep(300)

    def lambda_1AF8():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AF8)
    Sleep(300)

    def lambda_1B18():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1B18)
    Sleep(300)

    def lambda_1B38():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1B38)
    Sleep(300)

    def lambda_1B58():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1B58)
    Sleep(300)

    def lambda_1B78():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1B78)
    Sleep(300)

    def lambda_1B98():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1B98)
    Sleep(300)

    def lambda_1BB8():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BB8)
    Sleep(300)

    def lambda_1BD8():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BD8)
    Sleep(300)

    def lambda_1BF8():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x6978, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BF8)
    Sleep(300)

    def lambda_1C18():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C18)
    Sleep(300)

    def lambda_1C38():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C38)
    Sleep(300)

    def lambda_1C58():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C58)
    Sleep(300)

    def lambda_1C78():
        OP_8F(0xFE, 0xFFFF9BD8, 0x5000, 0x7A468, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C78)
    Sleep(300)
    Return()

    # Function_15_1AD2 end

    def Function_16_1C93(): pass

    label("Function_16_1C93")

    OP_24(0x125, 0x5A)
    OP_24(0x159, 0x5A)
    OP_24(0x1C3, 0x5A)
    Sleep(300)
    OP_24(0x125, 0x50)
    OP_24(0x159, 0x50)
    OP_24(0x1C3, 0x50)
    Sleep(300)
    OP_24(0x125, 0x46)
    OP_24(0x159, 0x46)
    OP_24(0x1C3, 0x46)
    Sleep(300)
    OP_24(0x125, 0x3C)
    OP_24(0x159, 0x3C)
    OP_24(0x1C3, 0x3C)
    Sleep(300)
    OP_24(0x125, 0x32)
    OP_24(0x159, 0x32)
    OP_24(0x1C3, 0x32)
    Sleep(300)
    OP_24(0x125, 0x28)
    OP_24(0x159, 0x28)
    OP_24(0x1C3, 0x28)
    Sleep(300)
    OP_24(0x125, 0x1E)
    OP_24(0x159, 0x1E)
    OP_24(0x1C3, 0x1E)
    Sleep(300)
    OP_24(0x125, 0x14)
    OP_24(0x159, 0x14)
    OP_24(0x1C3, 0x14)
    Sleep(300)
    OP_24(0x125, 0xA)
    OP_24(0x159, 0xA)
    OP_24(0x1C3, 0xA)
    Sleep(300)
    OP_24(0x125, 0x0)
    OP_24(0x159, 0x0)
    OP_24(0x1C3, 0x0)
    OP_23(0x125)
    OP_23(0x159)
    OP_23(0x1C3)
    Return()

    # Function_16_1C93 end

    def Function_17_1D42(): pass

    label("Function_17_1D42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp014_00.eff")
    LoadEffect(0x1, "map\\mp021_00.eff")
    LoadEffect(0x2, "map\\mp064_01.eff")
    LoadEffect(0x3, "map\\mp065_01.eff")
    LoadEffect(0x4, "map\\mp064_00.eff")
    LoadEffect(0x5, "map\\mp065_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -42240, 10050, 20620, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 2000)
    OP_22(0x1C9, 0x0, 0x64)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_76(0x2, 0x0, 0x1, 0xFFFFFFF8, 0x0, 0x0, 0x0, 0x0)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_A1(0x13, 0x4)
    SetChrPos(0x13, -26450, 25000, 25740, 255)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_B0(0x4, 0xF)
    OP_6F(0x4, 281)
    OP_70(0x4, 0x12C)
    PlayEffect(0x2, 0x0, 0x13, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x13, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x13, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x13, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x13, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x13, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -38450, 30000, 63740, 270)
    OP_CF(0x14, 0x4, "Frame85__ren")
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 0)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x14, 0x20)
    OP_6D(-42240, 42050, 20620, 0)
    OP_67(0, -1600, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(259000, 0)
    OP_6E(700, 0)
    OP_D0(2000, 0)
    OP_22(0x113, 0x1, 0x64)

    def lambda_201B():
        OP_6D(-42240, 45050, 20620, 15000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_201B)

    def lambda_2033():
        OP_67(0, -4500, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2033)

    def lambda_204B():
        OP_6B(6430, 15000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_204B)

    def lambda_205B():
        OP_6E(973, 15000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_205B)

    def lambda_206B():
        OP_91(0xFE, 0xFFF85EE0, 0x222E0, 0xFFFE7960, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_206B)
    OP_C4(0x1, 0x20000000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14, 0x0, 0x0, 0x12)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x14, 0x3, 0x0, 0x13)
    OP_43(0x14, 0x2, 0x0, 0x14)
    OP_20(0x1388)
    OP_21()
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x14, 0x3)
    OP_44(0x15, 0x0)
    OP_44(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_44(0x15, 0x3)
    OP_44(0x14, 0x0)
    OP_44(0x13, 0x1)
    Sleep(1000)
    OP_F7(0x9, 0xF, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00Side Story [Paradise] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218A")
    Sleep(1000)
    OP_28(0xF, 0x4, 0x10)
    OP_28(0xF, 0x4, 0x20)
    OP_3E(0x2E8, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Received \x1F\xE8\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_218A")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1D42 end

    def Function_18_2197(): pass

    label("Function_18_2197")

    OP_24(0x113, 0x5A)
    Sleep(800)
    OP_24(0x113, 0x50)
    Sleep(700)
    OP_24(0x113, 0x46)
    Sleep(600)
    OP_24(0x113, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x32)
    Sleep(500)
    OP_24(0x113, 0x28)
    Sleep(500)
    OP_24(0x113, 0x1E)
    Sleep(500)
    OP_24(0x113, 0x14)
    Sleep(500)
    OP_24(0x113, 0xA)
    Sleep(500)
    OP_24(0x113, 0x0)
    OP_23(0x113)
    Return()

    # Function_18_2197 end

    def Function_19_21F0(): pass

    label("Function_19_21F0")

    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_24(0x1C3, 0x0)
    OP_23(0x1C3)
    Return()

    # Function_19_21F0 end

    def Function_20_2249(): pass

    label("Function_20_2249")

    OP_24(0x1C9, 0x5A)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x46)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x32)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x1E)
    Sleep(200)
    OP_24(0x1C9, 0x14)
    Sleep(200)
    OP_24(0x1C9, 0xA)
    Sleep(200)
    OP_24(0x1C9, 0x0)
    OP_23(0x1C9)
    Return()

    # Function_20_2249 end

    def Function_21_22A2(): pass

    label("Function_21_22A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(0, -10000, 800, 0)
    OP_67(0, -2890, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(350000, 0)
    OP_6E(450, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x401, 0x0)
    ExitThread()

    def lambda_230B():
        OP_6D(0, -10000, 800, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_230B)

    def lambda_2323():
        OP_67(0, -3220, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2323)

    def lambda_233B():
        OP_6B(1500, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_233B)
    FadeToBright(1500, 0)
    Sleep(5500)
    SetMessageWindowPos(320, 310, -1, -1)
    SetChrName("Major Vander")

    AnonymousTalk(    #3
        (
            "\x07\x00#277FIt's strange to think that this will be the\x01",
            "last time we'll see the moon from here...\x02\x03",

            "Truth be told, I'm going to miss it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 280, -1, -1)
    SetChrName("Prince Olivert")

    AnonymousTalk(    #4
        (
            "\x07\x00#031FWell, well! It looks like putting a smile on your face\x01",
            "a little more often isn't the only thing Liberl's done\x01",
            "for you--it's opened up your eyes to life's natural\x01",
            "beauty as well.\x02\x03",

            "#030FBut in all seriousness, we'll just have to do all we\x01",
            "can to be able to come back and see it again one\x01",
            "day.\x02\x03",

            "While we're both still alive.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("Major Vander")

    AnonymousTalk(    #5
        "\x07\x00#278FHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x15, 0x0, 0x0, 0x16)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    WaitChrThread(0x15, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00#40WThe next morning...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_22A2 end

    def Function_22_2600(): pass

    label("Function_22_2600")

    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_24(0x1C3, 0x0)
    OP_23(0x1C3)
    Return()

    # Function_22_2600 end

    def Function_23_2659(): pass

    label("Function_23_2659")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_24(0x1C3, 0x46)
    OP_71(0x401, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\mp288_00.eff")
    LoadEffect(0x1, "map\\mp288_01.eff")
    LoadEffect(0x2, "map\\mp288_02.eff")
    LoadEffect(0x3, "map\\mp288_04.eff")
    LoadEffect(0x4, "map\\mp289_00.eff")
    LoadEffect(0x5, "map\\mp289_01.eff")
    LoadEffect(0x6, "map\\mp290_00.eff")
    LoadEffect(0x7, "map\\mp293_00.eff")
    OP_6D(0, -20000, 5000, 0)
    OP_67(0, -7890, -10000, 0)
    OP_6B(3910, 0)
    OP_6C(180000, 0)
    OP_6E(880, 0)
    SetChrPos(0x102, 5000, -34000, 0, 0)
    SetChrPos(0x12, -5000, -34000, 0, 0)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x4)
    OP_77(0xC8, 0xC8, 0xC8, 0x0, 0x0)
    OP_22(0x183, 0x0, 0x64)

    def lambda_2784():
        OP_6D(0, -15000, 5000, 30000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2784)

    def lambda_279C():
        OP_67(0, -4300, -10000, 30000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_279C)

    def lambda_27B4():
        OP_6B(1550, 30000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_27B4)

    def lambda_27C4():
        OP_6E(880, 30000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_27C4)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x102, 0x0, 0x0, 0x19)
    Sleep(5000)
    SetMessageWindowPos(330, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #7 op#A
        "\x07\x00#1008F#20AWow, fireworks! They're so pretty!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(3000)
    SetMessageWindowPos(330, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #8 op#A
        "\x07\x00#1001F#20AThere's so many of them, too...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x183, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x102, 0x1, 0x0, 0x19)
    Sleep(12000)
    Fade(2000)
    OP_44(0x15, 0xFF)
    OP_6D(0, -33000, 9900, 0)
    OP_67(0, -16680, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(180000, 0)
    OP_6E(780, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)

    def lambda_28E6():
        OP_6E(580, 10000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_28E6)

    def lambda_28F6():
        OP_D0(40000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_28F6)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    Sleep(7000)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_44(0x102, 0xFF)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_23(0x1C3)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        "\x07\x0C#40WYou see, Estelle...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x3, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00Side Story [The Banquet] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB0")
    Sleep(1000)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x4, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_2A36")
    Jump("loc_2A76")

    label("loc_2A36")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #11
        "\x06\x07\x05Learned the recipe for \x07\x02Luxurious Lunch\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_2A76")

    AddMira(3500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05Received \x07\x023,500 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2AB0")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_2659 end

    def Function_24_2ABD(): pass

    label("Function_24_2ABD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C82")
    PlayEffect(0x0, 0xFF, 0xFF, 0, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(2500)
    PlayEffect(0x2, 0xFF, 0xFF, 5000, -12000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, -6000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1500)
    PlayEffect(0x4, 0xFF, 0xFF, 8000, -14000, -1560, 45, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1500)
    PlayEffect(0x2, 0xFF, 0xFF, 0, -13000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1500)
    PlayEffect(0x4, 0xFF, 0xFF, -11000, -11000, -1560, -45, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, 9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    Jump("Function_24_2ABD")

    label("loc_2C82")

    Return()

    # Function_24_2ABD end

    def Function_25_2C83(): pass

    label("Function_25_2C83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F79")
    PlayEffect(0x3, 0x0, 0xFF, 0, -12000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x1, 0xFF, 9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x2, 0xFF, -11000, -13000, -1560, 45, 50, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1500)
    PlayEffect(0x7, 0x3, 0xFF, 7000, -20000, -2560, 0, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x7, 0x4, 0xFF, -6000, -21000, -2560, 0, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x5, 0xFF, -9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x0, 0xFF, 11000, -16000, -1560, -45, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x183, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x6, 0x1, 0xFF, 0, -11000, -1560, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(2500)
    PlayEffect(0x1, 0x2, 0xFF, -10000, -13000, -2560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x5, 0x3, 0xFF, 11000, -11000, -2560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x5, 0x4, 0xFF, -15000, -20000, -2560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0x5, 0xFF, 16000, -19000, -2560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    Jump("Function_25_2C83")

    label("loc_2F79")

    Return()

    # Function_25_2C83 end

    def Function_26_2F7A(): pass

    label("Function_26_2F7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31A9")
    PlayEffect(0x3, 0xFF, 0xFF, 0, -12000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xFF, 10000, -10000, -5560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0xFF, 0xFF, -11000, -13000, 4560, 45, 50, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -16000, -13000, -12560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x5, 0xFF, 0xFF, 18000, -11000, 7560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, -9000, -10000, -4560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0xFF, 0xFF, 11000, -16000, 5560, -45, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(500)
    PlayEffect(0x5, 0xFF, 0xFF, -12000, -20000, 13060, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 12000, -19000, -9560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("Function_26_2F7A")

    label("loc_31A9")

    Return()

    # Function_26_2F7A end

    SaveToFile()

Try(main)
