from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7207   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7207.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'Schwarzritter',                        # 9
        'Arachne Graia',                        # 10
        'Arachne Evros',                        # 11
        'Arachne Thaleia',                      # 12
        'Sealing Stone 15',                     # 13
        'Dummy Character 1',                    # 14
        'Dummy Character 2',                    # 15
        'Dummy Character 3',                    # 16
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
        'ED6_DT29/CH14320 ._CH',             # 00
        'ED6_DT26/CH20668 ._CH',             # 01
        'ED6_DT27/CH04450 ._CH',             # 02
        'ED6_DT27/CH04455 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH14320P._CP',             # 00
        'ED6_DT26/CH20668P._CP',             # 01
        'ED6_DT27/CH04450P._CP',             # 02
        'ED6_DT27/CH04455P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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


    DeclEvent(
        X                   = -3830,
        Y                   = -1000,
        Z                   = 34110,
        Range               = 4210,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x8EE4,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -5060,
        Y                   = -1000,
        Z                   = 76030,
        Range               = 4750,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x13560,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_23D",          # 01, 1
        "Function_2_255",          # 02, 2
        "Function_3_26B",          # 03, 3
        "Function_4_123F",         # 04, 4
        "Function_5_12EE",         # 05, 5
        "Function_6_13A2",         # 06, 6
        "Function_7_1456",         # 07, 7
        "Function_8_14B1",         # 08, 8
        "Function_9_1511",         # 09, 9
        "Function_10_1571",        # 0A, 10
        "Function_11_15BF",        # 0B, 11
        "Function_12_160D",        # 0C, 12
        "Function_13_165B",        # 0D, 13
        "Function_14_16A4",        # 0E, 14
        "Function_15_31BD",        # 0F, 15
        "Function_16_3296",        # 10, 16
        "Function_17_3EC5",        # 11, 17
        "Function_18_4037",        # 12, 18
        "Function_19_4115",        # 13, 19
        "Function_20_41E2",        # 14, 20
        "Function_21_42F8",        # 15, 21
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_21D")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_21D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_235"),
        (SWITCH_DEFAULT, "loc_23C"),
    )


    label("loc_235")

    Event(0, 18)
    Jump("loc_23C")

    label("loc_23C")

    Return()

    # Function_0_20A end

    def Function_1_23D(): pass

    label("Function_1_23D")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFEA840, 0x230092)
    OP_1B(0x1, 0x0, 0x13)
    Return()

    # Function_1_23D end

    def Function_2_255(): pass

    label("Function_2_255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_262")
    Return()

    label("loc_262")

    Call(0, 3)
    Call(0, 14)
    Return()

    # Function_2_255 end

    def Function_3_26B(): pass

    label("Function_3_26B")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp298_00.eff")
    LoadEffect(0x1, "map\\mp298_01.eff")
    LoadEffect(0x2, "map\\mp302_00.eff")
    OP_E0(238, 0x44, 0x2)
    OP_E0(238, 0x45, 0x3)
    OP_E0(239, 0x46, 0x2)
    OP_E0(239, 0x47, 0x3)
    OP_E0(240, 0x48, 0x2)
    OP_E0(240, 0x49, 0x3)
    OP_E0(241, 0x4A, 0x2)
    OP_E0(241, 0x4B, 0x3)
    OP_E0(238, 0x4C, 0x4)
    OP_E0(239, 0x4D, 0x4)
    OP_E0(240, 0x4E, 0x4)
    OP_E0(241, 0x4F, 0x4)
    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)

    ChrTalk(    #0
        0x101,
        "#1004F#12POooh!\x02",
    )

    CloseMessageWindow()

    def lambda_319():
        OP_6D(0, 200, 93630, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_319)

    def lambda_331():
        OP_67(0, 8750, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_331)

    def lambda_349():
        OP_6B(5650, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_349)

    def lambda_359():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_359)

    def lambda_369():
        OP_6E(327, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_369)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)
    SetChrPos(0x10F, -870, -400, 54030, 0)
    SetChrPos(0x101, 1110, -400, 54610, 0)
    SetChrPos(0xF0, -1030, -400, 51900, 0)
    SetChrPos(0xF1, 1030, -400, 52150, 0)
    Fade(500)
    OP_6D(1700, -400, 54800, 0)
    OP_67(0, 4470, -10000, 0)
    OP_6B(4800, 0)
    OP_6C(45000, 0)
    OP_6E(178, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x101,
        (
            "#1006F#5PIs that our exit out of this plane?\x02\x03",

            "Doesn't look like there's anything standing\x01",
            "between us and it, either. Time to make a\x01",
            "mad dash for the--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10F,
        "#1443F#6PWait.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #3
        0x101,
        "#1004F#11PWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10F,
        (
            "#1445F#6PI can smell the distinctive scent of the \x01",
            "underworld.\x02\x03",

            "And it grows stronger by the second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1020F#11PWhat?!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_5A4():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5A4)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)

    def lambda_5C6():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5C6)
    SetChrChipByIndex(0xF0, 8)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_5E8():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_5E8)
    SetChrChipByIndex(0xF1, 10)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#1002F#5PAre we gonna get surrounded by magic circles,\x01",
            "then?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        "#1441F#6PNo. This isn't going to come from a circle...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x10F,
        "#1449F#6PIt's coming from above!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76C")

    label("loc_705")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76C")

    label("loc_72D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76C")

    label("loc_755")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_76C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_800")

    label("loc_799")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_800")

    label("loc_7C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_800")

    label("loc_7E9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_800")

    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)
    FadeToDark(300, 16777215, -1)

    def lambda_81A():
        OP_6D(1700, 6000, 54800, 600)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_81A)
    WaitChrThread(0x10F, 0x3)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(-1820, 11100, 50880, 0)
    OP_67(0, 500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(57000, 0)
    OP_6E(200, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_888():

        label("loc_888")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_888")

    QueueWorkItem2(0x10F, 2, lambda_888)
    OP_1D(0x9A)
    FadeToBright(500, 16777215)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_43(0x12, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x6)
    OP_43(0x15, 0x0, 0x0, 0x7)
    OP_43(0x16, 0x0, 0x0, 0x8)
    OP_43(0x17, 0x0, 0x0, 0x9)
    Sleep(1000)

    def lambda_8DE():
        OP_6D(-1820, 5100, 50880, 9500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_8DE)

    def lambda_8F6():
        OP_67(0, 6460, -10000, 9500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_8F6)

    def lambda_90E():
        OP_6B(4500, 9500)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_90E)

    def lambda_91E():
        OP_6E(220, 9500)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_91E)
    Sleep(5500)
    OP_43(0x10F, 0x0, 0x0, 0xA)
    OP_43(0x101, 0x0, 0x0, 0xB)
    OP_43(0xF0, 0x0, 0x0, 0xC)
    OP_43(0xF1, 0x0, 0x0, 0xD)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(1000)
    Fade(500)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)
    OP_6D(0, -700, 57300, 0)
    OP_67(0, 2290, -10000, 0)
    OP_6B(4720, 0)
    OP_6C(0, 0)
    OP_6E(210, 0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_44(0x10F, 0x2)
    OP_23(0x85)
    Sleep(500)

    ChrTalk(    #9
        0x101,
        "#1020F#6PWh-Wh-Wh-Wha...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A17")

    ChrTalk(    #10
        0x108,
        "#077F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_A17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3F")

    ChrTalk(    #11
        0x10D,
        "#271F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_A3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A67")

    ChrTalk(    #12
        0x10C,
        "#114F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8F")

    ChrTalk(    #13
        0x10E,
        "#177F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB7")

    ChrTalk(    #14
        0x106,
        "#054F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_AB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE0")

    ChrTalk(    #15
        0x103,
        "#1524F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B09")

    ChrTalk(    #16
        0x102,
        "#1506F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_B09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B32")

    ChrTalk(    #17
        0x104,
        "#1550F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_B32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5C")

    ChrTalk(    #18
        0x107,
        "#065F#6PS-Spiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B86")

    ChrTalk(    #19
        0x10B,
        "#216F#6PS-Spiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_B86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAF")

    ChrTalk(    #20
        0x105,
        "#1166F#6PSpiders?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_BAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD5")

    ChrTalk(    #21
        0x10A,
        "#1317F#6PSpiders?!\x02",
    )

    CloseMessageWindow()

    label("loc_BD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")

    ChrTalk(    #22
        0x110,
        (
            "#1306F#6PAww. How cute. They're trying so hard\x01",
            "to be intimidating for us, aren't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB3")

    ChrTalk(    #23
        0x10A,
        (
            "#1317F#6POn a scale of cute to creepy, these things\x01",
            "definitely weigh in heavy on creepy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE6")

    ChrTalk(    #24
        0x105,
        "#1162F#6PGoddess, help us...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D25")

    ChrTalk(    #25
        0x10B,
        "#216F#6PW-We have to beat THESE things?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(    #26
        0x107,
        "#065F#6PTh-This is terrible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_D58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA6")

    ChrTalk(    #27
        0x104,
        "#1550F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_DA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF4")

    ChrTalk(    #28
        0x102,
        "#1506F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E42")

    ChrTalk(    #29
        0x103,
        "#1524F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8F")

    ChrTalk(    #30
        0x106,
        "#054F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_E8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDC")

    ChrTalk(    #31
        0x10E,
        "#177F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F29")

    ChrTalk(    #32
        0x10C,
        "#114F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F73")

    label("loc_F29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F73")

    ChrTalk(    #33
        0x10D,
        "#271F#6PUgh... So these are this plane's final devils.\x02",
    )

    CloseMessageWindow()

    label("loc_F73")

    Sleep(500)

    ChrTalk(    #34
        0x10F,
        (
            "#1446F#6PThese are the three gluttonous Arachne sisters, \x01",
            "kin of the seventy-seven devils featured in the\x01",
            "Testaments!\x02\x03",

            "#1441FThey weave nightmares and consume the souls\x01",
            "of those who wander into their labyrinth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1002F#6PSo this is what real devils are like, huh?\x01",
            "They sure look the part.\x02\x03",

            "#1005FBut they're not gonna be enough to stop us!\x01",
            "Let's get nasty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        "#1449F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_22(0x148, 0x0, 0x64)

    def lambda_1106():

        label("loc_1106")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_1106")

    QueueWorkItem2(0x11, 3, lambda_1106)
    Sleep(30)
    OP_22(0x148, 0x0, 0x64)

    def lambda_1123():

        label("loc_1123")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_1123")

    QueueWorkItem2(0x12, 3, lambda_1123)
    Sleep(30)
    OP_22(0x148, 0x0, 0x64)

    def lambda_1140():

        label("loc_1140")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_1140")

    QueueWorkItem2(0x13, 3, lambda_1140)
    Sleep(500)

    def lambda_1158():
        OP_6D(0, -250, 58250, 300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1158)

    def lambda_1170():
        OP_67(0, 2210, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1170)

    def lambda_1188():
        OP_6B(5220, 300)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_1188)

    def lambda_1198():
        OP_6E(139, 300)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_1198)

    def lambda_11A8():
        OP_8F(0xFE, 0xFFFFFDB2, 0xFFFFFE70, 0xD00C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_11A8)
    Sleep(10)

    def lambda_11C8():
        OP_8F(0xFE, 0x294, 0xFFFFFE70, 0xD048, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C8)
    Sleep(10)

    def lambda_11E8():
        OP_8F(0xFE, 0xFFFFF9E8, 0xFFFFFE70, 0xCA26, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_11E8)
    Sleep(10)

    def lambda_1208():
        OP_8F(0xFE, 0x708, 0xFFFFFE70, 0xCC7E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1208)
    WaitChrThread(0x10F, 0x3)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF0, 0x3)
    WaitChrThread(0xF1, 0x3)
    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_26B end

    def Function_4_123F(): pass

    label("Function_4_123F")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 14000, 50840, 180)
    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1292():

        label("loc_1292")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1292")

    QueueWorkItem2(0xFE, 3, lambda_1292)
    PlayEffect(0x2, 0x3, 0xFE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFCB44, 0x0, 0x5DC, 0x0)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_4_123F end

    def Function_5_12EE(): pass

    label("Function_5_12EE")

    Sleep(150)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2300, 16000, 52450, 180)
    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1346():

        label("loc_1346")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1346")

    QueueWorkItem2(0xFE, 3, lambda_1346)
    PlayEffect(0x2, 0x4, 0xFE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC568, 0x0, 0x640, 0x0)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_5_12EE end

    def Function_6_13A2(): pass

    label("Function_6_13A2")

    Sleep(400)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2300, 15000, 53500, 180)
    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_13FA():

        label("loc_13FA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13FA")

    QueueWorkItem2(0xFE, 3, lambda_13FA)
    PlayEffect(0x2, 0x5, 0xFE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC950, 0x0, 0x640, 0x0)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_6_13A2 end

    def Function_7_1456(): pass

    label("Function_7_1456")

    SetChrPos(0x15, 0, 15000, 51000, 0)
    PlayEffect(0x1, 0x0, 0x15, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFCD38, 0x0, 0x5DC, 0x0)
    Return()

    # Function_7_1456 end

    def Function_8_14B1(): pass

    label("Function_8_14B1")

    Sleep(150)
    SetChrPos(0x16, -2300, 17000, 52650, 0)
    PlayEffect(0x1, 0x1, 0x16, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC180, 0x0, 0x5DC, 0x0)
    Return()

    # Function_8_14B1 end

    def Function_9_1511(): pass

    label("Function_9_1511")

    Sleep(400)
    SetChrPos(0x17, 2300, 16000, 53700, 0)
    PlayEffect(0x1, 0x2, 0x17, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC568, 0x0, 0x5DC, 0x0)
    Return()

    # Function_9_1511 end

    def Function_10_1571(): pass

    label("Function_10_1571")

    Sleep(140)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1592():
        OP_96(0xFE, 0xFFFFFD58, 0xFFFFFE70, 0xB716, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1592)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_10_1571 end

    def Function_11_15BF(): pass

    label("Function_11_15BF")

    Sleep(80)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_15E0():
        OP_96(0xFE, 0x3C0, 0xFFFFFE70, 0xB810, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15E0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_15BF end

    def Function_12_160D(): pass

    label("Function_12_160D")

    Sleep(30)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_162E():
        OP_96(0xFE, 0xFFFFFB14, 0xFFFFFE70, 0xAE88, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_162E)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_160D end

    def Function_13_165B(): pass

    label("Function_13_165B")

    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1677():
        OP_96(0xFE, 0x5A0, 0xFFFFFE70, 0xAE7E, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1677)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_13_165B end

    def Function_14_16A4(): pass

    label("Function_14_16A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10F, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xF0, 0x1)
    OP_44(0xF1, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    LoadEffect(0x3, "map\\mp263_00.eff")
    LoadEffect(0x4, "map\\mp263_01.eff")
    OP_E0(238, 0x44, 0x5)
    OP_E0(239, 0x45, 0x5)
    OP_E0(240, 0x46, 0x5)
    OP_E0(241, 0x47, 0x5)
    SetChrPos(0x10F, -800, -400, 52050, 0)
    SetChrPos(0x101, 930, -400, 51930, 0)
    SetChrPos(0xF0, -1130, -400, 50190, 0)
    SetChrPos(0xF1, 1060, -400, 50160, 0)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 3)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0xF0, 6)
    SetChrSubChip(0xF0, 3)
    SetChrChipByIndex(0xF1, 7)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xEE, 0x800)
    SetChrFlags(0xEF, 0x800)
    SetChrFlags(0xF0, 0x800)
    SetChrFlags(0xF1, 0x800)
    OP_43(0xEE, 0x0, 0x0, 0xF)
    OP_43(0xEF, 0x0, 0x0, 0xF)
    OP_43(0xF0, 0x0, 0x0, 0xF)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    OP_6D(770, -400, 50900, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(135000, 0)
    OP_6E(168, 0)

    def lambda_1824():
        OP_6B(4850, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1824)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x2)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        (
            "#1007F#5P*pant*...*pant*...\x02\x03",

            "#1019FWhat was up with that last one?\x01",
            "That was so unfair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        (
            "#1446F#6PThat must have been Zigma, the three\x01",
            "sisters' mother.\x02\x03",

            "#1806FAnd even she was not able to stop us,\x01",
            "thankfully.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x10F, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xEE, 0x0)
    Sleep(50)
    OP_62(0x101, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xEF, 0x0)
    Sleep(50)
    OP_62(0xF0, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xF0, 0x0)
    Sleep(50)
    OP_62(0xF1, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xF1, 0x0)
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 180, 800, 55300, 0)
    PlayEffect(0x3, 0x6, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    ClearChrFlags(0x0, 0x800)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    ClearChrFlags(0x1, 0x800)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    ClearChrFlags(0x2, 0x800)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x3, 0x800)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x10F,
        "#1444F#11P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1004F#5PTh-That looks like...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1AF2():
        OP_6D(1200, -400, 53000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1AF2)

    def lambda_1B0A():
        OP_67(0, 4890, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1B0A)
    OP_8F(0x10F, 0x8C, 0xFFFFFE70, 0xD2DC, 0x3E8, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x14, 0x82, 0x320, 0xD57A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    SetChrFlags(0x14, 0x80)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05Found \x1F\x60\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x360, 1)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #42
        0x101,
        (
            "#1002F#11PAnother sealing stone, huh?\x02\x03",

            "I honestly figured Renne's was gonna be the\x01",
            "last.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFE")

    ChrTalk(    #43
        0x110,
        (
            "#265FHuh... So I was in a pretty stone like that\x01",
            "when you found me, too?\x02\x03",

            "#261FI feel like a princess in a fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1016F#5PAhaha... You kinda were like a little princess,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFE")


    ChrTalk(    #45
        0x10F,
        (
            "#1443F#5P...\x02\x03",

            "#1446FI think this one may actually be different.\x02\x03",

            "The other stones had a strange sense of\x01",
            "warmth when you held them. Not so for\x01",
            "this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1004F#11PReally?\x02\x03",

            "#1015FIs it 'cause it has something bad in it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DE9():
        OP_6D(920, -400, 51870, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1DE9)
    OP_8C(0x10F, 180, 400)
    WaitChrThread(0x10F, 0x1)

    ChrTalk(    #47
        0x10F,
        (
            "#1448F#6PNo... Instead of the usual warmth, it seems to\x01",
            "have a cool, almost divine feel to it.\x02\x03",

            "Almost as if it might contain the Goddess Herself\x01",
            "within.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 64500, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #48
        0x10,
        "Man's Voice",
        "\x07\x05#2PHeh. Sharp as usual.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F59")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FC0")

    label("loc_1F59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F81")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FC0")

    label("loc_1F81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FC0")

    label("loc_1FA9")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1FC0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FED")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2054")

    label("loc_1FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2015")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2054")

    label("loc_2015")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2054")

    label("loc_203D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2054")

    Sleep(1000)

    def lambda_205F():
        OP_6D(600, 0, 64000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_205F)

    def lambda_2077():
        OP_67(0, 5770, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2077)

    def lambda_208F():
        OP_6B(4380, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_208F)

    def lambda_209F():
        OP_6E(186, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_209F)
    OP_8C(0x10F, 0, 600)
    WaitChrThread(0x10F, 0x0)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0, 100, 64500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    OP_0D()
    Sleep(1000)
    OP_1D(0xB0)
    Fade(1000)
    OP_6D(1100, 0, 65400, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(4380, 0)
    OP_6C(45000, 0)
    OP_6E(186, 0)

    def lambda_2144():
        OP_6B(4100, 500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2144)

    def lambda_2154():
        OP_6E(185, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2154)
    PlayEffect(0x1, 0x1, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2199():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2199)
    OP_22(0x59, 0x0, 0x64)
    OP_23(0xBA)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21DB")

    ChrTalk(    #49
        0x102,
        "#1502F#1POh...\x02",
    )

    CloseMessageWindow()

    label("loc_21DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2203")

    ChrTalk(    #50
        0x110,
        "#264F#1PHe's here...\x02",
    )

    CloseMessageWindow()

    label("loc_2203")


    ChrTalk(    #51
        0x101,
        "#1004F#1PWho's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        (
            "#1441F#1PSo you decided to show your face again,\x01",
            "did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "\x07\x05#1591F#5PHaha. The priest is still unconscious, I see.\x01",
            "What a shame.\x02\x03",

            "I was rather surprised to find out that he can\x01",
            "only use his Stigma's power against heretics.\x02\x03",

            "Even power of that magnitude is meaningless\x01",
            "if it's so limited and has such repercussions...\x01",
            "I almost pity him.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1445F#1P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-30, -200, 61510, 0)
    OP_67(0, 2350, -10000, 0)
    OP_6B(4300, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x10F, -490, -400, 53000, 0)
    SetChrPos(0x101, 500, -400, 52130, 0)
    SetChrPos(0xF0, -1090, -400, 49800, 0)
    SetChrPos(0xF1, 1030, -400, 49700, 0)
    SetChrPos(0x10, 0, 0, 63820, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x10,
        (
            "\x07\x05#1591F#5PTo tell you the truth, I wasn't expecting you to\x01",
            "reach this point so quickly.\x02\x03",

            "Your final piece is inordinately capable.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25DD")

    ChrTalk(    #56
        0x110,
        "#1306F#6POh? Might you be referring to me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "\x07\x05#1591F#5PThanks to you, I ended up having to make my\x01",
            "appearance sooner than I was expecting.\x02\x03",

            "I suppose I should have expected no less from\x01",
            "the host of Grancel's finest tea party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x110,
        "#263F#6PTeehee. That's very true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DD")

    label("loc_25DD")


    ChrTalk(    #59
        0x101,
        "#1002F#6PDo you mean Renne?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "\x07\x05#1591F#5PThanks to her, I ended up having to make my\x01",
            "appearance sooner than I was expecting.\x02\x03",

            "I should have assumed no less from the host\x01",
            "of Grancel's finest tea party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1026F#6PHow do you know about that...?\x02",
    )

    CloseMessageWindow()

    label("loc_26DD")


    ChrTalk(    #62
        0x10,
        (
            "\x07\x05#1591F#5PRegardless, I came to fulfill a duty, and fulfill\x01",
            "it I shall.\x02\x03",

            "Think of that stone as a gift for gathering all\x01",
            "the pieces scattered throughout Phantasma.\x02\x03",

            "It contains not an additional piece, but a rule\x01",
            "book of sorts that you may find beneficial.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1002F#6PA rule book?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10F,
        (
            "#1446F#6PThat certainly explains why it feels different\x01",
            "compared to the others.\x02\x03",

            "#1443FCould this mean that you're finally ready to face\x01",
            "us head on rather than continuously taunting us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "\x07\x05#1591F#5PWhether that time comes is entirely up to you.\x02\x03",

            "For now, all I will say is this:\x02\x03",

            "On the next game board, all of you will find\x01",
            "yourselves face to face with a number of trials\x01",
            "to overcome.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)

    def lambda_29AD():

        label("loc_29AD")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_29AD")

    QueueWorkItem2(0x10, 3, lambda_29AD)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 0, 0, 63820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x1, 0xFF, 0, 0, 63820, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A92")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF9")

    label("loc_2A92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF9")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF9")

    label("loc_2AE2")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2AF9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B26")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8D")

    label("loc_2B26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8D")

    label("loc_2B4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B76")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8D")

    label("loc_2B76")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B8D")

    Sleep(1000)

    ChrTalk(    #66
        0x10F,
        "#1449F#6PHe's escaping again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1005F#6PW-Wait a damn minute!\x02\x03",

            "Is that all you've got to say?\x01",
            "What kind of trials?!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    Fade(250)
    OP_44(0x10, 0x3)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #68
        0x10,
        (
            "\x07\x05#1591F#5PHeh. A variety in all shapes and sizes.\x02\x03",

            "Even I will be one of them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1020F#6PYou?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CB7")

    ChrTalk(    #70
        0x102,
        "#1503F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_2CB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CE2")

    ChrTalk(    #71
        0x110,
        "#262F#6P...Really, now?\x02",
    )

    CloseMessageWindow()

    label("loc_2CE2")


    ChrTalk(    #72
        0x10,
        (
            "\x07\x05#1590F#5PI eagerly anticipate seeing whether you are able\x01",
            "to overcome them all and make it to me.\x02\x03",

            "#1591FDon't disappoint me, now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x2, 0xFF, 0, 0, 63820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2DA9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2DA9)
    OP_22(0x59, 0x0, 0x64)
    OP_23(0xBA)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_20(0x7D0)
    Sleep(2000)
    Fade(1000)
    OP_6D(1880, -400, 56000, 0)
    OP_67(0, 4000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(44000, 0)
    OP_6E(185, 0)

    def lambda_2E15():
        OP_6D(1850, -400, 53600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2E15)
    SetChrPos(0x10F, -240, -400, 53860, 0)
    SetChrPos(0x101, 730, -400, 52100, 0)
    SetChrPos(0xF0, -1130, -400, 50090, 0)
    SetChrPos(0xF1, 1260, -400, 50260, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #73
        0x101,
        (
            "#1020F#11POh...\x02\x03",

            "#1026F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10F,
        (
            "#1446F#5PIt's almost as if he can't help but try to taunt us.\x02\x03",

            "#1445FHe stays just long enough to say something cryptic\x01",
            "and then leaves before elaborating every single\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1007F#11POh, I just love those types...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F92")

    ChrTalk(    #76
        0x102,
        "#1503F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_2F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB1")

    ChrTalk(    #77
        0x110,
        "#262F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_2FB1")

    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x10F, 180, 400)
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3029")

    ChrTalk(    #78
        0x10F,
        "#1444F#5PIs something wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3054")

    label("loc_3029")


    ChrTalk(    #79
        0x10F,
        "#1444F#5PIs something wrong, Estelle?\x02",
    )

    CloseMessageWindow()

    label("loc_3054")


    ChrTalk(    #80
        0x101,
        (
            "#1016F#11POh, it's nothing.\x02\x03",

            "#1006FAnyway, we might've got nothing but cryptic\x01",
            "teasers out of him, but we do have a new sealing\x01",
            "stone to unlock.\x02\x03",

            "I think we should head back to the garden and\x01",
            "get to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        (
            "#1448F#5PI agree.\x02\x03",

            "#1446FI'm quite curious as to just what this 'rule book'\x01",
            "is as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3187():
        OP_6D(1850, 5000, 53600, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3187)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10F, 0x0)
    Sleep(2000)
    OP_A2(0x2505)
    OP_A2(0x2508)
    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_16A4 end

    def Function_15_31BD(): pass

    label("Function_15_31BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3295")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E7")
    Sleep(100)
    Jump("loc_3262")

    label("loc_31E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31FC")
    Sleep(200)
    Jump("loc_3262")

    label("loc_31FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3211")
    Sleep(300)
    Jump("loc_3262")

    label("loc_3211")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3226")
    Sleep(400)
    Jump("loc_3262")

    label("loc_3226")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323B")
    Sleep(500)
    Jump("loc_3262")

    label("loc_323B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3250")
    Sleep(600)
    Jump("loc_3262")

    label("loc_3250")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3262")
    Sleep(700)

    label("loc_3262")

    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_15_31BD")

    label("loc_3295")

    Return()

    # Function_15_31BD end

    def Function_16_3296(): pass

    label("Function_16_3296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 1)), scpexpr(EXPR_END)), "loc_329E")
    Return()

    label("loc_329E")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-250, -400, 97250, 0)
    OP_67(0, 12670, -10000, 0)
    OP_6B(5670, 0)
    OP_6C(0, 0)
    OP_6E(318, 0)
    SetChrPos(0x109, -870, 0, 80100, 0)
    SetChrPos(0xEF, 360, 0, 79320, 0)
    SetChrPos(0xF0, -1120, 0, 77610, 0)
    SetChrPos(0xF1, 560, 0, 77100, 0)
    OP_0D()

    def lambda_332D():
        OP_6D(640, -400, 90990, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_332D)

    def lambda_3345():
        OP_67(0, 6040, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3345)

    def lambda_335D():
        OP_6B(3730, 7000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_335D)

    def lambda_336D():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_336D)

    def lambda_337D():
        OP_6E(218, 7000)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_337D)
    Sleep(1000)

    def lambda_3392():
        OP_8E(0xFE, 0xFFFFFC2C, 0xFFFFFE70, 0x16058, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3392)

    def lambda_33AD():
        OP_8E(0xFE, 0x258, 0xFFFFFE70, 0x16094, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_33AD)

    def lambda_33C8():
        OP_8E(0xFE, 0xFFFFF9F2, 0x0, 0x157C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_33C8)

    def lambda_33E3():
        OP_8E(0xFE, 0x28, 0x0, 0x157D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_33E3)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #82
        0x109,
        (
            "#1079F#6PThis is the warp to the sixth plane, right?\x02\x03",

            "#1060FTime to hop to it, then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3559")
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #83
        0x10F,
        "#1445F#11PUmm... Kevin?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #84
        0x109,
        (
            "#1075F#6PHaha. There's no need for the sad face, Ries.\x02\x03",

            "#1840FWe can't afford to stand around talking here.\x01",
            "We need to get moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10F,
        "#1802F#11P...Okay, then.\x02",
    )

    CloseMessageWindow()

    label("loc_3559")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3965")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F6")
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #86
        0x101,
        "#1002F#11PAre you sure you're definitely okay, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_378F")

    label("loc_35F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3647")
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #87
        0x102,
        "#1502F#11PAre you sure you're okay now, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_378F")

    label("loc_3647")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369B")
    OP_8C(0x10B, 270, 400)
    Sleep(300)

    ChrTalk(    #88
        0x10B,
        "#212F#11PUmm... You sure you're okay, by the way?\x02",
    )

    CloseMessageWindow()
    Jump("loc_378F")

    label("loc_369B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36EE")
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #89
        0x107,
        "#065F#11PUmm... Are you sure you're okay, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_378F")

    label("loc_36EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3741")
    OP_8C(0x10A, 270, 400)
    Sleep(300)

    ChrTalk(    #90
        0x10A,
        "#812F#11PUmm... Are you sure you're okay, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_378F")

    label("loc_3741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378F")
    OP_8C(0x110, 270, 400)
    Sleep(300)

    ChrTalk(    #91
        0x110,
        "#267F#11PBy the way...how are you feeling now?\x02",
    )

    CloseMessageWindow()

    label("loc_378F")

    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #92
        0x109,
        (
            "#1075F#6PHaha. I'm fine, honestly. Never better!\x02\x03",

            "#1840FAnyway, we can't afford to stand around\x01",
            "talking here. We need to get moving.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385D")

    ChrTalk(    #93
        0x101,
        "#1006F#11PI suppose you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3962")

    label("loc_385D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3896")

    ChrTalk(    #94
        0x102,
        "#1505F#11PYou're right, I suppose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3962")

    label("loc_3896")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38CD")

    ChrTalk(    #95
        0x10B,
        "#210F#11PI suppose you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3962")

    label("loc_38CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38FA")

    ChrTalk(    #96
        0x107,
        "#560F#11PO-Okay, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3962")

    label("loc_38FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3931")

    ChrTalk(    #97
        0x10A,
        "#816F#11PI suppose you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3962")

    label("loc_3931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3962")

    ChrTalk(    #98
        0x110,
        "#268F#11PWell, if you say so.\x02",
    )

    CloseMessageWindow()

    label("loc_3962")

    Jump("loc_3EBA")

    label("loc_3965")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EBA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1E")
    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #99
        0x105,
        (
            "#1163F#2PBy the way, Kevin...are you sure you're all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6E")
    OP_8C(0x103, 270, 400)
    Sleep(300)

    ChrTalk(    #100
        0x103,
        "#1522F#2PAre you sure you're okay now, Kevin?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB9")
    OP_8C(0x106, 270, 400)
    Sleep(300)

    ChrTalk(    #101
        0x106,
        "#555F#11PYou sure you're all right, man?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B17")
    OP_8C(0x108, 270, 400)
    Sleep(300)

    ChrTalk(    #102
        0x108,
        (
            "#072F#11PBy the way...are you sure you're all right,\x01",
            "Kevin?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3B17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B85")
    OP_8C(0x10E, 270, 400)
    Sleep(300)

    ChrTalk(    #103
        0x10E,
        (
            "#178F#11PBefore we advance, Father Graham...\x01",
            "Are you sure you're all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3B85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE4")
    OP_8C(0x104, 270, 400)
    Sleep(300)

    ChrTalk(    #104
        0x104,
        (
            "#1542F#11PBy the way...are you sure you're all right,\x01",
            "Kevin?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3BE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C31")
    OP_8C(0x10D, 270, 400)
    Sleep(300)

    ChrTalk(    #105
        0x10D,
        "#276F#11P...Are you sure you're all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C81")
    OP_8C(0x10C, 270, 400)
    Sleep(300)

    ChrTalk(    #106
        0x10C,
        "#112F#11PIncidentally...how are you feeling now?\x02",
    )

    CloseMessageWindow()

    label("loc_3C81")

    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #107
        0x109,
        (
            "#1075F#6PHaha. I'm fine, honestly. Never better!\x02\x03",

            "#1840FAnyway, we can't afford to stand around\x01",
            "talking here. We need to get moving.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4B")

    ChrTalk(    #108
        0x105,
        "#1382F#11P...All right, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D81")

    ChrTalk(    #109
        0x103,
        "#1534F#11PWell, if you're sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3D81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DBB")

    ChrTalk(    #110
        0x106,
        "#051F#11PHeh. Well, if you're sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3DBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF2")

    ChrTalk(    #111
        0x108,
        "#573F#11PTrue enough, I suppose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(    #112
        0x10E,
        "#179F#11PVery well, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E58")

    ChrTalk(    #113
        0x104,
        "#1541F#11PHeh. Very well, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E87")

    ChrTalk(    #114
        0x10D,
        "#277F#11P...As you wish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3E87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EBA")

    ChrTalk(    #115
        0x10C,
        "#119F#11PI suppose that's true.\x02",
    )

    CloseMessageWindow()

    label("loc_3EBA")

    OP_A2(0x2B01)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_16_3296 end

    def Function_17_3EC5(): pass

    label("Function_17_3EC5")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-80, -400, 94230, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(4390, 0)
    OP_6C(45000, 0)
    OP_6E(206, 0)
    SetChrPos(0x109, 0, -400, 95030, 0)
    SetChrPos(0xEF, 930, -400, 94030, 0)
    SetChrPos(0xF0, -1220, -400, 94080, 0)
    SetChrPos(0xF1, -170, -400, 93210, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()

    def lambda_3F7C():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3F7C)
    OP_0D()
    Sleep(1500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, -400, 94100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3FE4():
        OP_67(0, 8500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3FE4)

    def lambda_3FFC():
        OP_6E(420, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3FFC)
    Call(0, 21)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_20(0x7D0)
    Sleep(2000)
    NewScene("ED6_DT21/M4113   ._SN", 102, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_17_3EC5 end

    def Function_18_4037(): pass

    label("Function_18_4037")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3, 0, -400, 95030, 180)
    SetChrPos(0x2, 930, -400, 94030, 180)
    SetChrPos(0x1, -1220, -400, 94080, 180)
    SetChrPos(0x0, -170, -400, 93210, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, -400, 94100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_4037 end

    def Function_19_4115(): pass

    label("Function_19_4115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4126")
    Call(0, 17)
    Return()

    label("loc_4126")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, 0, -400, 95030, 0)
    SetChrPos(0x1, 930, -400, 94030, 0)
    SetChrPos(0x2, -1220, -400, 94080, 0)
    SetChrPos(0x3, -170, -400, 93210, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, -400, 94100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M4113   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_4115 end

    def Function_20_41E2(): pass

    label("Function_20_41E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_420B")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_41FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_41FF)

    label("loc_420B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4234")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4228():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4228)

    label("loc_4234")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_425D")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4251():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4251)

    label("loc_425D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4286")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_427A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_427A)

    label("loc_4286")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42B2")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_42B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42C9")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_42C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42E0")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_42E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42F7")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_42F7")

    Return()

    # Function_20_41E2 end

    def Function_21_42F8(): pass

    label("Function_21_42F8")


    def lambda_42FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_42FE)

    def lambda_4310():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4310)

    def lambda_4322():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4322)

    def lambda_4334():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4334)
    Sleep(1000)
    Return()

    # Function_21_42F8 end

    SaveToFile()

Try(main)
