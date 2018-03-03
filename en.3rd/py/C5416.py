from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5416   ._SN',
        MapName             = 'Other',
        Location            = 'C5416.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Campanella',                           # 9
        "Weissmann's Staff",                    # 10
        'Light of Staff',                       # 11
        'First Anguis',                         # 12
        'Second Anguis',                        # 13
        'Fourth Anguis',                        # 14
        'Fifth Anguis',                         # 15
        'Sixth Anguis',                         # 16
        'Seventh Anguis',                       # 17
        'Grandmaster',                          # 18
        'Target Camera',                        # 19
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
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT26/CH20766 ._CH',             # 01
        'ED6_DT26/CH20485 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT26/CH20766P._CP',             # 01
        'ED6_DT26/CH20485P._CP',             # 02
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_308",          # 02, 2
        "Function_3_12DD",         # 03, 3
        "Function_4_3BAA",         # 04, 4
        "Function_5_3C0D",         # 05, 5
        "Function_6_3C24",         # 06, 6
        "Function_7_3D4A",         # 07, 7
        "Function_8_3D85",         # 08, 8
        "Function_9_3DC0",         # 09, 9
        "Function_10_3DF1",        # 0A, 10
        "Function_11_3E2C",        # 0B, 11
        "Function_12_3E67",        # 0C, 12
        "Function_13_3EA2",        # 0D, 13
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_24A")

    Return()

    # Function_0_222 end

    def Function_1_24B(): pass

    label("Function_1_24B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307")
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_72(0x801, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x802, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_72(0x804, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_72(0x805, 0x0)
    ExitThread()
    OP_72(0x2005, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_72(0x807, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 0)

    label("loc_307")

    Return()

    # Function_1_24B end

    def Function_2_308(): pass

    label("Function_2_308")

    EventBegin(0x0)
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, -100, -2940, 0)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, -100, -1940, 0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 5)
    OP_6D(1180, -100, -1600, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Fade(500)
    OP_6D(0, -1900, 2700, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(0, 0)
    OP_6E(558, 0)

    def lambda_3ED():
        OP_6D(0, 0, 4000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3ED)

    def lambda_405():
        OP_67(0, 3900, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_405)

    def lambda_41D():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_41D)

    def lambda_42D():
        OP_6E(644, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_42D)
    OP_22(0xEB, 0x0, 0x64)
    OP_43(0x13, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_43(0x14, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_43(0x19, 0x0, 0x0, 0x9)
    Sleep(500)
    OP_43(0x15, 0x0, 0x0, 0xA)
    Sleep(500)
    OP_43(0x16, 0x0, 0x0, 0xB)
    Sleep(500)
    OP_43(0x17, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x18, 0x0, 0x0, 0xD)
    Sleep(1000)
    OP_23(0xEB)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x0, 0x0)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 500, 3000, 12000, 0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -9720, 3000, 8420, 0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13850, 3000, 580, 0)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -13650, 3000, 730, 0)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -9640, 3000, -7050, 0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 9870, 3000, -7050, 0)
    Sleep(1500)

    NpcTalk(    #0
        0x17,
        "Voice",
        "#4PWe have been waiting for you...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x18,
        "Voice",
        "#3PYou have done well...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x16,
        "Voice",
        "#2PSo that is the Aureole...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x15,
        "Voice",
        "#1PSo you were able to recover it after all...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x14,
        "Voice",
        (
            "#5PStill, many sacrifices had to be made to obtain\x01",
            "it...\x02\x03",

            "We should not forget that...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x13,
        "Voice",
        (
            "#5PEveryone, be silent.\x02\x03",

            "The Grandmaster is about to make an appearance.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x79)
    Fade(500)
    OP_6D(0, -1550, 7650, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(0, 0)
    OP_6E(826, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_99(0x10, 0x0, 0x3, 0x5DC)

    def lambda_8D3():
        OP_6D(0, 8500, 16050, 3500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8D3)

    def lambda_8EB():
        OP_67(0, -2100, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8EB)

    def lambda_903():
        OP_6B(2510, 3500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_903)

    def lambda_913():
        OP_6E(864, 3500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_913)
    Sleep(500)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x140)
    Sleep(3000)
    OP_23(0xEB)
    OP_73(0x7)
    WaitChrThread(0x0, 0x0)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 800, 8000, 19010, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(1430, 2890, 5390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #6
        0x10,
        (
            "#850F#4PI, Enforcer No. 0...\x02\x03",

            "...have returned.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x19,
        "Voice",
        (
            "#5PRaise your head.\x02\x03",

            "Well, Campanella...\x02\x03",

            "...did the world move as I expected it would?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_END)), "loc_BD1")

    ChrTalk(    #8
        0x10,
        (
            "#850FWell, yes and no.\x02\x03",

            "As you foretold, the activation of the Aureole was a\x01",
            "success...\x02\x03",

            "...but due to unforeseen circumstances that occurred,\x01",
            "the Third Anguis and Enforcer No. II both journeyed to\x01",
            "the Outside.\x02\x03",

            "And as of now, No. VI and No. XV's current locations\x01",
            "are unknown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEC")

    label("loc_BD1")


    ChrTalk(    #9
        0x10,
        (
            "#850FWell, yes and no.\x02\x03",

            "As you foretold, the activation of the Aureole was a\x01",
            "success...\x02\x03",

            "...but due to unforeseen circumstances that occurred,\x01",
            "the Third Anguis and Enforcer No. II both journeyed to\x01",
            "the Outside.\x02\x03",

            "And as of now, No. VI and No. XV's current locations\x01",
            "are unknown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEC")


    NpcTalk(    #10
        0x19,
        "Voice",
        (
            "How pitiful...\x02\x03",

            "As I expected, they were unable to overcome\x01",
            "their trials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#850F#4PPlease, do not place the burden of blame upon \x01",
            "yourself.\x02\x03",

            "The victory we obtained was more than worth\x01",
            "the price we paid.\x02\x03",

            "Please accept this. Once the Aureole returns to\x01",
            "you, the Gospel Plan will be complete, after all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_6D(1180, -100, -1600, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_E78():

        label("loc_E78")

        OP_99(0xFE, 0x8, 0xF, 0x5DC)
        OP_48()
        Jump("loc_E78")

    QueueWorkItem2(0x11, 0, lambda_E78)
    Sleep(2000)
    Fade(300)
    OP_44(0x11, 0x0)
    SetChrSubChip(0x11, 5)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -600, -1940, 0)
    OP_22(0x138, 0x0, 0x64)
    LoadEffect(0x0, "monster\\ms31000.eff")
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    OP_8F(0x12, 0x0, 0x578, 0xFFFFF86C, 0x7D0, 0x0)
    PlayEffect(0x0, 0x1, 0x12, 200, 800, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_F63():
        OP_6D(7550, 2000, 23500, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_F63)

    def lambda_F7B():
        OP_67(0, 6030, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F7B)

    def lambda_F93():
        OP_6B(3830, 2500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_F93)

    def lambda_FA3():
        OP_6E(421, 2500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_FA3)
    OP_43(0x12, 0x0, 0x0, 0x6)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    NpcTalk(    #12
        0x19,
        "Voice",
        "#5PThe Aureole...has finally returned to me.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x2DF, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(2000)
    Fade(500)
    OP_6D(1430, 2890, 5390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #13
        0x19,
        "Voice",
        (
            "#5PThe bells in the West have rung, and the first of\x01",
            "the Sept-Terrions has fulfilled its role.\x02\x03",

            "So I hereby proclaim the end of the Gospel\x01",
            "Plan...\x02\x03",

            "...and the commencement of the next plan,\x01",
            "Orpheus.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_20(0x7D0)
    Fade(2000)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_72(0x801, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x802, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_72(0x804, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_72(0x805, 0x0)
    ExitThread()
    OP_72(0x2005, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_72(0x807, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_6F(0x7, 0)
    OP_6D(51430, 2890, 5390, 0)
    OP_67(0, 1920, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    SetChrPos(0x10, 50000, -100, -2940, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_6D(50770, -100, -1860, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(308, 0)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2507)
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C5401   ._SN", 100, 1, 0)
    IdleLoop()
    Return()

    # Function_2_308 end

    def Function_3_12DD(): pass

    label("Function_3_12DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    LoadEffect(0x0, "monster\\ms31000.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    SetChrPos(0x0, 0, 0, -2940, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, -100, -2940, 0)
    OP_6D(0, 0, -320, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(0, 0)
    OP_6E(558, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C8(0x200, 0x46, "C_PLAC40._CH", 0x0, 0x3E8)
    FadeToBright(2500, 0)
    OP_6B(1700, 4000)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    SetMessageWindowPos(-1, 90, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #14
        "\x07\x05We've been waiting for you...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #15
        0x10,
        "#853F#6PHeehee. Already here, I see.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x10, 0x2, 0x0, 0x4)
    Fade(500)
    OP_6D(2280, 0, 10380, 0)
    OP_67(0, 18060, -10000, 0)
    OP_6B(840, 0)
    OP_6C(308000, 0)
    OP_6E(582, 0)
    Sleep(1000)

    def lambda_147E():
        OP_6D(-780, 0, 10850, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_147E)

    def lambda_1496():
        OP_67(0, 4900, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1496)

    def lambda_14AE():
        OP_6B(1900, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_14AE)

    def lambda_14BE():
        OP_6E(582, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_14BE)

    def lambda_14CE():
        OP_6C(36000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_14CE)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)

    def lambda_14E8():
        OP_6D(-8520, 0, -2100, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_14E8)

    def lambda_1500():
        OP_67(0, 4900, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1500)

    def lambda_1518():
        OP_6B(1900, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1518)

    def lambda_1528():
        OP_6E(682, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1528)

    def lambda_1538():
        OP_6C(306000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1538)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(8520, 0, -2100, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(54000, 0)
    OP_6E(682, 0)

    def lambda_1594():
        OP_6D(0, 0, 0, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1594)

    def lambda_15AC():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_15AC)

    def lambda_15C4():
        OP_6B(2320, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_15C4)

    def lambda_15D4():
        OP_6E(964, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_15D4)

    def lambda_15E4():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_15E4)
    WaitChrThread(0x1A, 0x0)
    Sleep(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1607():
        OP_67(0, 5060, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1607)

    def lambda_161F():
        OP_6B(2620, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_161F)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-730, 0, -2029, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(1020, 0)
    OP_6C(312000, 0)
    OP_6E(795, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(400, 100, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #16
        (
            "\x07\x05...I certainly never envisioned that the\x01",
            "Faceless would perish.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #17
        (
            "\x07\x05Poor thing. All the trouble he caused his old\x01",
            "friends finally caught up with him.\x02\x03",

            "So, how exactly did he die? I'm simply dying\x01",
            "to know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #18
        0x10,
        (
            "#853FOh, I wish you could have seen it!\x02\x03",

            "#854FThe poor fellow was turned completely to salt,\x01",
            "from the top of his head to the tips of his toes.\x02\x03",

            "Then it all came crumbling down into itty bitty\x01",
            "pieces.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #19
        (
            "\x07\x05Oh, my... What a chilling way to go.\x02\x03",

            "I do wish I could have been there to witness\x01",
            "it for myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(20, 320, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #20
        (
            "\x07\x05So he fell victim to the result of that\x01",
            "singularity in North Ambria, did he?\x02\x03",

            "Ahhh, I would have loved to have seen\x01",
            "the real thing when it first appeared...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_44(0x1A, 0xFF)
    OP_44(0x10, 0xFF)
    Fade(500)
    OP_6D(-4940, 2000, 560, 0)
    OP_67(0, 3400, -10000, 0)
    OP_6B(2220, 0)
    OP_6B(2620, 0)
    OP_6C(119000, 0)
    OP_6E(706, 0)
    OP_0D()

    def lambda_1B35():
        OP_6B(2200, 25000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1B35)
    Sleep(1000)
    SetMessageWindowPos(380, 310, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #21
        (
            "\x07\x05Haha. Who'd have seen that coming?\x02\x03",

            "That guy never seemed to let his guard down\x01",
            "even for a second. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #22
        (
            "\x07\x05...I imagine it was the work of a Dominion.\x02\x03",

            "Almost certainly the fifth--the position everyone\x01",
            "previously believed to be vacant.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 310, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #23
        (
            "\x07\x05Oh, right... Guess that explains why he screwed\x01",
            "up.\x02\x03",

            "So what's the Fifth Dominion's name, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #24
        0x10,
        (
            "#853F#11PKevin Graham.\x02\x03",

            "He calls himself the Heretic Hunter,\x01",
            "and he studied under the one and\x01",
            "only Carnelia.\x02\x03",

            "#854FHeehee. Seemed like a real riot, too.\x01",
            "Twisted in all the right places.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 320, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #25
        (
            "\x07\x05He studied under Carnelia, now?\x02\x03",

            "Now I'm even more interested in him.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 310, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #26
        (
            "\x07\x05You've gotta be kidding me, Abyss.\x02\x03",

            "After how into Leonhardt you were, you're not\x01",
            "even gonna mourn his loss for more than a\x01",
            "second before setting your eyes on a new guy?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 320, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #27
        (
            "\x07\x05Oh, my... You've got me all wrong.\x02\x03",

            "I assure you that I'm mourning Leon's death in my\x01",
            "own way.\x02\x03",

            "He's not a man I'll likely ever forget...especially as\x01",
            "I could never get him to show even the slightest hint\x01",
            "of interest in me to the very end.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("Seventh Anguis")

    AnonymousTalk(    #28
        (
            "\x07\x05Indeed...\x02\x03",

            "He truly was a skilled swordsman... His loss will\x01",
            "be keenly felt.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #29
        (
            "\x07\x05He was the only one among the Enforcers who was \x01",
            "able to cross blades with you, I believe?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 20, -1, -1)
    SetChrName("Seventh Anguis")

    AnonymousTalk(    #30
        (
            "\x07\x05Certainly of those I have fought against. I often\x01",
            "asked him to humor me with my training.\x02\x03",

            "I always felt as though there was a chance he\x01",
            "may surpass me as a swordsman one day.\x02\x03",

            "It makes knowing he lost his life before having\x01",
            "a chance that much more difficult to bear.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_44(0x1A, 0xFF)
    OP_44(0x10, 0xFF)
    Fade(1000)
    OP_6D(-6200, 1000, -3100, 0)
    OP_67(0, 4090, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(41000, 0)
    OP_6E(698, 0)
    OP_0D()

    def lambda_2249():
        OP_6B(2100, 25000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2249)
    Sleep(500)
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #31
        (
            "\x07\x05Haha. In my opinion, the loss of the Bladelord\x01",
            "isn't all that significant when you look at the\x01",
            "bigger picture.\x02\x03",

            "A tiny, predictable loss in our overall combat\x01",
            "capabilities.\x02\x03",

            "Now, the loss of the Angel of Slaughter will\x01",
            "have much more of a long-term impact.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(0, 250, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #32
        (
            "\x07\x05Heh. Oh, the chick with the scythe?\x02\x03",

            "I wonder if she'll come back in the end.\x01",
            "She seemed pretty confused.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #33
        (
            "\x07\x05That's a decision for her and her alone to make.\x02\x03",

            "We may be above them in the Ouroboros hierarchy,\x01",
            "but that doesn't give us the right to order them\x01",
            "around.\x02\x03",

            "That is the way of the society.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #34
        "\x07\x05But still...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #35
        (
            "\x07\x05Professor, all of us here are well aware of the\x01",
            "importance of the Gordias series.\x02\x03",

            "But this is a law decided by the Grandmaster.\x02\x03",

            "Surely you are aware of what that means.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #36
        "\x07\x05...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(10, 80, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #37
        (
            "\x07\x05Heehee... You only need to look at Weissmann's\x01",
            "obsession with that black-haired boy to see what\x01",
            "can come from being too fixated on someone.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #38
        (
            "\x07\x05Indeed... That very obsession proved to be\x01",
            "his undoing.\x02\x03",

            "Isn't that right, Campanella?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #39
        0x10,
        (
            "#853F#12PYou could definitely argue it was one of\x01",
            "the factors that led to his failure, yes.\x02\x03",

            "#854FKevin seemed like he was trying to use it\x01",
            "to his advantage, too.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 300, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #40
        (
            "\x07\x05...All right, all right. I'll drop the issue.\x02\x03",

            "But know that as long as the Thirteen Factories\x01",
            "are in my care, the Gordias series will be of\x01",
            "unparalleled importance to me.\x02\x03",

            "So I'll be keeping an eye on her from here on to\x01",
            "observe how well the one she has is functioning.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #41
        (
            "\x07\x05Certainly. We'll leave that to you.\x02\x03",

            "I believed we've talked for long enough. The time\x01",
            "has come for the Grandmaster's advent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    Sleep(500)
    SetMessageWindowPos(360, 10, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #42
        "\x07\x05Is that so...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(10, 80, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #43
        "\x07\x05Teehee... How thrilling.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_21()
    OP_1D(0xB6)
    Fade(1000)
    OP_44(0x1A, 0xFF)
    OP_6D(0, -1550, 7650, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(0, 0)
    OP_6E(826, 0)
    OP_0D()

    def lambda_2A41():
        OP_6B(2350, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2A41)
    Sleep(500)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_99(0x10, 0x0, 0x3, 0x3E8)

    def lambda_2A6A():
        OP_6D(0, 12000, 16050, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2A6A)

    def lambda_2A82():
        OP_67(0, -2500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2A82)

    def lambda_2A9A():
        OP_6B(2510, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2A9A)

    def lambda_2AAA():
        OP_6E(864, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_2AAA)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_B0(0x7, 0x1E)
    OP_70(0x7, 0x140)
    Sleep(4500)

    def lambda_2AD6():
        OP_6D(0, 8000, 16050, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2AD6)

    def lambda_2AEE():
        OP_67(0, -2000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2AEE)
    Sleep(1000)
    OP_23(0xEB)
    OP_73(0x7)
    WaitChrThread(0x1A, 0x0)
    OP_22(0x13D, 0x0, 0x64)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)

    def lambda_2B5A():
        OP_6D(5710, 1250, 13110, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2B5A)

    def lambda_2B72():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2B72)

    def lambda_2B8A():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2B8A)

    def lambda_2B9A():
        OP_6E(940, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_2B9A)

    def lambda_2BAA():
        OP_6C(44000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2BAA)
    WaitChrThread(0x1A, 0x0)
    Sleep(500)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(220, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "#7C#40WI see you have all gathered.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(150, 260, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #45
        (
            "\x07\x05Yes, Grandmaster.\x02\x03",

            "With the exception of the Third Anguis,\x01",
            "all are present and accounted for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(220, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "#7C#40WVery good.#0C\x02\x03",

            "You deserve my thanks for observing all that\x01",
            "transpired as my representative, Campanella.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #47
        0x10,
        (
            "#853F#11PI'm pleased to hear as much, Grandmaster.\x02\x03",

            "#853FI imagine you are already aware of what transpired\x01",
            "during the Gospel Plan even without me relaying\x01",
            "the details...\x02\x03",

            "...but allow me to fulfill my most important duty.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(1380, 0, 820, 0)
    OP_67(0, 3860, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(35000, 0)
    OP_6E(493, 0)
    OP_0D()
    OP_99(0x10, 0x3, 0x5, 0x3E8)
    Sleep(500)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, -100, -740, 90)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 8)

    def lambda_2ECB():

        label("loc_2ECB")

        OP_99(0xFE, 0x8, 0xF, 0x4B0)
        OP_48()
        Jump("loc_2ECB")

    QueueWorkItem2(0x11, 1, lambda_2ECB)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x11, 0, 600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2F1D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2F1D)
    WaitChrThread(0x11, 0x2)
    OP_83(0x1, 0x2)
    Sleep(3000)
    Fade(500)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x0)
    SetChrSubChip(0x11, 5)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -600, -740, 0)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)

    def lambda_2FAF():
        OP_6D(1380, 500, 820, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2FAF)
    OP_8F(0x12, 0x0, 0x578, 0xFFFFFD1C, 0x3E8, 0x0)
    PlayEffect(0x0, 0x1, 0x12, 200, 800, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x1A, 0x0)
    Sleep(500)
    SetMessageWindowPos(400, 50, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #48
        "\x07\x05Oh, my!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 200, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #49
        "\x07\x05So that's...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(70, 320, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #50
        "\x07\x05That's the Aureole!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)

    def lambda_30A4():
        OP_6D(7550, 2000, 23500, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_30A4)

    def lambda_30BC():
        OP_67(0, 6030, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_30BC)

    def lambda_30D4():
        OP_6B(3830, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_30D4)

    def lambda_30E4():
        OP_6E(421, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_30E4)

    def lambda_30F4():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_30F4)
    OP_43(0x12, 0x0, 0x0, 0x6)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x12, 200, 800, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x2DF, 0x0, 0x64)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(2000)
    Fade(500)
    OP_6D(5710, 1250, 13110, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(44000, 0)
    OP_6E(940, 0)
    OP_0D()
    Sleep(300)

    def lambda_31B1():
        OP_6D(1430, 2490, 5390, 30000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_31B1)

    def lambda_31C9():
        OP_67(0, 1920, -10000, 30000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_31C9)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        (
            "#7C#40WThank you.\x02\x03",

            "If only the price we paid to obtain it weren't\x01",
            "so great...\x02\x03",

            "Weissmann... Leonhardt...\x02\x03",

            "To say nothing of the countless other sacrifices,\x01",
            "both human and otherwise that arose through\x01",
            "this plan...\x02\x03",

            "I, and I alone, bear responsibility for each and \x01",
            "every one of them.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(370, 150, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #52
        "\x07\x05Th-That is simply not true!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(430, 250, -1, -1)
    SetChrName("Seventh Anguis")

    AnonymousTalk(    #53
        (
            "\x07\x05Please, do not place the burden of blame upon\x01",
            "yourself.\x02\x03",

            "The Faceless alone was at fault for his death.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(20, 280, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #54
        (
            "\x07\x05But if anyone should take the blame, it's we\x01",
            "Anguis who chose to overlook his behavior\x01",
            "rather than steer him back on the right track.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "#7C#40WNo... I half expected that this is what would\x01",
            "happen.\x02\x03",

            "Yet I chose to leave all of the decisions in his\x01",
            "hands.\x02\x03",

            "I did so because I believed that to be necessary\x01",
            "for this world, but nonetheless...\x02\x03",

            "...the blame is unequivocally mine.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(370, 150, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #56
        "\x07\x05Oh, Grandmaster...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(420, 250, -1, -1)
    SetChrName("Seventh Anguis")

    AnonymousTalk(    #57
        "\x07\x05Why must you blame yourself so?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "#7C#40W...\x02\x03",

            "There will inevitably be a reaction to what has\x01",
            "happened in time...\x02\x03",

            "...but I imagine the church will act regarding that.\x02\x03",

            "Let us leave the matter to them.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    SetMessageWindowPos(150, 250, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #59
        "\x07\x05...As you wish.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(220, 340, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #60
        (
            "\x07\x05Haha... I must admit that my curiosity is piqued,\x01",
            "but it shall be as you desire.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(30, 320, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #61
        "\x07\x05In that case, what should all of us do now?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #62
        "#7C#40W...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(1000)
    OP_44(0x1A, 0xFF)
    OP_6D(0, 7500, 8680, 0)
    OP_67(0, -1860, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(0, 0)
    OP_6E(940, 0)
    OP_0D()

    def lambda_38BF():
        OP_6B(3150, 20000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_38BF)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "#7C#40WThe bells in the west have rang, and the\x01",
            "first pact applies no more.#0C\x02\x03",

            "I hereby proclaim the completion of the\x01",
            "first phase of the Orpheus Final Plan,\x01",
            "the Gospel Plan...#0C\x02\x03",

            "...and the initiation of its second phase,\x01",
            "the Phantasmal Blaze Plan.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    SetMessageWindowPos(380, 275, -1, -1)
    SetChrName("Fifth Anguis")

    AnonymousTalk(    #64
        "\x07\x05Very well!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(20, 200, -1, -1)
    SetChrName("Second Anguis")

    AnonymousTalk(    #65
        "\x07\x05Heehee...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 280, -1, -1)
    SetChrName("Sixth Anguis")

    AnonymousTalk(    #66
        "\x07\x05Leave everything to us.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 340, -1, -1)
    SetChrName("Fourth Anguis")

    AnonymousTalk(    #67
        "\x07\x05We, your loyal Anguis...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 280, -1, -1)
    SetChrName("Seventh Anguis")

    AnonymousTalk(    #68
        "\x07\x05...in accordance with your wishes...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("First Anguis")

    AnonymousTalk(    #69
        (
            "\x07\x05...shall now fully devote ourselves to\x01",
            "the execution of your plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(3000, 16777215, -1)
    OP_0D()
    OP_20(0x1388)
    OP_AD(0x240184, 0x0, 0x0, 0x5DC)
    OP_21()
    Sleep(500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5401   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_3_12DD end

    def Function_4_3BAA(): pass

    label("Function_4_3BAA")

    OP_43(0x13, 0x3, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x7)
    Sleep(3000)
    OP_43(0x14, 0x0, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x15, 0x0, 0x0, 0xA)
    Sleep(1000)
    OP_43(0x17, 0x0, 0x0, 0xC)
    Sleep(4000)
    OP_43(0x19, 0x0, 0x0, 0x9)
    Sleep(1000)
    OP_43(0x16, 0x0, 0x0, 0xB)
    Sleep(1000)
    OP_43(0x18, 0x0, 0x0, 0xD)
    Sleep(5000)
    OP_44(0x13, 0x3)
    OP_23(0xBA)
    Return()

    # Function_4_3BAA end

    def Function_5_3C0D(): pass

    label("Function_5_3C0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C23")
    OP_22(0xBA, 0x0, 0x64)
    Sleep(6000)
    Jump("Function_5_3C0D")

    label("loc_3C23")

    Return()

    # Function_5_3C0D end

    def Function_6_3C24(): pass

    label("Function_6_3C24")


    def lambda_3C2A():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C2A)
    Sleep(500)

    def lambda_3C4A():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C4A)
    Sleep(500)

    def lambda_3C6A():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C6A)
    Sleep(500)

    def lambda_3C8A():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C8A)
    Sleep(500)

    def lambda_3CAA():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CAA)
    Sleep(1500)

    def lambda_3CCA():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CCA)
    Sleep(500)

    def lambda_3CEA():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CEA)
    Sleep(400)

    def lambda_3D0A():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D0A)
    Sleep(300)

    def lambda_3D2A():
        OP_8F(0xFE, 0x320, 0x1F40, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D2A)
    Sleep(200)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_3C24 end

    def Function_7_3D4A(): pass

    label("Function_7_3D4A")

    OP_6F(0x0, 0)
    OP_B0(0x0, 0x1E)
    OP_70(0x0, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x0)
    Return()

    # Function_7_3D4A end

    def Function_8_3D85(): pass

    label("Function_8_3D85")

    OP_6F(0x1, 0)
    OP_B0(0x1, 0x1E)
    OP_70(0x1, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x1)
    Return()

    # Function_8_3D85 end

    def Function_9_3DC0(): pass

    label("Function_9_3DC0")

    OP_6F(0x2, 0)
    OP_B0(0x2, 0x1E)
    OP_70(0x2, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_73(0x2)
    Return()

    # Function_9_3DC0 end

    def Function_10_3DF1(): pass

    label("Function_10_3DF1")

    OP_6F(0x3, 0)
    OP_B0(0x3, 0x1E)
    OP_70(0x3, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x3)
    Return()

    # Function_10_3DF1 end

    def Function_11_3E2C(): pass

    label("Function_11_3E2C")

    OP_6F(0x4, 0)
    OP_B0(0x4, 0x1E)
    OP_70(0x4, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x4)
    Return()

    # Function_11_3E2C end

    def Function_12_3E67(): pass

    label("Function_12_3E67")

    OP_6F(0x5, 0)
    OP_B0(0x5, 0x1E)
    OP_70(0x5, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x5)
    Return()

    # Function_12_3E67 end

    def Function_13_3EA2(): pass

    label("Function_13_3EA2")

    OP_6F(0x6, 0)
    OP_B0(0x6, 0x1E)
    OP_70(0x6, 0x140)
    Sleep(4900)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(700)
    OP_22(0x2D8, 0x0, 0x64)
    OP_73(0x6)
    Return()

    # Function_13_3EA2 end

    SaveToFile()

Try(main)
