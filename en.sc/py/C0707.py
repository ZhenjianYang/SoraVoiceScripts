from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0707   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0707.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'Bleublanc',                            # 9
        'Gospel',                               # 10
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
        'ED6_DT27/CH03530 ._CH',             # 00
        'ED6_DT27/CH04530 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT27/CH04001 ._CH',             # 03
        'ED6_DT27/CH04010 ._CH',             # 04
        'ED6_DT27/CH04011 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT27/CH04530P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT27/CH04001P._CP',             # 03
        'ED6_DT27/CH04010P._CP',             # 04
        'ED6_DT27/CH04011P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
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
        Unknown3            = 458758,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_13F",          # 01, 1
        "Function_2_140",          # 02, 2
        "Function_3_1266",         # 03, 3
        "Function_4_127B",         # 04, 4
        "Function_5_1290",         # 05, 5
        "Function_6_12D8",         # 06, 6
        "Function_7_135E",         # 07, 7
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_13E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_13E")

    Return()

    # Function_0_122 end

    def Function_1_13F(): pass

    label("Function_1_13F")

    Return()

    # Function_1_13F end

    def Function_2_140(): pass

    label("Function_2_140")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157")
    Call(0, 6)
    Call(0, 7)

    label("loc_157")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_178"),
        (5, "loc_185"),
        (4, "loc_192"),
        (6, "loc_19F"),
        (7, "loc_1AC"),
        (8, "loc_1B9"),
        (SWITCH_DEFAULT, "loc_1C6"),
    )


    label("loc_178")

    OP_D2(0x701D0, 0x701DC, 0x7)
    Jump("loc_1C6")

    label("loc_185")

    OP_D2(0x70218, 0x70224, 0x7)
    Jump("loc_1C6")

    label("loc_192")

    OP_D2(0x70200, 0x7020C, 0x7)
    Jump("loc_1C6")

    label("loc_19F")

    OP_D2(0x70230, 0x7023C, 0x7)
    Jump("loc_1C6")

    label("loc_1AC")

    OP_D2(0x70248, 0x70254, 0x7)
    Jump("loc_1C6")

    label("loc_1B9")

    OP_D2(0x270176, 0x270183, 0x7)
    Jump("loc_1C6")

    label("loc_1C6")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1E7"),
        (5, "loc_1F4"),
        (4, "loc_201"),
        (6, "loc_20E"),
        (7, "loc_21B"),
        (8, "loc_228"),
        (SWITCH_DEFAULT, "loc_235"),
    )


    label("loc_1E7")

    OP_D2(0x701D0, 0x701DC, 0x9)
    Jump("loc_235")

    label("loc_1F4")

    OP_D2(0x70218, 0x70224, 0x9)
    Jump("loc_235")

    label("loc_201")

    OP_D2(0x70200, 0x7020C, 0x9)
    Jump("loc_235")

    label("loc_20E")

    OP_D2(0x70230, 0x7023C, 0x9)
    Jump("loc_235")

    label("loc_21B")

    OP_D2(0x70248, 0x70254, 0x9)
    Jump("loc_235")

    label("loc_228")

    OP_D2(0x270176, 0x270183, 0x9)
    Jump("loc_235")

    label("loc_235")

    OP_D2(0x27026E, 0x270278, 0xB)
    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, 700, 950, 12150, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 4)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 7)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    SetChrPos(0x101, -700, 0, 4650, 90)
    SetChrPos(0x102, 700, 0, 4520, 90)
    SetChrPos(0xF8, -800, 0, 2930, 90)
    SetChrPos(0xF9, 800, 0, 2800, 90)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_72(0x6, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    FadeToBright(1000, 0)

    def lambda_369():
        OP_6D(1840, 0, 7670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_369)

    def lambda_381():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_381)

    def lambda_399():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_399)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1025F#5PHey!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF")

    ChrTalk(    #1
        0x109,
        "#1062F#5PHeeey! It's all back to normal!\x02",
    )

    CloseMessageWindow()
    Jump("loc_504")

    label("loc_3FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44E")

    ChrTalk(    #2
        0x105,
        (
            "#542F#5PEverything's returned to normal!\x01",
            "Thank goodness!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504")

    label("loc_44E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_496")

    ChrTalk(    #3
        0x103,
        (
            "#027F#5PThat did it, everything's\x01",
            "back to normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504")

    label("loc_496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D1")

    ChrTalk(    #4
        0x108,
        "#070F#5PAnd it's all back to normal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_504")

    label("loc_4D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_504")

    ChrTalk(    #5
        0x106,
        "#051F#5PHell yeah, that did it!\x02",
    )

    CloseMessageWindow()

    label("loc_504")


    ChrTalk(    #6
        0x8,
        (
            "#230F#6PIt seems my role has come\x01",
            "to an end for now.\x02\x03",

            "Nothing for it, then.\x01",
            "I suppose I shall withdraw.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    def lambda_57E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57E)
    Sleep(50)

    def lambda_591():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_591)
    Sleep(50)

    def lambda_5A4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5A4)
    Sleep(50)

    ChrTalk(    #7
        0x101,
        "#1004F#2PWh--\x02",
    )

    CloseMessageWindow()

    def lambda_5CA():
        OP_6D(1500, 0, 9790, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CA)

    def lambda_5E2():
        OP_67(0, 5000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E2)

    def lambda_5FA():
        OP_6B(4220, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5FA)
    OP_8C(0x8, 180, 400)
    Sleep(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 11)
    OP_99(0x8, 0x0, 0x5, 0x7D0)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_704")

    label("loc_6C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ED")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_704")

    label("loc_6ED")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_704")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76E")

    label("loc_730")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_76E")

    label("loc_757")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_76E")

    Sleep(1000)

    ChrTalk(    #8
        0x101,
        "#1005F#2PHOLD ON, YOU!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(    #9
        0x105,
        "#043F#2PWait, please!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80D")

    ChrTalk(    #10
        0x106,
        (
            "#054F#2POh, hell no, clown, you\x01",
            "don't get to run this time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_80D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_854")

    ChrTalk(    #11
        0x109,
        (
            "#1069F#2PWhat, you running?!\x01",
            "We're not done yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88D")

    ChrTalk(    #12
        0x103,
        "#024F#2PTrying to run, Bleublanc?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BB")

    label("loc_88D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BB")

    ChrTalk(    #13
        0x108,
        "#076F#2PRunning, are you?!\x02",
    )

    CloseMessageWindow()

    label("loc_8BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99F")

    ChrTalk(    #14
        0x8,
        (
            "#231F#6PHaha! Ah! I expected it of the\x01",
            "princess, but you bracers also\x01",
            "shine with a certain nobility.\x02\x03",

            "When next we meet, I shall take\x01",
            "the full measure of your radiance.\x02\x03",

            "#230FWell, then, everyone... Adieu!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_99F")


    ChrTalk(    #15
        0x8,
        (
            "#231F#6PHaha! I expected it of the Black Fang,\x01",
            "but you bracers are also quite skilled.\x02\x03",

            "I shall determine the true measure\x01",
            "of your worth when next we meet.\x02\x03",

            "#230FWell, then, everyone... Adieu!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A65")

    OP_99(0x8, 0x5, 0xE, 0x7D0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    SetChrFlags(0x8, 0x80)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x5)
    Sleep(3500)

    ChrTalk(    #16
        0x101,
        "#1019F#5PDarn it, he got away after all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1042F#2P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()

    def lambda_AF4():
        OP_8E(0xFE, 0xDC, 0x3B6, 0x2F58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF4)

    def lambda_B0F():
        OP_6D(0, 950, 13850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B0F)

    def lambda_B27():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B27)

    def lambda_B3F():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B3F)

    def lambda_B4F():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_B4F)

    def lambda_B5F():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B5F)
    Sleep(200)

    def lambda_B74():
        OP_8E(0xFE, 0xFFFFFBA0, 0x3B6, 0x2EF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B74)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x4)
    Sleep(200)
    OP_43(0xF8, 0x1, 0x0, 0x3)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x102,
        (
            "#1043F#4PSo this is the beta, then.\x01",
            "The final Gospel made by the society.\x02\x03",

            "It's even larger than the other new models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002F#5PI'm glad the tower's back\x01",
            "to normal, and all...\x02\x03",

            "...but what was he trying\x01",
            "to do with this thing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #20
        0x108,
        (
            "#072F#2PThe machinery that was operating\x01",
            "until now has stopped.\x02\x03",

            "#572FIt's...unsettling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F38")

    label("loc_D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D93")

    ChrTalk(    #21
        0x106,
        (
            "#552F#2PGood question. The machinery up\x01",
            "here's stopped working again.\x02\x03",

            "#053FTch. Gotta say, it gives me\x01",
            "a bad feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F38")

    label("loc_D93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E28")

    ChrTalk(    #22
        0x109,
        (
            "#1063F#2PAll the mechanical junk up here's\x01",
            "stopped working again, looks like.\x02\x03",

            "#1068FThaaaat's definitely not ominous, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F38")

    label("loc_E28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC4")

    ChrTalk(    #23
        0x103,
        (
            "#022F#2PI wonder. The machinery up here was\x01",
            "functioning again, until a moment ago.\x02\x03",

            "#522FThat doesn't feel ominous\x01",
            "at all, does it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F38")

    label("loc_EC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F38")

    ChrTalk(    #24
        0x107,
        (
            "#561F#2PThe machinery up here was working\x01",
            "again until a second ago.\x02\x03",

            "#063FIt kinda worries me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBB")

    ChrTalk(    #25
        0x105,
        (
            "#043F#2PAnd that barrier that was covering the\x01",
            "tower's crown until a moment ago...\x02\x03",

            "What WAS that, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(    #26
        0x107,
        (
            "#065F#2POh, and, and!\x02\x03",

            "The weird black energy is gone,\x01",
            "too! I wonder what it was?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_1023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1094")

    ChrTalk(    #27
        0x103,
        (
            "#522FAnd the barrier that was covering\x01",
            "the roof has disappeared.\x02\x03",

            "What was it, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_1094")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1105")

    ChrTalk(    #28
        0x109,
        (
            "#1067FThat...black whatever that was\x01",
            "coverin' the roof is gone now, too.\x02\x03",

            "The heck was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_1105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(    #29
        0x106,
        (
            "#555FAnd that whatever-it-was up\x01",
            "here on the roof is gone, too.\x02\x03",

            "The hell was that, anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1174")


    ChrTalk(    #30
        0x102,
        "#1043F#4P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #31
        0x102,
        (
            "#1040F#4PRegardless, the tower has\x01",
            "been returned to normal.\x02\x03",

            "We should return to\x01",
            "the Arseille for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #32
        0x101,
        (
            "#1025F#5PYeah, we should discuss this\x01",
            "with Professor Russell.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_140 end

    def Function_3_1266(): pass

    label("Function_3_1266")

    OP_8E(0xFE, 0xFFFFFBB4, 0xFA, 0x2B48, 0xBB8, 0x0)
    Return()

    # Function_3_1266 end

    def Function_4_127B(): pass

    label("Function_4_127B")

    OP_8E(0xFE, 0x17C, 0x1F4, 0x2B8E, 0xBB8, 0x0)
    Return()

    # Function_4_127B end

    def Function_5_1290(): pass

    label("Function_5_1290")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_5_1290 end

    def Function_6_12D8(): pass

    label("Function_6_12D8")

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
        (0, "loc_1351"),
        (1, "loc_1357"),
        (SWITCH_DEFAULT, "loc_135D"),
    )


    label("loc_1351")

    OP_A2(0x1200)
    Jump("loc_135D")

    label("loc_1357")

    OP_A2(0x1201)
    Jump("loc_135D")

    label("loc_135D")

    Return()

    # Function_6_12D8 end

    def Function_7_135E(): pass

    label("Function_7_135E")

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

    # Function_7_135E end

    SaveToFile()

Try(main)
