from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5401   ._SN',
        MapName             = 'Other',
        Location            = 'C5401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T7000   ._SN',
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
        'Weissmann',                            # 9
        'Campanella',                           # 10
        "Weissmann's Staff",                    # 11
        'Target Camera',                        # 12
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
        'ED6_DT27/CH03550 ._CH',             # 00
        'ED6_DT27/CH03600 ._CH',             # 01
        'ED6_DT26/CH20765 ._CH',             # 02
        'ED6_DT26/CH20485 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03550P._CP',             # 00
        'ED6_DT27/CH03600P._CP',             # 01
        'ED6_DT26/CH20765P._CP',             # 02
        'ED6_DT26/CH20485P._CP',             # 03
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_1D5",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_655",          # 03, 3
        "Function_4_6AC",          # 04, 4
        "Function_5_B91",          # 05, 5
        "Function_6_F7C",          # 06, 6
        "Function_7_FD5",          # 07, 7
        "Function_8_1AB9",         # 08, 8
        "Function_9_1BB4",         # 09, 9
        "Function_10_1CAF",        # 0A, 10
        "Function_11_1D27",        # 0B, 11
        "Function_12_1DCB",        # 0C, 12
        "Function_13_1EBD",        # 0D, 13
        "Function_14_1F67",        # 0E, 14
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_166"),
        (102, "loc_16D"),
        (SWITCH_DEFAULT, "loc_174"),
    )


    label("loc_166")

    Event(0, 8)
    Jump("loc_174")

    label("loc_16D")

    Event(0, 9)
    Jump("loc_174")

    label("loc_174")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_18D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1B8")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_1D4")

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1D4")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_1D4")

    Return()

    # Function_0_14A end

    def Function_1_1D5(): pass

    label("Function_1_1D5")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F1")
    OP_1B(0x1, 0x0, 0xA)
    OP_1B(0x2, 0x0, 0xB)
    Jump("loc_203")

    label("loc_1F1")

    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)

    label("loc_203")

    Return()

    # Function_1_1D5 end

    def Function_2_204(): pass

    label("Function_2_204")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_22(0x85, 0x28, 0x64)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1140, 1500, 85570, 0)
    OP_6D(-300, 0, 53260, 0)
    OP_67(0, 9770, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(410, 0)

    def lambda_282():
        OP_6D(-510, 1500, 87040, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_282)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(20, 1500, 86880, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x11,
        (
            "#850F#5PHeehee. What a lovely sound.\x02\x03",

            "The sound of everything crumbling to the ground...\x02\x03",

            "Still, at least now the professor has the rubble\x01",
            "of an ancient city to serve as his pillow in his\x01",
            "eternal slumber.\x02\x03",

            "I'm sure he must be very happy about that.\x02\x03",

            "Haha. Don't you worry, Professor. You just leave\x01",
            "everything to me now...\x02\x03",

            "And with that...\x02\x03",

            "...you won't ever need to crawl your way out of \x01",
            "Gehenna and return to this world ever again.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x2)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(300)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0x11, 2)
    Sleep(300)
    OP_43(0x12, 0x0, 0x0, 0x3)
    WaitChrThread(0x12, 0x0)
    Fade(250)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x2)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00◆Campanella clicks his fingers\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #2
        0x11,
        (
            "#850F#5PEnforcer No. 0, Campanella the Fool...\x02\x03",

            "Entering the Celestial Globe in place of the\x01",
            "Third Anguis, Georg Weissmann!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x3, 0x0, 0x0, 0x6)
    OP_20(0x7D0)
    Fade(2000)
    OP_6D(20, 1500, 156880, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, -1140, 1500, 155570, 0)
    SetChrPos(0x12, -1140, 1500, 156570, 0)
    OP_0D()
    OP_A2(0x2506)
    OP_4F(0x43, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C5416   ._SN", 100, 1, 0)
    IdleLoop()
    Return()

    # Function_2_204 end

    def Function_3_655(): pass

    label("Function_3_655")

    SetChrFlags(0xFE, 0x800)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 5)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1140, 1500, 86570, 0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)

    def lambda_695():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_695)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_655 end

    def Function_4_6AC(): pass

    label("Function_4_6AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_6D(0, 0, 60700, 0)
    OP_67(0, 8920, -10000, 0)
    OP_6B(4560, 0)
    OP_6C(55000, 0)
    OP_6E(328, 0)
    LoadEffect(0x0, "map\\\\mp294_00.eff")
    LoadEffect(0x1, "map\\\\mp294_01.eff")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1000, 0, 65360, 0)

    def lambda_757():
        OP_6D(1000, 0, 84400, 7000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_757)

    def lambda_76F():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_76F)

    def lambda_77F():
        OP_8E(0xFE, 0xFFFFFC18, 0x5DC, 0x14F00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_77F)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x13, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-60, 1500, 86800, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x11, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x11,
        (
            "#850FEven all the noise going on outside can't reach\x01",
            "this far inside the ship by the looks of it.\x02\x03",

            "#853FJust as well. I couldn't fulfill my role otherwise.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(200)
    SetChrSubChip(0x11, 2)
    Sleep(400)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0x11, 3)
    Sleep(50)
    OP_20(0x0)
    Sleep(450)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8E6():
        OP_6D(-1000, 2300, 88200, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_8E6)

    def lambda_8FE():
        OP_67(0, 4440, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8FE)

    def lambda_916():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_916)

    def lambda_926():
        OP_6E(605, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_926)
    WaitChrThread(0x13, 0x0)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(200)
    OP_22(0x9D, 0x0, 0x64)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x405, 0x0)
    ExitThread()
    OP_0D()
    Sleep(400)
    Fade(200)
    OP_22(0x9D, 0x0, 0x64)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x11,
        (
            "#853F#6PRequesting access.\x02\x03",

            "#854FI, Enforcer No. 0, Campanella the Fool...\x02\x03",

            "...hereby request access to the Celestial Globe\x01",
            "in place of the Third Anguis, Georg Weissmann.\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0xE0)
    Sleep(500)
    OP_59()
    Fade(1000)
    PlayEffect(0x0, 0x1, 0xFF, -6820, 5000, 75500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 4820, 5000, 75500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -13120, 5000, 85000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 11120, 5000, 85000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x5, 0xFF, -1000, 8500, 91000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_C0(0x14, 0xFA0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5416   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_6AC end

    def Function_5_B91(): pass

    label("Function_5_B91")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_6D(-60, 1500, 86800, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(3550, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1000, 1500, 85760, 0)
    OP_AE(0x5DC)

    def lambda_C1E():
        OP_6B(3350, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C1E)
    FadeToBright(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x11,
        (
            "#853F#6PSo it's time for the Phantasmal Blaze Plan to\x01",
            "begin, huh?\x02\x03",

            "The stage is set, at the very least. It's going\x01",
            "to utterly dwarf the Gospel Plan in terms of\x01",
            "both quality and scale...\x02\x03",

            "#854FHeehee... Things are finally about to get\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #6
        0x11,
        (
            "#855F#6P...By the way.\x02\x03",

            "I might be the last person you want to hear\x01",
            "this from, but...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_DC6():
        OP_6D(-360, 1500, 86500, 1200)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_DC6)

    def lambda_DDE():
        OP_67(0, 7000, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DDE)

    def lambda_DF6():
        OP_6B(3550, 1200)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DF6)
    OP_8C(0x11, 225, 300)
    WaitChrThread(0x13, 0x0)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #7
        0x11,
        (
            "#854F#5P...would you mind stopping the whole peeping\x01",
            "in thing, mysterious stranger?\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_F7(0x9, 0xE, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00Side Story [Phantasmal Blaze] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    ClearMapFlags(0x2000000)
    ClearMapFlags(0x100000)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6F")
    Sleep(500)
    OP_28(0x12, 0x4, 0x10)
    OP_28(0x12, 0x4, 0x20)
    OP_3E(0x18F, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Received \x1F\x8F\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(30000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "\x07\x05Received \x07\x0230,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_F6F")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B91 end

    def Function_6_F7C(): pass

    label("Function_6_F7C")

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
    OP_24(0x85, 0x14)
    Sleep(100)
    OP_24(0x85, 0xA)
    Sleep(100)
    OP_24(0x85, 0x0)
    OP_23(0x85)
    Return()

    # Function_6_F7C end

    def Function_7_FD5(): pass

    label("Function_7_FD5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x124, -1000, 0, 43070, 0)
    SetChrPos(0x10, -1170, 1500, 85080, 0)
    SetChrPos(0x11, 70, 1500, 84280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(-1000, 0, 50840, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(429, 0)

    def lambda_1061():
        OP_6D(-1000, 1500, 87960, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1061)

    def lambda_1079():
        OP_67(0, 6100, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1079)

    def lambda_1091():
        OP_6B(3820, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1091)

    def lambda_10A1():
        OP_6E(500, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_10A1)

    def lambda_10B1():
        OP_8F(0xFE, 0xFFFFFC18, 0x0, 0x130C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_10B1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Sleep(1000)

    def lambda_10E0():
        OP_6D(-1000, 1500, 83010, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_10E0)

    def lambda_10F8():
        OP_67(0, 3250, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_10F8)

    def lambda_1110():
        OP_6B(2380, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1110)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x124, 0x0)
    Fade(500)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(830, 420, 83300, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(386, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x10, 180, 400)
    Sleep(100)
    OP_8C(0x11, 180, 400)
    Sleep(500)

    ChrTalk(    #11
        0x11,
        "#850F#2PHey, Loewe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "#1150FDid you get plenty of rest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x124,
        (
            "#120FYeah...\x02\x03",

            "So, what's the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#1150FHeheh... Things are going even better than\x01",
            "we expected.\x02\x03",

            "The kingdom is in a complete state of panic\x01",
            "because of the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#850F#2PTo make matters worse for them, we sent down\x01",
            "quite a lot of archaisms, too.\x02\x03",

            "All in all, the Royal Army won't be able to act in\x01",
            "an organized fashion to deal with things any time\x01",
            "soon.\x02\x03",

            "That goes for that irritating Cassius Bright, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x124,
        (
            "#120FSo all in all, everything is going well.\x02\x03",

            "...What about Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1150FThe ship he was on has landed in Valleria Lake.\x02\x03",

            "I don't doubt he'll begin to act again at some\x01",
            "point, but for now, I don't think there's any\x01",
            "need to factor him into our calculations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#850F#2PHaha. By the time he's ready to act again, it'll\x01",
            "be too late for him to do anything, anyway.\x02\x03",

            "After all, now even the famous Blood and Iron\x01",
            "Chancellor seems to have taken an interest in\x01",
            "what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x124,
        (
            "#120FHeh. You say that as if you had nothing to\x01",
            "do with it.\x02\x03",

            "It's only because of you that he even knows\x01",
            "about the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#850F#2PAhaha. Well, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#1150FStill, the more actors on the stage, the livelier\x01",
            "it is.\x02\x03",

            "...Incidentally, Loewe...\x02\x03",

            "We do have one small problem that needs to\x01",
            "be dealt with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x124,
        "#120FDo we, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#850F#2PIt's the floating city's defensive system,\x01",
            "you see.\x02\x03",

            "Amazingly enough, it's still operational.\x02\x03",

            "We're going to need to disable it before we\x01",
            "can land, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1150FA giant ship like the Glorious is just going to\x01",
            "be a huge, slow target for all of its firepower\x01",
            "if we try getting any closer.\x02\x03",

            "Still, if you use the Reverie Dragion that was\x01",
            "developed for you, you should be able to get\x01",
            "close to it and attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x124,
        (
            "#120FI see...\x02\x03",

            "So that's why you called me, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "#850F#2PDo you think you can handle it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x124,
        (
            "#120FI have the sword granted to me by the Grandmaster,\x01",
            "that can cut anything in this world...\x02\x03",

            "Of course I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#850F#2PHaha. So you do.\x02\x03",

            "That was made with the Divergent Laws, too,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1150FThe Dragion is standing by for you on the deck.\x02\x03",

            "Go forth, and use it to open the door that leads\x01",
            "to a legend!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x124, 180, 400)
    Fade(500)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_79(0x9, 0x1)
    OP_7B()
    OP_6D(-970, -1500, 81290, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)

    def lambda_1A65():
        OP_8F(0xFE, 0xFFFFFC54, 0x0, 0xF83E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_1A65)
    OP_0D()
    Sleep(500)

    def lambda_1A86():
        OP_6D(-1000, 11000, 85270, 7000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A86)
    WaitChrThread(0x10, 0x0)
    OP_44(0x124, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5408   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_FD5 end

    def Function_8_1AB9(): pass

    label("Function_8_1AB9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-980, 0, 56040, 0)
    SetChrPos(0x3, -920, 0, 55420, 0)
    SetChrPos(0x2, -1670, 0, 56080, 0)
    SetChrPos(0x1, -310, 0, 56080, 0)
    SetChrPos(0x0, -980, 0, 56670, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 12)
    Call(0, 13)
    Fade(500)
    OP_6D(-960, 0, 58290, 0)
    SetChrPos(0x0, -960, 0, 58290, 0)
    SetChrPos(0x1, -960, 0, 58290, 0)
    SetChrPos(0x2, -960, 0, 58290, 0)
    SetChrPos(0x3, -960, 0, 58290, 0)
    EventEnd(0x0)
    Return()

    # Function_8_1AB9 end

    def Function_9_1BB4(): pass

    label("Function_9_1BB4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-960, 0, 78190, 0)
    SetChrPos(0x3, -960, 0, 78810, 180)
    SetChrPos(0x2, -350, 0, 78190, 180)
    SetChrPos(0x1, -1580, 0, 78190, 180)
    SetChrPos(0x0, -960, 0, 77580, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 12)
    Call(0, 13)
    Fade(500)
    OP_6D(-960, 0, 75810, 0)
    SetChrPos(0x0, -960, 0, 75810, 180)
    SetChrPos(0x1, -960, 0, 75810, 180)
    SetChrPos(0x2, -960, 0, 75810, 180)
    SetChrPos(0x3, -960, 0, 75810, 180)
    EventEnd(0x0)
    Return()

    # Function_9_1BB4 end

    def Function_10_1CAF(): pass

    label("Function_10_1CAF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-980, 0, 56040, 0)
    SetChrPos(0x0, -920, 0, 55420, 180)
    SetChrPos(0x1, -1670, 0, 56080, 180)
    SetChrPos(0x2, -310, 0, 56080, 180)
    SetChrPos(0x3, -980, 0, 56670, 180)
    OP_0D()
    Call(0, 12)
    Call(0, 14)
    NewScene("ED6_DT21/C5313   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1CAF end

    def Function_11_1D27(): pass

    label("Function_11_1D27")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-1000, 0, 79150, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(0, 0)
    OP_6E(402, 0)
    SetChrPos(0x3, -960, 0, 78810, 180)
    SetChrPos(0x2, -350, 0, 78190, 180)
    SetChrPos(0x1, -1580, 0, 78190, 180)
    SetChrPos(0x0, -960, 0, 77580, 180)
    OP_0D()
    Call(0, 12)
    Call(0, 14)
    NewScene("ED6_DT21/C4103   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1D27 end

    def Function_12_1DCB(): pass

    label("Function_12_1DCB")

    LoadEffect(0x0, "map\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_12_1DCB end

    def Function_13_1EBD(): pass

    label("Function_13_1EBD")


    def lambda_1EC3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1EC3)

    def lambda_1ED5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1ED5)

    def lambda_1EE7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1EE7)

    def lambda_1EF9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1EF9)
    Sleep(2500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F21")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1F21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F38")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1F38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1F4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F66")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1F66")

    Return()

    # Function_13_1EBD end

    def Function_14_1F67(): pass

    label("Function_14_1F67")


    def lambda_1F6D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F6D)

    def lambda_1F7F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1F7F)

    def lambda_1F91():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1F91)

    def lambda_1FA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1FA3)
    Sleep(2000)
    Return()

    # Function_14_1F67 end

    SaveToFile()

Try(main)
