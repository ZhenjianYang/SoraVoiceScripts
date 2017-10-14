from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3404   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3404.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        'Walter',                               # 9
        'Abyss Worm',                           # 10
        'Abyss Worm',                           # 11
        'Abyss Worm',                           # 12
        'Abyss Worm',                           # 13
        'Abyss Worm',                           # 14
        'Sieg',                                 # 15
        'Zin',                                  # 16
        'Olivier',                              # 17
        'Kloe',                                 # 18
        'Estelle',                              # 19
        'Zin',                                  # 20
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C8,
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
        NpcIndex            = 0x1CC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9390,
        TriggerZ            = 0,
        TriggerY            = 2710,
        TriggerRange        = 1600,
        ActorX              = 9390,
        ActorZ              = 800,
        ActorY              = 2710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_275",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_2E2",          # 03, 3
        "Function_4_473",          # 04, 4
        "Function_5_62C",          # 05, 5
        "Function_6_635",          # 06, 6
        "Function_7_1D09",         # 07, 7
        "Function_8_1D2E",         # 08, 8
        "Function_9_1D66",         # 09, 9
        "Function_10_1D9E",        # 0A, 10
        "Function_11_1DD6",        # 0B, 11
        "Function_12_1E0E",        # 0C, 12
        "Function_13_1E46",        # 0D, 13
        "Function_14_4423",        # 0E, 14
        "Function_15_4455",        # 0F, 15
        "Function_16_4473",        # 10, 16
        "Function_17_448C",        # 11, 17
        "Function_18_44C9",        # 12, 18
        "Function_19_44EF",        # 13, 19
        "Function_20_4535",        # 14, 20
        "Function_21_4551",        # 15, 21
        "Function_22_4567",        # 16, 22
        "Function_23_45B2",        # 17, 23
        "Function_24_4773",        # 18, 24
        "Function_25_4A41",        # 19, 25
        "Function_26_4AEC",        # 1A, 26
        "Function_27_4C25",        # 1B, 27
        "Function_28_4D6C",        # 1C, 28
        "Function_29_4DD3",        # 1D, 29
        "Function_30_4E34",        # 1E, 30
        "Function_31_4F15",        # 1F, 31
        "Function_32_4F66",        # 20, 32
        "Function_33_4FFE",        # 21, 33
        "Function_34_5064",        # 22, 34
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263")
    Event(0, 5)

    label("loc_263")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_24E end

    def Function_1_275(): pass

    label("Function_1_275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3AF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2A7")
    OP_82(0x80, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_71(0x1, 0x4)
    OP_22(0x1C7, 0x0, 0x64)
    Jump("loc_2B0")

    label("loc_2A7")

    OP_64(0x0, 0x1)
    OP_22(0x10B, 0x1, 0x46)

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2BB")
    OP_64(0x0, 0x1)

    label("loc_2BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3AF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    Call(0, 4)

    label("loc_2CB")

    Return()

    # Function_1_275 end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CC")

    label("loc_2E1")

    Return()

    # Function_2_2CC end

    def Function_3_2E2(): pass

    label("Function_3_2E2")

    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270110, 0x270120, 0x1)
    OP_D2(0x270110, 0x270120, 0x2)
    OP_D2(0x70230, 0x7023C, 0x3)
    OP_D2(0x270110, 0x270120, 0x4)
    OP_D2(0x270110, 0x270120, 0x5)
    OP_D2(0x70218, 0x70224, 0x6)
    OP_D2(0x270110, 0x270120, 0x7)
    OP_D2(0x270110, 0x270120, 0x8)
    OP_D2(0x701D0, 0x701DC, 0x9)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270110, 0x270120, 0xB)
    OP_D2(0x701E8, 0x701F4, 0xC)
    OP_D2(0x270110, 0x270120, 0xD)
    OP_D2(0x270110, 0x270120, 0xE)
    OP_D2(0x70200, 0x7020C, 0xF)
    OP_D2(0x270110, 0x270120, 0x10)
    OP_D2(0x270110, 0x270120, 0x11)
    OP_D2(0x270110, 0x270120, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270110, 0x270120, 0x14)
    OP_D2(0x2701C6, 0x2701CB, 0x15)
    OP_D2(0x270110, 0x270120, 0x16)
    OP_D2(0x270110, 0x270120, 0x17)
    OP_D2(0x270110, 0x270120, 0x18)
    OP_D2(0x270110, 0x270120, 0x19)
    OP_D2(0x270110, 0x270120, 0x1A)
    OP_D2(0x270110, 0x270120, 0x1B)
    OP_D2(0x290077, 0x290079, 0x1C)
    OP_D2(0x29006E, 0x290072, 0x1D)
    OP_D2(0x290070, 0x290074, 0x1E)
    OP_D2(0x2600A0, 0x2600A5, 0x1F)
    OP_D2(0x270110, 0x270120, 0x20)
    OP_D2(0x270110, 0x270120, 0x21)
    OP_D2(0x270110, 0x270120, 0x22)
    OP_D2(0x270110, 0x270120, 0x23)
    OP_D2(0x270110, 0x270120, 0x24)
    OP_D2(0x270110, 0x270120, 0x25)
    OP_D2(0x270110, 0x270120, 0x26)
    OP_D2(0x270110, 0x270120, 0x27)
    Return()

    # Function_3_2E2 end

    def Function_4_473(): pass

    label("Function_4_473")

    OP_D2(0x270110, 0x270120, 0x0)
    OP_D2(0x270113, 0x270123, 0x1)
    OP_D2(0x270114, 0x270124, 0x2)
    OP_D2(0x70230, 0x7023C, 0x3)
    OP_D2(0x70233, 0x7023F, 0x4)
    OP_D2(0x70234, 0x70240, 0x5)
    OP_D2(0x70230, 0x7023C, 0x6)
    OP_D2(0x70233, 0x7023F, 0x7)
    OP_D2(0x70234, 0x70240, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4F5")
    OP_D2(0x70218, 0x70224, 0x9)
    OP_D2(0x7021B, 0x70227, 0xA)
    OP_D2(0x7021C, 0x70228, 0xB)
    Jump("loc_513")

    label("loc_4F5")

    OP_D2(0x701D0, 0x701DC, 0x9)
    OP_D2(0x701D3, 0x701DF, 0xA)
    OP_D2(0x701D4, 0x701E0, 0xB)

    label("loc_513")

    OP_D2(0x701E8, 0x701F4, 0xC)
    OP_D2(0x701EB, 0x701F7, 0xD)
    OP_D2(0x701EC, 0x701F8, 0xE)
    OP_D2(0x70200, 0x7020C, 0xF)
    OP_D2(0x70203, 0x7020F, 0x10)
    OP_D2(0x70204, 0x70210, 0x11)
    OP_D2(0x701E9, 0x701F5, 0x12)
    OP_D2(0x70041, 0x70049, 0x13)
    OP_D2(0x70180, 0x70184, 0x14)
    OP_D2(0x2701C6, 0x2701CB, 0x15)
    OP_D2(0x27022A, 0x270234, 0x16)
    OP_D2(0x27022B, 0x270235, 0x17)
    OP_D2(0x27022C, 0x270236, 0x18)
    OP_D2(0x70070, 0x70078, 0x19)
    OP_D2(0x70248, 0x70254, 0x1A)
    OP_D2(0x7024A, 0x70256, 0x1B)
    OP_D2(0x70250, 0x7025C, 0x1C)
    OP_D2(0x70250, 0x7025C, 0x1D)
    OP_D2(0x270233, 0x27023D, 0x1E)
    OP_D2(0x2600A0, 0x2600A5, 0x1F)
    OP_D2(0x260052, 0x260057, 0x20)
    OP_D2(0x2600A2, 0x2600A7, 0x21)
    OP_D2(0x270232, 0x27023C, 0x22)
    OP_D2(0x60065, 0x6006A, 0x23)
    OP_D2(0x70249, 0x70255, 0x24)
    OP_D2(0x2601A7, 0x2601AC, 0x25)
    OP_D2(0x70030, 0x70038, 0x26)
    OP_D2(0x260068, 0x26006D, 0x27)
    Return()

    # Function_4_473 end

    def Function_5_62C(): pass

    label("Function_5_62C")

    Call(0, 6)
    Call(0, 13)
    Return()

    # Function_5_62C end

    def Function_6_635(): pass

    label("Function_6_635")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_656")
    Call(0, 32)
    Call(0, 33)

    label("loc_656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A")
    LoadEffect(0x0, "Scraft\\\\sc003_01.eff")

    label("loc_67A")

    Call(0, 3)
    OP_6D(-9630, 0, 2800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x90, 0x0, 0x64)
    SetChrPos(0x8, 7910, 0, 3440, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    SetChrPos(0x101, -14730, 0, 1440, 90)
    SetChrPos(0xF7, -14750, 0, 2770, 90)
    SetChrPos(0x107, -15870, 0, 1330, 90)
    SetChrPos(0xF9, -16200, 0, 2330, 90)

    def lambda_72A():
        OP_8E(0xFE, 0xFFFFDC74, 0x0, 0x8DE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72A)
    Sleep(100)

    def lambda_74A():
        OP_8E(0xFE, 0xFFFFDB48, 0x0, 0xE10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_74A)
    Sleep(100)

    def lambda_76A():
        OP_8E(0xFE, 0xFFFFD634, 0x0, 0x71C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_76A)
    Sleep(100)

    def lambda_78A():
        OP_8E(0xFE, 0xFFFFD56C, 0x0, 0xCB2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_78A)
    OP_20(0x5DC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xF9, 0x1)
    OP_1D(0x6F)

    ChrTalk(    #0
        0x101,
        (
            "#1020F#6PWhat the heck is...?\x02\x03",

            "It's spread all over the ground...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        (
            "#065F#5PGlowing veins of...\x01",
            "N-No way... It can't be...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x8,
        "Man's Voice",
        "#6PHeh heh heh.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x8,
        "Man's Voice",
        "#6PYou sure know how to keep a guy waitin'.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#1002F#6PHey...!\x02",
    )

    CloseMessageWindow()

    def lambda_943():
        OP_6D(5590, 0, 2620, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_943)

    def lambda_95B():
        OP_67(0, 2910, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_95B)

    def lambda_973():
        OP_6C(81000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_973)

    def lambda_983():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_983)

    def lambda_993():
        OP_6E(474, 3000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_993)
    Sleep(1000)

    def lambda_9A8():
        OP_8E(0xFE, 0x8C, 0x0, 0x4D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A8)
    Sleep(100)

    def lambda_9C8():
        OP_8E(0xFE, 0xFFFFFEE8, 0xFFFFFFF6, 0x884, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_9C8)
    Sleep(200)

    def lambda_9E8():
        OP_8E(0xFE, 0xFFFFF97A, 0xFFFFFFA6, 0xA64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_9E8)
    Sleep(100)

    def lambda_A08():
        OP_8E(0xFE, 0xFFFFFBBE, 0x0, 0x154, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_A08)
    Sleep(1500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x107, 0x0)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        "#1005F#2PA man with sunglasses...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AA7")

    ChrTalk(    #6
        0x106,
        (
            "#057F#5PAnd on the pole...\x01",
            "Aw, hell. Another Gospel?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADE")

    label("loc_AA7")


    ChrTalk(    #7
        0x103,
        (
            "#022F#5PAnd...a Gospel on the pole.\x01",
            "Well, then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADE")


    NpcTalk(    #8
        0x8,
        "Sunglasses Man",
        (
            "#250F#6PEvenin', ladies. Good of you\x01",
            "to come all the way out here.\x02\x03",

            "I'll do what I can to make you\x01",
            "feel nice and welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1005F#2PYou... You're one of Ouroboros' \x01",
            "thugs, aren't you?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x8,
        "Sunglasses Man",
        "#252F#6PHeh heh...\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS115._CH")
    OP_C6(0x0, 0x0, 125000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Sunglasses Man")

    AnonymousTalk(    #11
        (
            "#250FEnforcer No. VIII, Walter the Direwolf.\x02\x03",

            "That's what they call me, at any rate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D26")

    ChrTalk(    #12
        0x106,
        (
            "#057F#5PI knew it...\x02\x03",

            "Lemme guess, you're the one behind\x01",
            "all these earthquakes, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D94")

    label("loc_D26")


    ChrTalk(    #13
        0x103,
        (
            "#022F#5PThe pleasure is all yours, trust me.\x02\x03",

            "I'd assume you are the one behind\x01",
            "these earthquakes, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D94")


    ChrTalk(    #14
        0x8,
        (
            "#252F#6PC'mon, let's knock it off with the\x01",
            "obvious and just get down to it.\x02\x03",

            "This 'pole' is a little trick the\x01",
            "society's brains came up with to\x01",
            "mess with septium veins.\x02\x03",

            "It normally just screws with the\x01",
            "vein directly beneath it.\x02\x03",

            "You plug a Gospel into this thing,\x01",
            "though, and you can cause a local\x01",
            "earthquake or two.\x02\x03",

            "That's what I was asked to test.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F34")

    ChrTalk(    #15
        0x104,
        "#032FYour experiments are over, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_F34")


    ChrTalk(    #16
        0x105,
        (
            "#043FYou 'were' asked to...?\x01",
            "Your tests are finished, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F75")


    ChrTalk(    #17
        0x8,
        (
            "#250F#6PYeah. Real shame, too.\x02\x03",

            "What I wanted to do was work up\x01",
            "enough power to shatter buildings.\x02\x03",

            "Couldn't quite get it to hit with that\x01",
            "much force, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#065FWait... B-B-But...\x02\x03",

            "If the buildings collapsed, all the\x01",
            "people inside would get hurt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#252F#6PHeh. You catch on quick, little girlie.\x02\x03",

            "Some of 'em would get crushed under\x01",
            "the rubble, their arms and legs mashed\x01",
            "into jelly, left screamin' like pigs...\x02\x03",

            "Others? They'd get quick deaths. Heads\x01",
            "shattered like eggs, spillin' their brains\x01",
            "out on the road for everyone to see.\x02\x03",

            "Heeey, I've got an idea! How about we\x01",
            "do that to you instead? That blond head\x01",
            "of yours looks pretty fragile to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x107,
        "#069FAAAAAH! NO, GET AWAY!\x02",
    )

    OP_9E(0x107, 0x14, 0x0, 0x1F4, 0xFA0)
    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1002F#2PYou unbelievable son of a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#252F#6PAww, now what's with those faces?\x01",
            "I've been doin' you all a favor.\x02\x03",

            "You see, I just think the dreary, soggy\x01",
            "porridge of most people's lives needs\x01",
            "a little 'spice.'\x02\x03",

            "Thrills and suspense, you know?\x01",
            "The kind that leaves you in a cold sweat.\x02\x03",

            "Pushed to the point...where you could\x01",
            "die at any second.\x02\x03",

            "C'mon... Don't tell me I don't have your\x01",
            "heart poundin'!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1463")

    ChrTalk(    #23
        0x106,
        (
            "#551F#5PTch... What are you, some kind of psycho?\x02\x03",

            "#057FI get it now, though.\x02\x03",

            "You were luring us in here, weren't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150B")

    label("loc_1463")


    ChrTalk(    #24
        0x103,
        (
            "#025F#5PWell. Congratulations.\x01",
            "YOU are now the worst man I've ever known.\x02\x03",

            "#022FI think I see your plot now, however.\x02\x03",

            "You lured us here deliberately, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150B")

    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x101,
        "#1020F#2PWha...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1627")

    ChrTalk(    #26
        0x104,
        (
            "#035FYou allowed yourself to be seen all\x01",
            "over the region.\x02\x03",

            "And Elmo's hot springs boiled over\x01",
            "immediately after the earthquake at\x01",
            "the fortress...\x02\x03",

            "#030FIt was all a way of broadcasting your\x01",
            "location to us, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F9")

    label("loc_1627")


    ChrTalk(    #27
        0x105,
        (
            "#047FYou allowed yourself to be seen all\x01",
            "over the region.\x02\x03",

            "And Elmo's hot springs boiled over\x01",
            "immediately after the earthquake at\x01",
            "Leiston Fortress...\x02\x03",

            "#042FYou were issuing a challenge to us,\x01",
            "weren't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F9")


    ChrTalk(    #28
        0x101,
        "#1026F#2POh, crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#250F#6PHeh. Well, close enough for bracer\x01",
            "work, I guess.\x02\x03",

            "Enough talk.\x02\x03",

            "#252FLet's see what you're made of!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(500)
    SetChrSubChip(0x8, 2)
    OP_22(0xBC, 0x0, 0x64)
    OP_20(0x0)
    Sleep(500)
    Fade(1000)
    OP_E8(0xDC, 0x5, 0x0, 0x0)
    OP_6D(4130, 0, 3270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1050, 0)
    OP_6C(45000, 0)
    OP_6E(922, 0)
    SetChrPos(0x8, 8100, 0, 3250, 270)
    SetChrPos(0x101, 2029, 0, 1070, 90)
    SetChrPos(0xF7, 1710, 0, 2520, 90)
    SetChrPos(0xF9, 260, 0, 2110, 90)
    SetChrPos(0x107, 690, 0, 550, 90)
    OP_0D()
    OP_22(0x85, 0x0, 0x64)

    def lambda_184B():

        label("loc_184B")

        OP_7C(0x0, 0xC8, 0x12C, 0x64)
        OP_48()
        Jump("loc_184B")

    QueueWorkItem2(0x8, 3, lambda_184B)
    OP_6D(2260, 0, 2160, 1500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 150, 800, -3740, 0)
    SetChrPos(0xA, -3070, 800, 180, 90)
    SetChrPos(0xB, -2420, 800, 5380, 135)
    SetChrPos(0xC, 3190, 800, 6030, 180)
    SetChrPos(0xD, 5440, 800, -1300, 270)
    OP_43(0x9, 0x0, 0x0, 0x7)
    OP_43(0xC, 0x0, 0x0, 0x7)
    Sleep(200)
    OP_43(0xA, 0x0, 0x0, 0x7)
    OP_43(0xB, 0x0, 0x0, 0x7)
    Sleep(200)
    OP_43(0xD, 0x0, 0x0, 0x7)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)

    def lambda_1972():
        OP_8C(0x107, 225, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1972)

    def lambda_1980():
        OP_8C(0xF9, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1980)
    Sleep(100)

    def lambda_1993():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1993)
    Sleep(100)

    def lambda_19A6():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_19A6)
    WaitChrThread(0xF7, 0x1)
    OP_24(0x85, 0x5A)
    Sleep(100)
    OP_24(0x85, 0x50)
    Sleep(100)
    OP_24(0x85, 0x46)
    Sleep(100)
    OP_24(0x85, 0x3C)
    Sleep(100)
    OP_24(0x85, 0x32)
    Sleep(100)
    OP_24(0x85, 0x28)
    Sleep(100)
    OP_24(0x85, 0x1E)
    Sleep(100)
    OP_23(0x85)
    OP_44(0x8, 0x3)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x107, 3)
    OP_1D(0x29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A2D")
    SetChrChipByIndex(0x106, 6)
    Jump("loc_1A32")

    label("loc_1A2D")

    SetChrChipByIndex(0x103, 9)

    label("loc_1A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A47")
    SetChrChipByIndex(0x104, 12)
    Jump("loc_1A4C")

    label("loc_1A47")

    SetChrChipByIndex(0x105, 15)

    label("loc_1A4C")

    Sleep(500)

    ChrTalk(    #30
        0x107,
        "#065FAIIEEEEEEE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1020F#6PThe heck are THOSE?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    ChrTalk(    #32
        0x8,
        (
            "#252F#4PThese're some worms that live\x01",
            "in this area.\x02\x03",

            "Apparently, when you stimulate\x01",
            "the septium veins, they grow as\x01",
            "huge as these guys here.\x02\x03",

            "Well, have fun, ladies.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #33
        0x101,
        (
            "#1005F#6POh, what the heck is this?!\x02\x03",

            "You rotten coward!\x01",
            "Fight us fair and square!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BED")

    ChrTalk(    #34
        0x106,
        (
            "#054F#6PForget him! We need to take\x01",
            "care of these things first!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C42")

    label("loc_1BED")


    ChrTalk(    #35
        0x103,
        (
            "#024F#6PDon't let him distract you, Estelle!\x01",
            "We need to defeat the worms first!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C74")

    ChrTalk(    #36
        0x104,
        "#530F#6PCourage, my friends!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C94")

    label("loc_1C74")


    ChrTalk(    #37
        0x105,
        "#042F#6PDefend yourselves!\x02",
    )

    CloseMessageWindow()

    label("loc_1C94")

    OP_43(0x9, 0x0, 0x0, 0x8)
    OP_43(0xD, 0x0, 0x0, 0xC)
    Sleep(30)
    OP_43(0xB, 0x0, 0x0, 0xA)
    Sleep(30)
    OP_43(0xA, 0x0, 0x0, 0x9)
    OP_43(0xC, 0x0, 0x0, 0xB)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0xD, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Battle(0x3AF, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1D03"),
        (SWITCH_DEFAULT, "loc_1D08"),
    )


    label("loc_1D03")

    OP_B4(0x0)
    Jump("loc_1D08")

    label("loc_1D08")

    Return()

    # Function_6_635 end

    def Function_7_1D09(): pass

    label("Function_7_1D09")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 0)
    OP_43(0xFE, 0x1, 0x0, 0x2)
    Return()

    # Function_7_1D09 end

    def Function_8_1D2E(): pass

    label("Function_8_1D2E")

    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    def lambda_1D42():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1D42)
    Sleep(200)
    OP_8F(0xFE, 0x1C2, 0x320, 0xFFFFFC18, 0x1770, 0x0)
    Return()

    # Function_8_1D2E end

    def Function_9_1D66(): pass

    label("Function_9_1D66")

    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    def lambda_1D7A():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1D7A)
    Sleep(200)
    OP_8F(0xFE, 0xFFFFFAC4, 0x320, 0x23A, 0x1770, 0x0)
    Return()

    # Function_9_1D66 end

    def Function_10_1D9E(): pass

    label("Function_10_1D9E")

    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    def lambda_1DB2():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1DB2)
    Sleep(200)
    OP_8F(0xFE, 0xFFFFFE5C, 0x320, 0xEBA, 0x1770, 0x0)
    Return()

    # Function_10_1D9E end

    def Function_11_1DD6(): pass

    label("Function_11_1DD6")

    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    def lambda_1DEA():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1DEA)
    Sleep(200)
    OP_8F(0xFE, 0x92E, 0x320, 0xFDB, 0x1770, 0x0)
    Return()

    # Function_11_1DD6 end

    def Function_12_1E0E(): pass

    label("Function_12_1E0E")

    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    def lambda_1E22():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1E22)
    Sleep(200)
    OP_8F(0xFE, 0xD70, 0x320, 0x6E, 0x1770, 0x0)
    Return()

    # Function_12_1E0E end

    def Function_13_1E46(): pass

    label("Function_13_1E46")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(3700, 0, 3240, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(53000, 0)
    OP_6E(474, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_22(0x90, 0x0, 0x64)
    SetChrPos(0x8, 8100, 0, 3250, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    SetChrPos(0x101, 2029, 0, 1070, 180)
    SetChrPos(0xF7, 1710, 0, 2520, 0)
    SetChrPos(0xF9, 260, 0, 2110, 270)
    SetChrPos(0x107, 690, 0, 550, 180)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x107, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F3E")
    SetChrChipByIndex(0x106, 9)
    Jump("loc_1F43")

    label("loc_1F3E")

    SetChrChipByIndex(0x103, 9)

    label("loc_1F43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F58")
    SetChrChipByIndex(0x104, 12)
    Jump("loc_1F5D")

    label("loc_1F58")

    SetChrChipByIndex(0x105, 15)

    label("loc_1F5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F81")
    LoadEffect(0x0, "Scraft\\\\sc003_01.eff")

    label("loc_1F81")

    LoadEffect(0x1, "battle\\\\damage0.eff")
    LoadEffect(0x2, "Scraft\\\\sc006_17.eff")
    LoadEffect(0x3, "Scraft\\\\sc006_16.eff")
    LoadEffect(0x4, "Scraft\\\\sc007_05.eff")
    LoadEffect(0x5, "Scraft\\\\sc007_06.eff")
    LoadEffect(0x6, "Scraft\\sc000_00.eff")
    LoadEffect(0x7, "Scraft\\sc000_10.eff")
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #38
        0x101,
        (
            "#1025F#5POkay... We managed to win...\x01",
            "and I think I...still have most\x01",
            "of my limbs... Phew!...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x107,
        "#561FPhew!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20CB")

    ChrTalk(    #40
        0x104,
        "#034F#5PSuch vulgar foes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2104")

    label("loc_20CB")


    ChrTalk(    #41
        0x105,
        (
            "#042F#5PThose creatures were incredibly\x01",
            "powerful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2104")


    ChrTalk(    #42
        0x8,
        (
            "#250F#4PMmm. I mighta expected a bit much.\x02\x03",

            "I thought that fight would be a LITTLE\x01",
            "less pathetic.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2171():
        OP_6D(5390, 0, 3650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2171)
    OP_8C(0x101, 90, 400)
    OP_8C(0xF7, 90, 400)
    OP_8C(0xF9, 90, 400)
    OP_8C(0x107, 90, 400)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2211")

    ChrTalk(    #43
        0x106,
        (
            "#555F#5PPffft. Don't underestimate us, pal.\x02\x03",

            "We've killed monsters like that\x01",
            "plenty of times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2286")

    label("loc_2211")


    ChrTalk(    #44
        0x103,
        (
            "#022F#5PYou underestimate us at your peril,\x01",
            "'Direwolf.'\x02\x03",

            "We've slain monsters like your pets\x01",
            "many times before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2286")


    ChrTalk(    #45
        0x8,
        (
            "#254FTch.\x02\x03",

            "Screw it. This is just sad.\x02\x03",

            "I didn't think you'd be THIS weak.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_22FB")

    ChrTalk(    #46
        0x106,
        "#052F#5PThe hell...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2311")

    label("loc_22FB")


    ChrTalk(    #47
        0x103,
        "#023F#5PWhat...?\x02",
    )

    CloseMessageWindow()

    label("loc_2311")

    Fade(500)

    def lambda_231C():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_231C)
    SetChrChipByIndex(0x8, 23)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #48
        0x8,
        "#258FI'm disappointed in YOU worms!\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x18)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF7, 0x3)
    WaitChrThread(0xF9, 0x3)
    WaitChrThread(0x107, 0x3)
    Sleep(600)
    OP_43(0xF7, 0x1, 0x0, 0xE)
    Sleep(200)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x11)
    Sleep(200)
    OP_43(0x107, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x107, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x1E, 0x1C, 0x3E8)
    Fade(500)
    SetChrFlags(0x8, 0x100)
    ClearChrFlags(0x8, 0x2)
    OP_51(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 24)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 3240, 0, 1820, 225)

    def lambda_242A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_242A)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0x8,
        "#254F#2PThis is bullshit...\x02",
    )

    CloseMessageWindow()

    def lambda_245F():
        OP_6D(4130, 0, 3270, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_245F)

    def lambda_2477():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2477)

    def lambda_248F():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_248F)

    def lambda_249F():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_249F)

    def lambda_24AF():
        OP_6E(474, 3000)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_24AF)
    OP_43(0x8, 0x1, 0x0, 0x12)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x1)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    OP_0D()

    ChrTalk(    #50
        0x8,
        (
            "#254FLoewe was talking out his ass again.\x02\x03",

            "'He tells me the Divine Blade isn't the only\x01",
            "one in Liberl who might give me a run for\x01",
            "my money, and THIS is what I get?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25B3")

    ChrTalk(    #51
        0x106,
        "#057F#5PGotta be...kidding me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_25CF")

    label("loc_25B3")


    ChrTalk(    #52
        0x103,
        "#522F#5PThat... No... \x02",
    )

    CloseMessageWindow()

    label("loc_25CF")


    ChrTalk(    #53
        0x8,
        (
            "#252FWell, nothin' for it, then.\x02\x03",

            "I'll just have to sweet talk the professor\x01",
            "into letting me hunt old Fangboy.\x02\x03",

            "He'll be a little more exciting than this,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1020F#5PWha...?\x02\x03",

            "#1005FH...Hold on!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26A9():

        label("loc_26A9")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_26A9")

    QueueWorkItem2(0x101, 3, lambda_26A9)
    Sleep(500)
    OP_99(0x101, 0x3, 0x0, 0x12C)
    Sleep(500)
    OP_44(0x101, 0x3)
    SetChrFlags(0x8, 0x20)
    OP_8C(0x8, 225, 400)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x101, 0x800)

    ChrTalk(    #55
        0x8,
        "#250FWhat? You can still talk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1005F#5PYou...disgusting sicko...\x01",
            "Listen to me...\x02\x03",

            "If you mean Joshua when you say 'fangboy'...\x02\x03",

            "I...will...never...let...you...HURT HIM!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        "#065F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#250FI'd give you props on taking my punch\x01",
            "and still bein' able to stand...\x02\x03",

            "...but give it up. I can see your knees\x01",
            "buckling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1022F#5PYou really think I...care about that...?\x02\x03",

            "I'll find Joshua... I'll bring him home...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #60
        0x101,
        "#1005F#5PAND I WON'T LET SCUM LIKE YOU GET IN MY WAY!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2919")

    ChrTalk(    #61
        0x104,
        "#032F#5PEstelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2932")

    label("loc_2919")


    ChrTalk(    #62
        0x105,
        "#043F#5PEstelle...!\x02",
    )

    CloseMessageWindow()

    label("loc_2932")


    def lambda_2938():
        OP_6D(2990, 0, 690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2938)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 21)
    OP_8E(0x8, 0xE9C, 0x0, 0x136, 0x7D0, 0x0)
    OP_8C(0x8, 270, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #63
        0x8,
        (
            "#250F#4P...You GET why they call me the 'Direwolf,'\x01",
            "right? I don't hold back for women or kids.\x01",
            "Or both.\x02\x03",

            "You're a martial artist...sort of. I hope you\x01",
            "know what you're askin' for by pointin' that\x01",
            "thing at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1005F#6POf course I do...!\x02\x03",

            "If you think you can beat me...\x01",
            "COME ON!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "#252F#4PHeh heh heh. Nice.\x02",
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_2AD5():
        OP_6B(1800, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2AD5)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 23)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0x8,
        (
            "#250F#4PTell you what: I respect your guts.\x01",
            "You'll die in one blow. I'll make it quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1002F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0xC8, 1600, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #68
        0x107,
        (
            "#069F#5PNOOOOOOO!\x01",
            "ESTEEEEEEEEEELLE!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2BCC")

    ChrTalk(    #69
        0x106,
        (
            "#054F#6PEstelle!\x01",
            "RUN, DAMN IT!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE7")

    label("loc_2BCC")


    ChrTalk(    #70
        0x103,
        "#024F#6PEstelle! RUN!\x02",
    )

    CloseMessageWindow()

    label("loc_2BE7")


    ChrTalk(    #71
        0x8,
        "#250F#4PDie.\x02",
    )

    CloseMessageWindow()
    OP_20(0x0)
    OP_E8(0xDC, 0x5, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D26")
    OP_22(0x197, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)
    SetChrPos(0xE, -11220, 3000, 3760, 90)
    SetChrFlags(0xE, 0x40)
    OP_7D(0x0, 0xE, 0x32, 0x1F4)
    OP_6D(-3050, 0, 3540, 800)
    ClearChrFlags(0xE, 0x80)
    OP_43(0xE, 0x1, 0x0, 0x15)

    def lambda_2C5B():
        OP_6D(3230, 0, 1550, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2C5B)

    def lambda_2C73():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C73)

    def lambda_2C83():
        OP_8E(0xE, 0xE9C, 0x0, 0x136, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2C83)
    Sleep(500)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_2CA8():
        OP_96(0x8, 0x16BC, 0x0, 0x366, 0x12C, 0x3A98)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2CA8)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 22)

    def lambda_2CD0():
        TurnDirection(0x8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2CD0)
    OP_7D(0x1, 0xE, 0x0, 0x0)

    def lambda_2CE6():
        OP_8E(0xE, 0x4434, 0xFA0, 0xFFFFF632, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2CE6)
    Sleep(500)

    ChrTalk(    #72
        0x8,
        "#254F#4PGh...?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x2)
    OP_44(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    Jump("loc_2DA3")

    label("loc_2D26")


    def lambda_2D2C():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2D2C)
    PlayEffect(0x0, 0xFF, 0xFF, -6020, 1000, 400, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_96(0x8, 0x16BC, 0x0, 0x366, 0x12C, 0x3A98)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #73
        0x8,
        "#254F#4PGh...?!\x02",
    )

    CloseMessageWindow()

    label("loc_2DA3")


    ChrTalk(    #74
        0x101,
        "#1004F#6PWha...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x2C)
    Fade(400)
    OP_6D(-200, 0, -400, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(78000, 0)
    OP_6E(474, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0x0, 0xF, 0x32, 0x12C)
    SetChrPos(0xF, -10320, 0, -160, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 36)
    SetChrSubChip(0xF, 0)

    NpcTalk(    #75 op#A op#5
        0xF,
        "Man's Voice",
        "#10A#5PHaaaaa-AAAAH!\x05\x02",
    )


    def lambda_2E5B():
        OP_8E(0xFE, 0xFFFFE96C, 0xFFFFFFBA, 0x186, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E5B)
    WaitChrThread(0xF, 0x1)

    def lambda_2E7B():
        OP_6D(3500, 0, 400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E7B)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x20)
    SetChrChipByIndex(0xF, 28)
    SetChrSubChip(0xF, 32)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2EB1():
        OP_96(0xFE, 0xFFFFFB78, 0xFFFFFF9C, 0xFFFFF5C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2EB1)
    WaitChrThread(0xF, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xF, 33)
    SetChrSubChip(0xF, 15)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2EE8():
        OP_96(0xFE, 0x226, 0xFFFFFF9C, 0x4C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2EE8)
    WaitChrThread(0xF, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2F10():
        OP_6D(5000, 0, 1360, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F10)

    def lambda_2F28():
        OP_67(0, 4500, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F28)

    def lambda_2F40():
        OP_6B(1600, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F40)

    def lambda_2F50():
        OP_6C(45000, 500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_2F50)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 33)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2F79():
        OP_96(0xF, 0x10FE, 0x1F4, 0x3C0, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2F79)
    OP_99(0xF, 0x0, 0x3, 0xDAC)
    SetChrSubChip(0xF, 3)
    SetChrChipByIndex(0xF, 33)
    OP_7D(0x1, 0xF, 0x0, 0x0)
    OP_43(0x101, 0x3, 0x0, 0x1E)
    Sleep(200)
    OP_43(0xF, 0x0, 0x0, 0x1D)
    WaitChrThread(0xF, 0x0)

    def lambda_2FCA():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FCA)

    def lambda_2FDA():
        OP_6D(5330, 0, 1510, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FDA)

    def lambda_2FF2():
        OP_67(0, 5500, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FF2)
    ClearChrFlags(0xF, 0x4)

    def lambda_300F():
        OP_96(0xFE, 0xC26, 0x0, 0x154, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_300F)

    def lambda_302D():
        OP_99(0xF, 0x13, 0x17, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_302D)
    WaitChrThread(0xF, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xF, 0x2)
    Sleep(500)

    NpcTalk(    #76
        0xF,
        "Eastern Giant",
        "#6P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315C")
    SetChrPos(0x11, -5100, 0, -1100, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xE, 7850, 4000, 9650, 90)
    ClearChrFlags(0xE, 0x80)

    NpcTalk(    #77
        0x11,
        "Girl's Voice",
        "#2PThank Aidios...we made it in time!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0x11, 19)
    OP_43(0xE, 0x0, 0x0, 0x15)
    OP_43(0xE, 0x1, 0x0, 0x16)
    OP_8F(0x11, 0x708, 0x0, 0x514, 0x1388, 0x0)
    SetChrSubChip(0x11, 3)
    SetChrChipByIndex(0x11, 35)
    WaitChrThread(0xE, 0x1)
    Fade(250)
    SetChrFlags(0xE, 0x80)
    SetChrSubChip(0x11, 1)
    SetChrChipByIndex(0x11, 35)
    OP_0D()

    ChrTalk(    #78
        0x101,
        "#1004F#5PKloe! And...ZIN?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_321E")

    label("loc_315C")

    SetChrPos(0x10, -4120, 0, -400, 90)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_317E")
    SetChrFlags(0x10, 0x8000)

    label("loc_317E")


    NpcTalk(    #79
        0x10,
        "Man's Voice",
        "#2PHeh! A perfect entrance, my friend!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0x10, 18)
    OP_8F(0x10, 0x708, 0x0, 0x514, 0x1388, 0x0)
    OP_8C(0x10, 90, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_31E7")
    ClearChrFlags(0x10, 0x8000)

    label("loc_31E7")

    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 12)
    Sleep(500)

    ChrTalk(    #80
        0x101,
        "#1004F#5POlivier! And...ZIN?!\x02",
    )

    CloseMessageWindow()

    label("loc_321E")


    ChrTalk(    #81
        0xF,
        (
            "#070F#1PHey, Estelle. Feels like it's been ages.\x02\x03",

            "I meant to come sooner, but work back\x01",
            "home took longer than I expected...\x02\x03",

            "I'm glad to see I made it in time!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3312")

    ChrTalk(    #82
        0x106,
        (
            "#556F#5PGeez... Did you have to wait till the\x01",
            "last second, man?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3357")

    label("loc_3312")


    ChrTalk(    #83
        0x103,
        (
            "#524F#5PDon't tell me you didn't time that\x01",
            "one on purpose, Zin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3357")


    ChrTalk(    #84
        0x8,
        (
            "#257FHeh...heh heh heh...\x02\x03",

            "So YOU'RE the A-rank bracer Loewe\x01",
            "mentioned?\x02\x03",

            "#251FPerfect. Been a while, Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        (
            "#074F#1PThat's right...Walter.\x02\x03",

            "#072FI hardly expected to meet you here,\x01",
            "of all places, though.\x02\x03",

            "I always knew you had the mind of a\x01",
            "wolf, but tell me, when did you develop\x01",
            "the heart and loyalty of a serpent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#253FOh, that'd be right after we 'met' last.\x02\x03",

            "I've been having the time of my life since\x01",
            "I joined the society, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xF,
        (
            "#077F#1PYou blind fool...\x02\x03",

            "#076FDo you even realize what you've done?\x01",
            "What you're DOING?!\x02\x03",

            "It would break Master's heart to see--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#255FOh, spare me the righteous claptrap.\x02\x03",

            "You know better than anyone the path\x01",
            "I've chosen.\x02\x03",

            "#253FYou keep talkin' nonsense, and I WILL\x01",
            "kill you. Got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xF,
        (
            "#072F#1P...\x02\x03",

            "#075FI wonder...do you even know?\x02\x03",

            "Kilika's up there. In Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #90
        0x8,
        "#255FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xF,
        (
            "#072F#1PShe's been working there as the\x01",
            "guild receptionist for the past two\x01",
            "years.\x02\x03",

            "Before then, she was wandering\x01",
            "the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#256FThe hell...?\x02\x03",

            "Why bother coming to a backwater\x01",
            "place like Liberl...?\x02\x03",

            "#257FWhat's she thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xF,
        (
            "#074F#1PI don't know either, to be honest.\x02\x03",

            "#070FBut I do know that, even now, she\x01",
            "wants to see you.\x02\x03",

            "Set aside this 'Ouroboros' madness,\x01",
            "Walter. Go see--\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 34)
    SetChrSubChip(0x8, 0)

    def lambda_3868():
        OP_99(0x8, 0x0, 0x2, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3868)
    WaitChrThread(0x8, 0x2)

    def lambda_387D():
        OP_6D(3710, 0, 400, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_387D)

    def lambda_3895():
        OP_67(0, 4500, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3895)

    def lambda_38AD():
        OP_6B(1600, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38AD)
    ClearChrFlags(0x8, 0x4)

    def lambda_38C2():
        OP_96(0x8, 0x1108, 0x4B0, 0xA0, 0x578, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38C2)
    OP_22(0x84, 0x0, 0x64)

    def lambda_38E5():
        OP_99(0x8, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_38E5)
    WaitChrThread(0x8, 0x2)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x7, 0xFF, 0xF, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x2)
    ClearChrFlags(0xF, 0x20)
    OP_8C(0xF, 90, 0)
    SetChrChipByIndex(0xF, 27)
    SetChrSubChip(0xF, 6)

    def lambda_395B():
        OP_8F(0xFE, 0xC26, 0x0, 0x348, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_395B)

    def lambda_3976():
        OP_9E(0xF, 0x28, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3976)
    Sleep(200)

    def lambda_3995():
        OP_99(0x8, 0x5, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3995)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #94
        0xF,
        "#077F#6PGuh...!\x02",
    )

    WaitChrThread(0x8, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F6")
    SetChrFlags(0x11, 0x20)
    OP_8C(0x11, 135, 400)
    ClearChrFlags(0x11, 0x20)
    Jump("loc_39FD")

    label("loc_39F6")

    OP_8C(0x10, 135, 400)

    label("loc_39FD")

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #95
        0x8,
        "#254F#4PI told you. Talk nonsense, I kill you.\x02",
    )

    CloseMessageWindow()

    def lambda_3A48():
        OP_6D(5700, 0, 2200, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A48)

    def lambda_3A60():
        OP_67(0, 5500, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A60)

    def lambda_3A78():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A78)
    Sleep(100)
    OP_8C(0x8, 225, 0)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 0)
    OP_22(0x23B, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_96(0x8, 0x1EB4, 0x0, 0xB22, 0x190, 0x1770)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    SetChrChipByIndex(0xF, 26)
    SetChrSubChip(0xF, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AFE")
    SetChrFlags(0x11, 0x20)
    OP_8C(0x11, 90, 400)
    ClearChrFlags(0x11, 0x20)
    Jump("loc_3B05")

    label("loc_3AFE")

    OP_8C(0x10, 90, 400)

    label("loc_3B05")

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #96
        0x8,
        (
            "#250FHeh heh. Well, hey.\x02\x03",

            "Forget Kilika. You being here just\x01",
            "made my year.\x02\x03",

            "This plan of the professor's is gonna\x01",
            "be a whole lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BA8():
        OP_6D(6620, 0, 2060, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3BA8)
    SetChrFlags(0x8, 0x20)
    OP_8C(0x8, 90, 400)
    ClearChrFlags(0x8, 0x20)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    OP_71(0x1, 0x4)
    Sleep(1000)
    OP_22(0x64, 0x0, 0x64)
    OP_22(0x83, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9A, 0x0, 0x64)
    Sleep(500)
    Fade(1000)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x1)
    OP_79(0x2, 0x1)
    OP_79(0x3, 0x1)
    OP_79(0x4, 0x1)
    OP_7B()
    OP_82(0x80, 0x0)
    OP_82(0x83, 0x2)
    OP_82(0x84, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_24(0x90, 0x5A)
    Sleep(500)
    OP_24(0x90, 0x50)
    Sleep(500)
    OP_24(0x90, 0x46)
    Sleep(500)
    OP_24(0x90, 0x3C)
    Sleep(250)
    OP_24(0x90, 0x32)
    Sleep(250)
    OP_24(0x90, 0x28)
    Sleep(250)
    OP_24(0x90, 0x1E)
    Sleep(150)
    OP_24(0x90, 0x14)
    Sleep(50)
    OP_24(0x90, 0xA)
    Sleep(50)
    OP_23(0x90)

    ChrTalk(    #97
        0xF,
        "#076F#1PWait! Walter!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x20)
    OP_8C(0x8, 225, 400)
    ClearChrFlags(0x8, 0x20)
    Sleep(500)

    ChrTalk(    #98
        0x8,
        (
            "#252F#4PYou ladies keep workin' on your\x01",
            "kung fu until next time.\x02\x03",

            "See ya.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x20)
    OP_8C(0x8, 270, 400)
    ClearChrFlags(0x8, 0x20)

    def lambda_3D40():
        OP_6D(3970, 0, 2280, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3D40)

    def lambda_3D58():

        label("loc_3D58")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3D58")

    QueueWorkItem2(0x101, 3, lambda_3D58)

    def lambda_3D69():

        label("loc_3D69")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3D69")

    QueueWorkItem2(0xF, 3, lambda_3D69)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9A")
    SetChrFlags(0x11, 0x20)

    def lambda_3D8C():

        label("loc_3D8C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3D8C")

    QueueWorkItem2(0x11, 3, lambda_3D8C)
    Jump("loc_3DAB")

    label("loc_3D9A")


    def lambda_3DA0():

        label("loc_3DA0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3DA0")

    QueueWorkItem2(0x10, 3, lambda_3DA0)

    label("loc_3DAB")

    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 21)

    def lambda_3DBB():
        OP_8F(0x8, 0xFFFFDCD8, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3DBB)
    Sleep(1500)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1000)
    OP_44(0x11, 0x3)
    OP_44(0x10, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E22")

    def lambda_3E17():
        OP_8C(0xFE, 325, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3E17)
    Jump("loc_3E30")

    label("loc_3E22")


    def lambda_3E28():
        OP_8C(0xFE, 325, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_3E28)

    label("loc_3E30")


    ChrTalk(    #99
        0xF,
        "#076F#3S#6PWALTER...!\x02",
    )

    CloseMessageWindow()

    def lambda_3E51():
        OP_6D(-500, 0, 2000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E51)

    def lambda_3E69():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3E69)

    def lambda_3E81():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3E81)
    OP_44(0xF, 0x3)
    SetChrChipByIndex(0xF, 36)
    SetChrSubChip(0xF, 0)
    OP_8E(0xF, 0x9E2, 0x0, 0xF8C, 0xFA0, 0x0)
    OP_20(0xBB8)
    OP_8E(0xF, 0xFFFFFCE0, 0xFFFFFF7E, 0xE92, 0xFA0, 0x0)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 25)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x10, 0x3)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    Sleep(500)
    WaitChrThread(0x8, 0x3)

    ChrTalk(    #100
        0xF,
        "#072F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x13)
    Sleep(800)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    Sleep(800)
    OP_43(0x107, 0x1, 0x0, 0x13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F44")
    Jump("loc_3F4E")

    label("loc_3F44")

    SetChrChipByIndex(0x10, 38)
    SetChrSubChip(0x10, 0)

    label("loc_3F4E")

    WaitChrThread(0x107, 0x1)
    OP_8C(0x101, 325, 0)

    ChrTalk(    #101
        0x101,
        (
            "#1025F#4PUmmm... Thanks for saving us, Zin.\x02\x03",

            "Why are you here, though?\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x1)

    def lambda_3FAE():
        OP_6D(200, 0, 2700, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FAE)

    def lambda_3FC6():
        OP_6C(5000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FC6)
    Sleep(500)
    TurnDirection(0xF, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #102
        0xF,
        (
            "#070F#6PI stopped by the Zeiss branch and\x01",
            "Kilika began fussing at me a little.\x02\x03",

            "She told me to hurry on over to\x01",
            "Elmo to join forces with you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C9")
    OP_8C(0x11, 180, 400)

    ChrTalk(    #103
        0x11,
        (
            "#041F#6PKilika was worried, so I felt I had\x01",
            "to come too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4137")

    label("loc_40C9")

    OP_8C(0x10, 180, 400)

    ChrTalk(    #104
        0x10,
        (
            "#031F#6PAnd do you think I would miss an\x01",
            "entrance this spectacular? I simply\x01",
            "had to come as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4137")


    ChrTalk(    #105
        0x101,
        (
            "#1025F#2PSo we have Kilika to thank...\x02\x03",

            "#1016FWell, thank you, too.\x01",
            "You really saved us, there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4205")

    ChrTalk(    #106
        0x106,
        (
            "#053F#4PAll that aside...\x02\x03",

            "#555FYou actually know that psycho, Zin?\x01",
            "How's THAT shake out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4279")

    label("loc_4205")


    ChrTalk(    #107
        0x103,
        (
            "#026F#4PPutting that aside, though...\x02\x03",

            "#022FZin, you actually KNOW that psychopath?\x01",
            "How is that even possible?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_429C")
    SetChrFlags(0x11, 0x20)

    def lambda_4291():
        TurnDirection(0x11, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4291)
    Jump("loc_42AA")

    label("loc_429C")


    def lambda_42A2():
        TurnDirection(0x10, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_42A2)

    label("loc_42AA")


    ChrTalk(    #108
        0xF,
        (
            "#074F#6PHe's... He's an old acquaintance.\x02\x03",

            "#070FI'll explain in detail once we return\x01",
            "to the guild.\x02\x03",

            "With Walter's device gone, the dragon\x01",
            "veins are calming, so the hot springs\x01",
            "should cool down.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #109
        (
            "\x07\x05Estelle's group took the chance to relax in the springs once\x01",
            "they returned to the surface before going back to Zeiss...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1E46 end

    def Function_14_4423(): pass

    label("Function_14_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_443C")
    SetChrFlags(0x106, 0x8000)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 11)
    Jump("loc_4446")

    label("loc_443C")

    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 11)

    label("loc_4446")

    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Return()

    # Function_14_4423 end

    def Function_15_4455(): pass

    label("Function_15_4455")

    SetChrFlags(0x101, 0x800)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 2)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Return()

    # Function_15_4455 end

    def Function_16_4473(): pass

    label("Function_16_4473")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 5)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Return()

    # Function_16_4473 end

    def Function_17_448C(): pass

    label("Function_17_448C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44AB")
    SetChrFlags(0x104, 0x8000)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 14)
    Jump("loc_44BA")

    label("loc_44AB")

    SetChrFlags(0x105, 0x8000)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 17)

    label("loc_44BA")

    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Return()

    # Function_17_448C end

    def Function_18_44C9(): pass

    label("Function_18_44C9")

    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 21)
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x1932, 0x0, 0x852, 0x5DC, 0x0)
    Return()

    # Function_18_44C9 end

    def Function_19_44EF(): pass

    label("Function_19_44EF")


    def lambda_44F5():

        label("loc_44F5")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_44F5")

    QueueWorkItem2(0xFE, 2, lambda_44F5)
    Sleep(500)
    OP_99(0xFE, 0x3, 0x0, 0x3E8)
    Sleep(500)
    OP_44(0xFE, 0x2)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    TurnDirection(0xFE, 0xF, 400)
    Return()

    # Function_19_44EF end

    def Function_20_4535(): pass

    label("Function_20_4535")

    OP_8E(0xFE, 0x6F4, 0x0, 0x5F0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_4535 end

    def Function_21_4551(): pass

    label("Function_21_4551")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4566")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_21_4551")

    label("loc_4566")

    Return()

    # Function_21_4551 end

    def Function_22_4567(): pass

    label("Function_22_4567")

    Sleep(500)
    OP_22(0x8C, 0x0, 0x64)
    OP_8E(0xE, 0x3F2, 0x5DC, 0x83E, 0x1388, 0x0)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 39)
    OP_43(0xE, 0x0, 0x0, 0x15)
    OP_8C(0xE, 90, 400)
    OP_8F(0xE, 0x726, 0x64, 0x5FA, 0x7D0, 0x0)
    Return()

    # Function_22_4567 end

    def Function_23_45B2(): pass

    label("Function_23_45B2")

    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_45C0():
        OP_6D(390, 0, 2650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45C0)

    def lambda_45D8():
        OP_6B(500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45D8)
    Sleep(200)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_45FC():
        OP_96(0x8, 0xCEE, 0x0, 0x73A, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_45FC)
    Sleep(200)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    Fade(250)
    OP_6D(640, 0, 1950, 0)
    OP_67(0, 8980, -10000, 0)
    OP_6C(315000, 0)
    OP_6B(800, 0)
    OP_6E(872, 0)
    WaitChrThread(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 24)
    SetChrSubChip(0x8, 6)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_0D()

    ChrTalk(    #110
        0x101,
        "#1004F#5PWha--\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x6, 0x8, 0x7D0)
    OP_22(0x1FB, 0x0, 0x64)
    OP_99(0x8, 0x9, 0xC, 0x1388)
    OP_22(0x245, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)

    def lambda_46D0():
        OP_6B(900, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_46D0)
    PlayEffect(0x2, 0xFF, 0xFF, 1690, 0, 1790, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x8, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_43(0x101, 0x3, 0x0, 0x19)
    Sleep(100)
    OP_43(0xF7, 0x3, 0x0, 0x1A)
    Sleep(100)
    OP_43(0xF9, 0x3, 0x0, 0x1B)
    Sleep(100)
    OP_43(0x107, 0x3, 0x0, 0x1C)
    OP_82(0x3, 0x0)
    Return()

    # Function_23_45B2 end

    def Function_24_4773(): pass

    label("Function_24_4773")

    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4787():
        OP_6D(1640, 0, 2600, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4787)

    def lambda_479F():
        OP_67(0, 6980, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_479F)

    def lambda_47B7():
        OP_6B(820, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47B7)

    def lambda_47C7():
        OP_6C(330000, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_47C7)

    def lambda_47D7():
        OP_6E(872, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_47D7)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    Sleep(200)
    OP_7D(0x0, 0x8, 0x1E, 0xC8)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_480D():
        OP_96(0x8, 0x1090, 0xFFFFFF38, 0x780, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_480D)
    Sleep(200)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    WaitChrThread(0x8, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 30)
    SetChrSubChip(0x8, 27)
    ClearChrFlags(0x8, 0x100)
    OP_D1(8, 24000, -30000, 0, 0)
    SetChrPos(0x8, 3540, 0, 2120, 270)
    OP_51(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x280), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x280), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x280), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0x1, 0x8, 300, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x8, 400, 750, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #111 op#A
        0x101,
        "#1004F#5P#10A?!\x02",
    )

    Sleep(500)
    OP_56(0x0)
    OP_83(0x1, 0x2)

    def lambda_4923():
        OP_99(0xFE, 0x1B, 0x1E, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4923)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    Sleep(200)
    OP_22(0x245, 0x0, 0x64)

    def lambda_4943():
        OP_6D(1080, 0, 1580, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4943)

    def lambda_495B():
        OP_67(0, 7980, -10000, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_495B)

    def lambda_4973():
        OP_6C(315000, 300)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_4973)

    def lambda_4983():
        OP_D1(254, 34000, -45000, 0, 300)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4983)
    OP_7C(0xC8, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x2, 0xFF, 0xFF, 1980, 0, 1580, 0, 0, 60, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x8, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_43(0x101, 0x3, 0x0, 0x19)
    Sleep(100)
    OP_82(0x3, 0x2)
    OP_43(0xF7, 0x3, 0x0, 0x1A)
    Sleep(100)
    OP_43(0xF9, 0x3, 0x0, 0x1B)
    Sleep(100)
    OP_43(0x107, 0x3, 0x0, 0x1C)
    Return()

    # Function_24_4773 end

    def Function_25_4A41(): pass

    label("Function_25_4A41")

    SetChrPos(0x12, 2590, 0, 640, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 1)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x101, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_4A9C():
        OP_8F(0xFE, 0x6FE, 0x0, 0x3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A9C)

    def lambda_4AB7():
        OP_9E(0xFE, 0x32, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4AB7)
    Sleep(500)
    OP_82(0x1, 0x2)

    ChrTalk(    #112 op#A op#5
        0x12,
        "#1021F#10A#4PAugh!\x05\x02",
    )

    Return()

    # Function_25_4A41 end

    def Function_26_4AEC(): pass

    label("Function_26_4AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4B8D")
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 10)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x106, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_4B3D():
        OP_8F(0xFE, 0x208, 0xFFFFFFEC, 0xA78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4B3D)

    def lambda_4B58():
        OP_9E(0xFE, 0x32, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4B58)
    Sleep(500)
    OP_82(0x1, 0x2)

    ChrTalk(    #113 op#A op#5
        0x106,
        "#056F#10A#2PGuh!\x05\x02",
    )

    Jump("loc_4C24")

    label("loc_4B8D")

    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 10)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x103, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_4BD7():
        OP_8F(0xFE, 0x208, 0xFFFFFFEC, 0xA78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BD7)

    def lambda_4BF2():
        OP_9E(0xFE, 0x32, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4BF2)
    Sleep(500)
    OP_82(0x1, 0x2)

    ChrTalk(    #114 op#A op#5
        0x103,
        "#523F#10A#2PAgh!\x05\x02",
    )


    label("loc_4C24")

    Return()

    # Function_26_4AEC end

    def Function_27_4C25(): pass

    label("Function_27_4C25")

    OP_22(0x1FB, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD2")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 13)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x1, 0x2, 0x104, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_4C81():
        OP_8F(0xFE, 0xFFFFFBF0, 0xFFFFFFF6, 0x6E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C81)

    def lambda_4C9C():
        OP_9E(0xFE, 0x32, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4C9C)
    Sleep(500)
    OP_82(0x1, 0x2)

    ChrTalk(    #115 op#A op#5
        0x104,
        "#039F#10A#1PWhoa!\x05\x02",
    )

    Jump("loc_4D6B")

    label("loc_4CD2")

    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 16)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x1, 0x2, 0x105, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_4D1C():
        OP_8F(0xFE, 0xFFFFFBF0, 0xFFFFFFF6, 0x6E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D1C)

    def lambda_4D37():
        OP_9E(0xFE, 0x32, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4D37)
    Sleep(500)
    OP_82(0x1, 0x0)

    ChrTalk(    #116 op#A op#5
        0x105,
        "#541F#10A#1PAaaah!\x05\x02",
    )


    label("loc_4D6B")

    Return()

    # Function_27_4C25 end

    def Function_28_4D6C(): pass

    label("Function_28_4D6C")

    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 4)
    OP_22(0x209, 0x0, 0x64)

    def lambda_4D81():
        OP_8F(0xFE, 0x3C, 0x0, 0xFFFFFE5C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4D81)

    def lambda_4D9C():
        OP_9E(0xFE, 0x32, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_4D9C)
    Sleep(500)
    OP_82(0x1, 0x2)

    ChrTalk(    #117 op#A op#5
        0x107,
        "#068F#10A#3PWAAAAAH!\x05\x02",
    )

    Return()

    # Function_28_4D6C end

    def Function_29_4DD3(): pass

    label("Function_29_4DD3")

    SetChrFlags(0x8, 0x20)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)

    def lambda_4DEF():
        OP_8F(0xFE, 0x1978, 0x0, 0x384, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4DEF)
    OP_99(0xF, 0x4, 0x7, 0x5DC)
    OP_99(0xF, 0x4, 0x7, 0x5DC)
    OP_A2(0x0)

    def lambda_4E1F():
        OP_99(0xF, 0x8, 0xE, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4E1F)
    WaitChrThread(0xF, 0x1)
    Sleep(400)
    Return()

    # Function_29_4DD3 end

    def Function_30_4E34(): pass

    label("Function_30_4E34")

    SetChrChipByIndex(0x8, 37)
    SetChrSubChip(0x8, 2)
    Sleep(200)
    OP_43(0x8, 0x3, 0x0, 0x1F)

    label("loc_4E4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E73")
    OP_9E(0x8, 0x96, 0x0, 0x1F4, 0xFA0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4E70")
    Jump("loc_4E73")

    label("loc_4E70")

    Jump("loc_4E4A")

    label("loc_4E73")

    Sleep(400)
    PlayEffect(0x7, 0xFF, 0x8, 500, 500, 1000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_4EB3():
        OP_9E(0xFE, 0x32, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4EB3)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_22(0x22A, 0x0, 0x64)

    def lambda_4EE3():
        OP_96(0x8, 0x1BD0, 0x0, 0x28A, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4EE3)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x8, 0x2)
    Fade(100)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_30_4E34 end

    def Function_31_4F15(): pass

    label("Function_31_4F15")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F65")
    PlayEffect(0x6, 0xFF, 0x8, 500, 500, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F62")
    Jump("loc_4F65")

    label("loc_4F62")

    Jump("Function_31_4F15")

    label("loc_4F65")

    Return()

    # Function_31_4F15 end

    def Function_32_4F66(): pass

    label("Function_32_4F66")

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
        (0, "loc_4FDF"),
        (1, "loc_4FE5"),
        (SWITCH_DEFAULT, "loc_4FEB"),
    )


    label("loc_4FDF")

    OP_A2(0x1200)
    Jump("loc_4FEB")

    label("loc_4FE5")

    OP_A2(0x1201)
    Jump("loc_4FEB")

    label("loc_4FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4FF9")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4FFD")

    label("loc_4FF9")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4FFD")

    Return()

    # Function_32_4F66 end

    def Function_33_4FFE(): pass

    label("Function_33_4FFE")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5038")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_5052")

    label("loc_5038")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_5052")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_33_4FFE end

    def Function_34_5064(): pass

    label("Function_34_5064")

    TalkBegin(0xFF)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #118
        "\x07\x02There is a septium vein activator here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Flip Switch]\x01",      # 0
            "[Don't]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5107")
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)

    AnonymousTalk(    #119
        "\x07\x05...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #120
        "Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5114")

    label("loc_5107")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5114")

    label("loc_5114")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_5064 end

    SaveToFile()

Try(main)
