from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5702   ._SN',
        MapName             = 'Other',
        Location            = 'C5702.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        'Enhanced Jaeger',                      # 9
        'Enhanced Jaeger',                      # 10
        'Enhanced Jaeger',                      # 11
        'Don',                                  # 12
        'Kyle',                                 # 13
        'Sky Bandit',                           # 14
        'Sky Bandit',                           # 15
        'Sky Bandit',                           # 16
        'Sky Bandit',                           # 17
        'Sky Bandit',                           # 18
        'Sky Bandit',                           # 19
        'Sky Bandit',                           # 20
        'Sky Bandit',                           # 21
        'Target',                               # 22
        'Industrial Block - Factoria',          # 23
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
        'ED6_DT26/CH20208 ._CH',             # 00
        'ED6_DT07/CH00291 ._CH',             # 01
        'ED6_DT07/CH00301 ._CH',             # 02
        'ED6_DT07/CH00361 ._CH',             # 03
        'ED6_DT26/CH20209 ._CH',             # 04
        'ED6_DT26/CH20501 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT26/CH20208P._CP',             # 00
        'ED6_DT07/CH00291P._CP',             # 01
        'ED6_DT07/CH00301P._CP',             # 02
        'ED6_DT07/CH00361P._CP',             # 03
        'ED6_DT26/CH20209P._CP',             # 04
        'ED6_DT26/CH20501P._CP',             # 05
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 74170,
        Z                   = 4000,
        Y                   = -220080,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 66000,
        Y                   = 10000,
        Z                   = -124270,
        Range               = 82300,
        Unknown_10          = 0x4650,
        Unknown_14          = 0xFFFE1E7A,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 64500,
        Y                   = 10000,
        Z                   = -96700,
        Range               = 83300,
        Unknown_10          = 0x4650,
        Unknown_14          = 0xFFFE83EC,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_2FA",          # 00, 0
        "Function_1_317",          # 01, 1
        "Function_2_461",          # 02, 2
        "Function_3_1DD0",         # 03, 3
        "Function_4_2D1A",         # 04, 4
        "Function_5_2D23",         # 05, 5
        "Function_6_34B4",         # 06, 6
        "Function_7_379E",         # 07, 7
        "Function_8_37B5",         # 08, 8
        "Function_9_37CC",         # 09, 9
        "Function_10_380D",        # 0A, 10
        "Function_11_3829",        # 0B, 11
        "Function_12_3845",        # 0C, 12
        "Function_13_3861",        # 0D, 13
        "Function_14_387D",        # 0E, 14
        "Function_15_38AD",        # 0F, 15
        "Function_16_38DD",        # 10, 16
        "Function_17_390D",        # 11, 17
        "Function_18_393D",        # 12, 18
        "Function_19_3BD0",        # 13, 19
        "Function_20_3C5C",        # 14, 20
        "Function_21_3C7B",        # 15, 21
        "Function_22_3D01",        # 16, 22
        "Function_23_3D94",        # 17, 23
    )


    def Function_0_2FA(): pass

    label("Function_0_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_316")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_316")

    Return()

    # Function_0_2FA end

    def Function_1_317(): pass

    label("Function_1_317")

    OP_16(0x2, 0xFA0, 0xFFFF2D10, 0xFFFC4EB0, 0x230076)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x518), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33E")

    OP_22(0x1C7, 0x0, 0x64)
    OP_22(0x1C3, 0x1, 0x50)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x518), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_460")
    OP_D2(0x26020B, 0x260210, 0x9)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    OP_D2(0x702B4, 0x702BB, 0xE)
    OP_D2(0x702B5, 0x702BC, 0xF)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_3BF"),
        (3, "loc_3D6"),
        (4, "loc_3ED"),
        (5, "loc_404"),
        (6, "loc_41B"),
        (7, "loc_432"),
        (8, "loc_449"),
        (SWITCH_DEFAULT, "loc_460"),
    )


    label("loc_3BF")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_460")

    label("loc_3D6")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_460")

    label("loc_3ED")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_460")

    label("loc_404")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_460")

    label("loc_41B")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_460")

    label("loc_432")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_460")

    label("loc_449")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_460")

    label("loc_460")

    Return()

    # Function_1_317 end

    def Function_2_461(): pass

    label("Function_2_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46D")
    Return()

    label("loc_46D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_492")
    Call(0, 21)
    Call(0, 22)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_492")

    SetChrPos(0x8, 37090, 16000, -74080, 135)
    SetChrPos(0x9, 40420, 16000, -76420, 270)
    SetChrPos(0xA, 37590, 16000, -77170, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)
    OP_43(0x9, 0x0, 0x6, 0x2)
    OP_43(0xA, 0x0, 0x6, 0x2)
    OP_E5(0x8, 0x0, 0x0)
    OP_E5(0x9, 0x0, 0x0)
    OP_E5(0xA, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B")
    OP_62(0x107, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_558")

    label("loc_51B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541")
    OP_62(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_558")

    label("loc_541")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_558")

    Sleep(1000)
    StopSound(0x186A0, 0x9C400, 0x2710)

    def lambda_570():
        OP_6D(62050, 16000, -34780, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_570)

    def lambda_588():
        OP_67(0, 10390, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_588)

    def lambda_5A0():
        OP_6B(14610, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A0)

    def lambda_5B0():
        OP_6C(343000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5B0)

    def lambda_5C0():
        OP_6E(599, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Fade(500)
    OP_11(0xAA, 0xC8, 0xFF, 0x124F8, 0x3A980, 0x0)
    OP_6D(37580, 16000, -75050, 0)
    OP_67(0, 4590, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(341, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_0D()
    Sleep(500)
    OP_E5(0x8, 0x0, 0x1)
    OP_E5(0x9, 0x0, 0x1)
    OP_E5(0xA, 0x0, 0x1)

    ChrTalk(    #0
        0x9,
        (
            "#4PMan, never thought we'd end\x01",
            "up in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "#4PWhat d'you figure they'll make us do now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#6PNo clue...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#6PWith the professor and the Enforcers all\x01",
            "headin' out together, though, doubt there's\x01",
            "much left for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#6PProbably just capturing intruders like\x01",
            "those bandits, you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#6PYeah, that Liberlian ship crashed\x01",
            "down here, too, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "#6PDon't we need to deal with them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#6PWe got orders on that. Professor says to\x01",
            "ignore 'em until he and the others get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#6PNot like they can do much to\x01",
            "us until their ship's fixed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E6")
    SetChrPos(0x101, 65519, 16000, -92680, 315)
    SetChrPos(0x102, 65540, 16000, -94040, 315)
    SetChrPos(0xF8, 67240, 16000, -92700, 315)
    SetChrPos(0xF9, 67200, 16000, -94120, 315)
    Jump("loc_958")

    label("loc_8E6")

    SetChrPos(0x10B, 65519, 16000, -92680, 315)
    SetChrPos(0x101, 65540, 16000, -94040, 315)
    SetChrPos(0x102, 67240, 16000, -92700, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93A")
    SetChrPos(0xF9, 67200, 16000, -94120, 315)
    Jump("loc_958")

    label("loc_93A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_958")
    SetChrPos(0xF8, 67200, 16000, -94120, 315)

    label("loc_958")


    def lambda_95E():
        OP_6D(64690, 16000, -92130, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95E)

    def lambda_976():
        OP_67(0, 7850, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_976)
    OP_6C(294000, 5000)
    Fade(500)
    OP_6D(65129, 16000, -94170, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(243000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A28")
    SetChrPos(0x101, 65519, 16000, -92680, 270)
    SetChrPos(0x102, 65540, 16000, -94040, 0)
    SetChrPos(0xF8, 67240, 16000, -92700, 270)
    SetChrPos(0xF9, 67200, 16000, -94120, 0)
    Jump("loc_A9A")

    label("loc_A28")

    SetChrPos(0x10B, 65519, 16000, -92680, 270)
    SetChrPos(0x101, 65540, 16000, -94040, 0)
    SetChrPos(0x102, 67240, 16000, -92700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7C")
    SetChrPos(0xF9, 67200, 16000, -94120, 270)
    Jump("loc_A9A")

    label("loc_A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A")
    SetChrPos(0xF8, 67200, 16000, -94120, 0)

    label("loc_A9A")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1642")

    ChrTalk(    #9
        0x101,
        "#1020F#6P(So this is where the Glorious docked.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(    #10
        0x107,
        "#065F#5P(Waaaah! What a huge ship...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_B20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #11
        0x105,
        (
            "#1167F#5P(Just as Sieg said, it was on the\x01",
            "eastern side of the city...)\x02\x03",

            "#1162F(Still, it's enormous...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_B9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C05")

    ChrTalk(    #12
        0x109,
        (
            "#1063F#5P(Sweet Aidios, when you get this close,\x01",
            "you see just how BIG it is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")

    ChrTalk(    #13
        0x103,
        (
            "#025F#5P(It's only when you get this close\x01",
            "that you realize how huge it is.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_C68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCD")

    ChrTalk(    #14
        0x104,
        (
            "#032F#5P(Only when you are this close to it\x01",
            "do you realize how massive it is.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3A")

    ChrTalk(    #15
        0x106,
        (
            "#555F#5P(Damn. When you're this close, you realize\x01",
            "just how stupidly huge that thing is.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7C")

    ChrTalk(    #16
        0x108,
        "#072F#1P(I believe this may be our chance.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD4")

    ChrTalk(    #17
        0x106,
        (
            "#057F#5P(You heard the guards, though.\x01",
            "This might be our chance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_DD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E16")

    ChrTalk(    #18
        0x104,
        "#030F#5P(This may, perhaps, be our chance.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E70")

    ChrTalk(    #19
        0x103,
        (
            "#022F#5P(But listen to the guards.\x01",
            "I think we've found our chance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED4")

    ChrTalk(    #20
        0x109,
        (
            "#1063F#5P(Yeah, but...you heard 'em, right?\x01",
            "Think we found our chance, here.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_ED4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2F")

    ChrTalk(    #21
        0x105,
        (
            "#1162F#5P(What the guards said, however...\x01",
            "I think we have an opening.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2F")


    ChrTalk(    #22
        0x102,
        (
            "#1035F#6P(Yes, if all the major society members\x01",
            "are absent...)\x02\x03",

            "#1042F(This is the best shot we have at saving\x01",
            "the Capuas. We should break in.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_FD1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_FD1)
    Sleep(50)

    def lambda_FE4():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_FE4)
    Sleep(250)

    ChrTalk(    #23
        0x101,
        (
            "#1004F#4P(Wait a sec.)\x02\x03",

            "#1015F(I'm all for going in, but shouldn't\x01",
            "we tell Josette?)\x02\x03",

            "(We ARE going to go rescue her brothers.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1044F#6P(Estelle...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #25
        0x101,
        (
            "#1013F#4P(Er, don't misunderstand, okay?)\x02\x03",

            "(It's just, you know, a responsible\x01",
            "bracer thing. To do. Yeah.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1158")

    ChrTalk(    #26
        0x107,
        "#061F#5P(Heehee! That's so like you, Estelle!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A4")

    label("loc_1158")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1196")

    ChrTalk(    #27
        0x105,
        "#1168F#5P(Haha... That's very Estelle.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A4")

    label("loc_1196")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D8")

    ChrTalk(    #28
        0x109,
        "#1061F#5P(Haha! No need to be embarrassed.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A4")

    label("loc_11D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1219")

    ChrTalk(    #29
        0x104,
        "#031F#5P(Heh... So very like our Estelle.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A4")

    label("loc_1219")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1256")

    ChrTalk(    #30
        0x103,
        "#021F#5P(Heh. The more they change...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A4")

    label("loc_1256")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A4")

    ChrTalk(    #31
        0x108,
        (
            "#071F#1P(Haha! You don't need to be\x01",
            "embarrassed, Estelle.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F2")

    ChrTalk(    #32
        0x106,
        "#051F#5P(In that case, let's get back to the Arseille.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1489")

    label("loc_12F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133F")

    ChrTalk(    #33
        0x108,
        "#070F#1P(Let us return to the Arseille for now, then.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1489")

    label("loc_133F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1389")

    ChrTalk(    #34
        0x104,
        (
            "#035F#5P(Then let us away to our\x01",
            "bird on the mend.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1489")

    label("loc_1389")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E8")

    ChrTalk(    #35
        0x103,
        (
            "#027F#5P(It's likely a good idea to return\x01",
            "to the Arseille in any case.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1489")

    label("loc_13E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1437")

    ChrTalk(    #36
        0x109,
        "#1062F#5P(Anyway, sounds like it's the Arseille for us.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1489")

    label("loc_1437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(    #37
        0x105,
        (
            "#1168F#5P(Let us return to the Arseille for\x01",
            "the moment, then.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1489")


    ChrTalk(    #38
        0x101,
        "#1013F#4P(Uh, yeah...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as saw station terminal\x01",              # 0
            "Set as did not see station terminal\x01",      # 1
            "No change\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_153E"),
        (1, "loc_1544"),
        (SWITCH_DEFAULT, "loc_154A"),
    )


    label("loc_153E")

    OP_A2(0x222F)
    Jump("loc_154A")

    label("loc_1544")

    OP_A3(0x222F)
    Jump("loc_154A")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 7)), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(    #39
        0x102,
        (
            "#1040F#6P(Let's head back to the Halo Rail\x01",
            "station then.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161A")

    label("loc_1593")


    ChrTalk(    #40
        0x102,
        (
            "#1035F#6P(That's going to be a bit of a walk back\x01",
            "to the Arseille from here, though.)\x02\x03",

            "#1040F(Let's try and find a rail station.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161A")


    ChrTalk(    #41
        0x101,
        "#1006F#4P(Good point!)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2220)
    OP_28(0x9E, 0x1, 0x4)
    Jump("loc_1D2E")

    label("loc_1642")


    ChrTalk(    #42
        0x101,
        "#1002F#6P(So this is where the Glorious docked.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B4")

    ChrTalk(    #43
        0x107,
        "#065F#1P(Waaaah! What a huge ship...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_16B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1733")

    ChrTalk(    #44
        0x105,
        (
            "#1167F#1P(Just as Sieg said, it was on the\x01",
            "eastern side of the city...)\x02\x03",

            "#1162F(Still, it's enormous...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1799")

    ChrTalk(    #45
        0x109,
        (
            "#1063F#1P(Sweet Aidios, when you get this close,\x01",
            "you see just how BIG it is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1799")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FC")

    ChrTalk(    #46
        0x103,
        (
            "#025F#1P(It's only when you get this close\x01",
            "that you realize how huge it is.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_17FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1861")

    ChrTalk(    #47
        0x104,
        (
            "#032F#1P(Only when you are this close to it\x01",
            "do you realize how massive it is.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1861")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CE")

    ChrTalk(    #48
        0x106,
        (
            "#555F#1P(Damn. When you're this close, you realize\x01",
            "just how stupidly huge that thing is.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")

    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10B)
    Sleep(500)

    ChrTalk(    #49
        0x10B,
        (
            "#212F#6P(They said their boss is gone, right?\x01",
            "This is the chance I need!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 90, 400)
    Sleep(300)

    ChrTalk(    #50
        0x10B,
        "#210F#4P(Thanks, guys. I'll handle things from here.)\x02",
    )

    CloseMessageWindow()

    def lambda_1989():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1989)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AD")
    TurnDirection(0xF9, 0x10B, 400)
    Jump("loc_19C1")

    label("loc_19AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C1")
    TurnDirection(0xF8, 0x10B, 400)

    label("loc_19C1")


    ChrTalk(    #51
        0x101,
        "#1019F#6P(Uh. Are you, like, sleepwalking or something?)\x02",
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x10B, 0x101, 400)

    ChrTalk(    #52
        0x10B,
        "#216F#4P(What d'you mean?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1040F#5P(You can't seriously expect us to\x01",
            "let you charge in on your own.)\x02\x03",

            "(We'll back you up.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10B,
        "#215F#4P(But...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1022F#6P(Argh, look, this is part of a bracer's\x01",
            "job too, okay?!)\x02\x03",

            "#1009F(Stop being all mopey and get\x01",
            "ready to kick some butt!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10B,
        (
            "#413F#4P(H-Hmph!)\x02\x03",

            "#214F(Just...don't think you can make me owe\x01",
            "you anything by doing this, got it?)\x02\x03",

            "(I don't ever want to be 'friends' with\x01",
            "you, for a whole bunch'a reasons!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1019F#6P(Trust me, feeling's mutual.)\x02\x03",

            "#1007F(Ugh, how can someone younger\x01",
            "than me be less cute than I am?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#1052F#5P(Rrrright...)\x02\x03",

            "#1048F(Anyway. Once we're ready, we'll take\x01",
            "down the guards and board the ship.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 90, 400)

    ChrTalk(    #59
        0x10B,
        "#213F#4P(R-Right...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #60
        0x101,
        "#1013F#6P(Ahem, yes, right.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2221)
    OP_28(0x9E, 0x1, 0x8)

    label("loc_1D2E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(74210, 16000, -100620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74210, 16000, -100620, 180)
    SetChrPos(0x1, 74210, 16000, -100620, 180)
    SetChrPos(0x2, 74210, 16000, -100620, 180)
    SetChrPos(0x3, 74210, 16000, -100620, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_2_461 end

    def Function_3_1DD0(): pass

    label("Function_3_1DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_26F2")
    EventBegin(0x0)
    TurnDirection(0x102, 0x0, 400)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1E18"),
        (1, "loc_1EAB"),
        (10, "loc_1F21"),
        (6, "loc_1FB2"),
        (4, "loc_2042"),
        (8, "loc_20D6"),
        (2, "loc_216B"),
        (3, "loc_2203"),
        (5, "loc_2297"),
        (7, "loc_232A"),
        (14, "loc_23C3"),
        (15, "loc_255A"),
        (SWITCH_DEFAULT, "loc_265C"),
    )


    label("loc_1E18")


    ChrTalk(    #61
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002FYeah, good point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_1EAB")


    ChrTalk(    #63
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_1F21")


    ChrTalk(    #64
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10B,
        "#212FOh, yeah, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_1FB2")


    ChrTalk(    #66
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x107,
        "#062FOh, yeah! Okay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_2042")


    ChrTalk(    #68
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        "#1162FYes, a good point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_20D6")


    ChrTalk(    #70
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x109,
        "#1063FRight. Let's scram.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_216B")


    ChrTalk(    #72
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x103,
        "#022FYou're right. Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_2203")


    ChrTalk(    #74
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x104,
        "#032FAn excellent point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_2297")


    ChrTalk(    #76
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x106,
        "#050FPoint. Let's book.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_232A")


    ChrTalk(    #78
        0x102,
        (
            "#1042FThe security is probably much tighter\x01",
            "beyond here.\x02\x03",

            "Going back in would be foolish.\x01",
            "We should pull out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x108,
        "#072FA good point. Let us go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_23C3")


    ChrTalk(    #80
        0x102,
        (
            "#1042FCaptain, we've broken into the ship once\x01",
            "already. Their security is going to be\x01",
            "absurdly tight at this point.\x02\x03",

            "We don't really have any business inside,\x01",
            "either. I think we should pull back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        (
            "#176F...Blast it all, you're right.\x02\x03",

            "#178FThese are the curs who attacked Grancel...\x01",
            "If we had the manpower, I'd want to\x01",
            "apprehend them all.\x02\x03",

            "Our battle now, however, must focus\x01",
            "on the Axis Pillar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_255A")


    ChrTalk(    #82
        0x110,
        "#270FThat society vessel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#1042FMajor, we've broken into that ship once already.\x01",
            "Their security is going to be absurdly tight at\x01",
            "this point.\x02\x03",

            "We don't really have any business inside,\x01",
            "either. I think we should pull back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x110,
        "#272FAs you say.\x02",
    )

    CloseMessageWindow()
    Jump("loc_265C")

    label("loc_265C")

    Sleep(100)
    Fade(500)
    OP_6D(74210, 16000, -100620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74210, 16000, -100620, 180)
    SetChrPos(0x1, 74210, 16000, -100620, 180)
    SetChrPos(0x2, 74210, 16000, -100620, 180)
    SetChrPos(0x3, 74210, 16000, -100620, 180)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_2D19")

    label("loc_26F2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2717")
    Call(0, 21)
    Call(0, 22)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2751"),
        (1, "loc_27AF"),
        (6, "loc_280C"),
        (4, "loc_286E"),
        (8, "loc_28BC"),
        (2, "loc_2913"),
        (3, "loc_2968"),
        (5, "loc_29CA"),
        (7, "loc_2A27"),
        (SWITCH_DEFAULT, "loc_2A79"),
    )


    label("loc_2751")


    ChrTalk(    #85
        0x101,
        (
            "#1007F(We've got to get back and call Josette.)\x02\x03",

            "#1019F(Always a pain in the butt...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_27AF")


    ChrTalk(    #86
        0x102,
        (
            "#1044F(Wait, no.)\x02\x03",

            "#1042F(We must return to the Arseille\x01",
            "a.s.a.p. and call Josette.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_280C")


    ChrTalk(    #87
        0x107,
        (
            "#065F(N-No, we shouldn't!)\x02\x03",

            "(We need to return to the Arseille\x01",
            "and call the bandit lady!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_286E")


    ChrTalk(    #88
        0x105,
        (
            "#1162F(No...)\x02\x03",

            "(We must return to the Arseille\x01",
            "and let Josette know.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_28BC")


    ChrTalk(    #89
        0x109,
        (
            "#1064F(Ah, wait.)\x02\x03",

            "#1060F(We've got to get that young\x01",
            "lady from the Arseille.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_2913")


    ChrTalk(    #90
        0x103,
        (
            "#023F(Ah, yes.)\x02\x03",

            "#020F(First we should go let Josette\x01",
            "know what's going on.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_2968")


    ChrTalk(    #91
        0x104,
        (
            "#035F(Ah, we should not be hasty.)\x02\x03",

            "#037F(We should go retrieve our lovely\x01",
            "bandit first.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_29CA")


    ChrTalk(    #92
        0x106,
        (
            "#052F(Ah, wait.)\x02\x03",

            "#053F(We gotta go back and let that\x01",
            "bandit girl know what's what.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_2A27")


    ChrTalk(    #93
        0x108,
        (
            "#073F(Wait.)\x02\x03",

            "#070F(First we must let Miss Capua\x01",
            "know what is happening.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A79")

    label("loc_2A79")

    Jump("loc_2C86")

    label("loc_2A7C")

    OP_A2(0x22D4)
    Fade(500)
    OP_6D(74330, 16000, -99550, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 74210, 16000, -98340, 180)
    SetChrPos(0x101, 74330, 16000, -100940, 0)
    SetChrPos(0xF8, 72760, 16000, -100170, 45)
    SetChrPos(0xF9, 75790, 16000, -100350, 315)
    OP_0D()
    Sleep(500)

    ChrTalk(    #94
        0x102,
        (
            "#1042F(Once we go in, we won't be able to disengage\x01",
            "until we rescue the Capuas.)\x02\x03",

            "(Are you sure we're ready to break\x01",
            "into the Glorious?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Go For It\x01",      # 0
            "Wait\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BEC")
    Jump("loc_2C86")

    label("loc_2BEC")


    ChrTalk(    #95
        0x101,
        "#1002F(Okay! Let's go!)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #96
        0x101,
        "#1006F(Capua, make sure you keep up, 'kay?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 400)
    Sleep(300)

    ChrTalk(    #97
        0x10B,
        "#214F(That's my line, airhead!)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 4)

    label("loc_2C86")

    Sleep(100)
    Fade(500)
    OP_6D(74210, 16000, -100620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74210, 16000, -100620, 180)
    SetChrPos(0x1, 74210, 16000, -100620, 180)
    SetChrPos(0x2, 74210, 16000, -100620, 180)
    SetChrPos(0x3, 74210, 16000, -100620, 180)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x2)

    label("loc_2D19")

    Return()

    # Function_3_1DD0 end

    def Function_4_2D1A(): pass

    label("Function_4_2D1A")

    Call(0, 5)
    Call(0, 6)
    Return()

    # Function_4_2D1A end

    def Function_5_2D23(): pass

    label("Function_5_2D23")

    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D48")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x2, 0xF9, 0xFF)

    label("loc_2D48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D63")
    RemoveParty(0x3, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)

    label("loc_2D63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7E")
    RemoveParty(0x4, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x4, 0xF9, 0xFF)

    label("loc_2D7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D99")
    RemoveParty(0x5, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x5, 0xF9, 0xFF)

    label("loc_2D99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB4")
    RemoveParty(0x6, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x6, 0xF9, 0xFF)

    label("loc_2DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DCF")
    RemoveParty(0x7, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x7, 0xF9, 0xFF)

    label("loc_2DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DEA")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x8, 0xF9, 0xFF)

    label("loc_2DEA")

    OP_D2(0x270312, 0x27031C, 0x6)
    OP_D2(0x270316, 0x270320, 0x8)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    OP_D2(0x702B4, 0x702BB, 0xE)
    OP_D2(0x702B5, 0x702BC, 0xF)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2E5F"),
        (3, "loc_2E76"),
        (4, "loc_2E8D"),
        (5, "loc_2EA4"),
        (6, "loc_2EBB"),
        (7, "loc_2ED2"),
        (8, "loc_2EE9"),
        (SWITCH_DEFAULT, "loc_2F00"),
    )


    label("loc_2E5F")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_2F00")

    label("loc_2E76")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_2F00")

    label("loc_2E8D")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_2F00")

    label("loc_2EA4")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_2F00")

    label("loc_2EBB")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_2F00")

    label("loc_2ED2")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_2F00")

    label("loc_2EE9")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_2F00")

    label("loc_2F00")

    OP_D2(0x270313, 0x27031D, 0x12)
    OP_D2(0x270326, 0x270330, 0x13)
    OP_D2(0x270327, 0x270331, 0x14)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0x10B, 14)
    SetChrChipByIndex(0xF9, 16)
    OP_6D(37580, 16000, -75050, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 37090, 16000, -74080, 135)
    SetChrPos(0x9, 40420, 16000, -76420, 270)
    SetChrPos(0xA, 37590, 16000, -77170, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    SetChrPos(0x101, 52000, 16000, -80320, 270)
    SetChrPos(0x102, 53880, 16000, -80190, 270)
    SetChrPos(0x10B, 54210, 16000, -82160, 270)
    SetChrPos(0xF9, 56010, 16000, -82070, 270)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrPos(0x15, 40620, 16000, -75270, 0)
    OP_20(0x3E8)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 41530, 16000, -75450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 40550, 16000, -79030, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrChipByIndex(0x9, 7)

    def lambda_3113():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3113)
    OP_96(0x9, 0x986C, 0x3E80, 0xFFFED702, 0x64, 0x1B58)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 3)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)

    def lambda_3186():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3186)
    Sleep(100)
    OP_8C(0xA, 90, 400)
    OP_43(0x8, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x8)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #98
        0x8,
        "#6PWha-?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        "#5PE-Enemy attack!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x2C)
    Sleep(500)

    def lambda_31EB():
        OP_6D(41870, 16000, -75460, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31EB)

    def lambda_3203():
        OP_67(0, 3690, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3203)

    def lambda_321B():
        OP_6B(3300, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_321B)

    def lambda_322B():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_322B)

    def lambda_323B():
        OP_6E(322, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_323B)
    OP_43(0x101, 0x0, 0x0, 0xA)
    OP_43(0x102, 0x0, 0x0, 0xB)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    OP_43(0x10B, 0x0, 0x0, 0xC)
    OP_43(0x9, 0x1, 0x0, 0x9)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x10B, 0x0)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #100
        0x9,
        "#6PIt's the bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "#6PWasn't your ship down for repairs?!\x02\x03",

            "How did you get HERE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1006F#2PThey're called legs.\x01",
            "You mighta heard of 'em!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10B,
        "#214F#2PGIMME BACK MY BROTHERS!\x02",
    )

    CloseMessageWindow()

    def lambda_3350():
        OP_6D(42000, 16000, -76180, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3350)

    def lambda_3368():
        OP_67(0, 4860, -10000, 350)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3368)

    def lambda_3380():
        OP_6B(2650, 350)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3380)

    def lambda_3390():
        OP_8F(0xFE, 0xAA82, 0x3E80, 0xFFFECFC8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3390)
    Sleep(20)

    def lambda_33B0():
        OP_8F(0xFE, 0xAAD2, 0x3E80, 0xFFFED4B4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33B0)
    SetChrChipByIndex(0x8, 20)
    SetChrFlags(0x8, 0x1000)

    def lambda_33D5():
        OP_8F(0xFE, 0xAC08, 0x3E80, 0xFFFED0E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_33D5)
    Sleep(30)
    SetChrChipByIndex(0x9, 18)
    SetChrFlags(0x9, 0x1000)

    def lambda_33FF():
        OP_8F(0xFE, 0xA6AE, 0x3E80, 0xFFFED338, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_33FF)

    def lambda_341A():
        OP_8F(0xFE, 0xB0C2, 0x3E80, 0xFFFECCF8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_341A)
    Sleep(30)
    SetChrChipByIndex(0xA, 18)
    SetChrFlags(0xA, 0x1000)

    def lambda_3444():
        OP_8F(0xFE, 0xA780, 0x3E80, 0xFFFED13A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3444)

    def lambda_345F():
        OP_8F(0xFE, 0xB022, 0x3E80, 0xFFFED540, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_345F)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10B, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x518, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_34AE"),
        (SWITCH_DEFAULT, "loc_34B3"),
    )


    label("loc_34AE")

    OP_B4(0x0)
    Jump("loc_34B3")

    label("loc_34B3")

    Return()

    # Function_5_2D23 end

    def Function_6_34B4(): pass

    label("Function_6_34B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0x10B, 0x0)
    OP_44(0xF9, 0x0)
    Sleep(500)
    OP_6D(38850, 16000, -75750, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(323000, 0)
    OP_6E(386, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, 39540, 16000, -77330, 270)
    SetChrPos(0x102, 39390, 16000, -75710, 270)
    SetChrPos(0x10B, 41200, 16000, -77800, 270)
    SetChrPos(0xF9, 41070, 16000, -75780, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 37040, 16000, -74990, 0)
    SetChrPos(0x9, 35310, 16000, -76550, 0)
    SetChrPos(0xA, 37100, 16000, -78080, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0x10B, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10B, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0x8, 8)
    SetChrSubChip(0x9, 10)
    SetChrSubChip(0xA, 12)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)

    def lambda_3645():
        OP_6B(2230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3645)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #104
        0x101,
        "#1006F#5POne group down!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #105
        0x102,
        (
            "#1042F#6PAll right, we'll break into the ship here.\x02\x03",

            "Josette, stay close.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x102, 400)

    ChrTalk(    #106
        0x10B,
        "#212F#5PUm, right!\x02",
    )

    CloseMessageWindow()

    def lambda_36FC():
        OP_6D(34850, 16500, -55030, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36FC)

    def lambda_3714():
        OP_67(0, 4920, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3714)

    def lambda_372C():
        OP_6B(5000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_372C)

    def lambda_373C():
        OP_6C(326000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_373C)

    def lambda_374C():
        OP_6E(449, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_374C)
    OP_43(0x102, 0x1, 0x0, 0xF)
    Sleep(100)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    Sleep(50)
    OP_43(0x10B, 0x1, 0x0, 0x11)
    WaitChrThread(0x101, 0x3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5404   ._SN", 147, 0, 0)
    IdleLoop()
    Return()

    # Function_6_34B4 end

    def Function_7_379E(): pass

    label("Function_7_379E")

    OP_8C(0xFE, 90, 400)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_7_379E end

    def Function_8_37B5(): pass

    label("Function_8_37B5")

    OP_8C(0xFE, 90, 400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 6)
    Return()

    # Function_8_37B5 end

    def Function_9_37CC(): pass

    label("Function_9_37CC")


    def lambda_37D2():

        label("loc_37D2")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_37D2")

    QueueWorkItem2(0xFE, 2, lambda_37D2)
    Sleep(200)
    OP_99(0xFE, 0x2, 0x0, 0x12C)
    Sleep(200)
    OP_44(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 6)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_37CC end

    def Function_10_380D(): pass

    label("Function_10_380D")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xB946, 0x3E80, 0xFFFECE92, 0x1388, 0x0)
    Return()

    # Function_10_380D end

    def Function_11_3829(): pass

    label("Function_11_3829")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xB978, 0x3E80, 0xFFFED3E2, 0x1388, 0x0)
    Return()

    # Function_11_3829 end

    def Function_12_3845(): pass

    label("Function_12_3845")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xBFEA, 0x3E80, 0xFFFECB54, 0x1388, 0x0)
    Return()

    # Function_12_3845 end

    def Function_13_3861(): pass

    label("Function_13_3861")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xC026, 0x3E80, 0xFFFED266, 0x1388, 0x0)
    Return()

    # Function_13_3861 end

    def Function_14_387D(): pass

    label("Function_14_387D")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x91B4, 0x3E80, 0xFFFEF070, 0x1B58, 0x0)
    OP_8E(0xFE, 0x91B4, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_14_387D end

    def Function_15_38AD(): pass

    label("Function_15_38AD")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x95CE, 0x3E80, 0xFFFEF066, 0x1B58, 0x0)
    OP_8E(0xFE, 0x95CE, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_15_38AD end

    def Function_16_38DD(): pass

    label("Function_16_38DD")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x9B78, 0x3E80, 0xFFFEF066, 0x1B58, 0x0)
    OP_8E(0xFE, 0x9B78, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_16_38DD end

    def Function_17_390D(): pass

    label("Function_17_390D")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x9664, 0x3E80, 0xFFFEF066, 0x1B58, 0x0)
    OP_8E(0xFE, 0x9664, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_17_390D end

    def Function_18_393D(): pass

    label("Function_18_393D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395F")
    Call(0, 21)
    Call(0, 23)

    label("loc_395F")

    OP_D2(0x270111, 0x270121, 0xA)
    OP_D2(0x270131, 0x270141, 0xB)
    OP_D2(0x702B5, 0x702BC, 0xC)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_39A2"),
        (3, "loc_39AF"),
        (4, "loc_39BC"),
        (5, "loc_39C9"),
        (6, "loc_39D6"),
        (7, "loc_39E3"),
        (8, "loc_39F0"),
        (SWITCH_DEFAULT, "loc_39FD"),
    )


    label("loc_39A2")

    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_39FD")

    label("loc_39AF")

    OP_D2(0x701E9, 0x701F5, 0xD)
    Jump("loc_39FD")

    label("loc_39BC")

    OP_D2(0x27036F, 0x27037C, 0xD)
    Jump("loc_39FD")

    label("loc_39C9")

    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_39FD")

    label("loc_39D6")

    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_39FD")

    label("loc_39E3")

    OP_D2(0x70249, 0x70255, 0xD)
    Jump("loc_39FD")

    label("loc_39F0")

    OP_D2(0x270177, 0x270184, 0xD)
    Jump("loc_39FD")

    label("loc_39FD")

    OP_6D(37920, 16500, -35740, 0)
    OP_67(0, 7220, -10000, 0)
    OP_6B(4870, 0)
    OP_6C(335000, 0)
    OP_6E(351, 0)
    SetChrPos(0x101, 36980, 16500, -28010, 90)
    SetChrPos(0x102, 38630, 16500, -28010, 90)
    SetChrPos(0x10B, 36980, 16500, -28010, 90)
    SetChrPos(0xF9, 38630, 16500, -28010, 90)
    SetChrPos(0xC, 37670, 16500, -28010, 90)
    SetChrPos(0xB, 38190, 16500, -28010, 90)
    SetChrPos(0xD, 39700, 16500, -28010, 90)
    SetChrPos(0xE, 38470, 16500, -28010, 90)
    SetChrPos(0xF, 36850, 16500, -28010, 90)
    SetChrPos(0x10, 39500, 16500, -28010, 90)
    SetChrPos(0x11, 36170, 16500, -28010, 90)
    SetChrPos(0x12, 37760, 16500, -28010, 90)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x10B, 12)
    SetChrChipByIndex(0xF9, 13)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x10B, 0x1000)
    SetChrFlags(0xF9, 0x1000)
    OP_43(0x101, 0x1, 0x0, 0x13)
    FadeToBright(1000, 0)
    Sleep(1000)

    def lambda_3B49():
        OP_6D(35620, 16500, -53400, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B49)

    def lambda_3B61():
        OP_67(0, 6270, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3B61)

    def lambda_3B79():
        OP_6B(5000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3B79)

    def lambda_3B89():
        OP_6C(311000, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_3B89)

    def lambda_3B99():
        OP_6E(403, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_3B99)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_393D end

    def Function_19_3BD0(): pass

    label("Function_19_3BD0")

    OP_43(0x101, 0x2, 0x0, 0x14)
    Sleep(50)
    OP_43(0x102, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x10B, 0x1, 0x0, 0x14)
    Sleep(80)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0xB, 0x1, 0x0, 0x14)
    Sleep(500)
    OP_43(0xD, 0x1, 0x0, 0x14)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xF, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x10, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0x11, 0x1, 0x0, 0x14)
    Sleep(200)
    OP_43(0x12, 0x1, 0x0, 0x14)
    Return()

    # Function_19_3BD0 end

    def Function_20_3C5C(): pass

    label("Function_20_3C5C")

    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFEC780, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_3C5C end

    def Function_21_3C7B(): pass

    label("Function_21_3C7B")

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
        (0, "loc_3CF4"),
        (1, "loc_3CFA"),
        (SWITCH_DEFAULT, "loc_3D00"),
    )


    label("loc_3CF4")

    OP_A2(0x1200)
    Jump("loc_3D00")

    label("loc_3CFA")

    OP_A2(0x1201)
    Jump("loc_3D00")

    label("loc_3D00")

    Return()

    # Function_21_3C7B end

    def Function_22_3D01(): pass

    label("Function_22_3D01")

    FadeToDark(0, 0, -1)
    OP_6D(-344380, 4000, -855980, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_22_3D01 end

    def Function_23_3D94(): pass

    label("Function_23_3D94")

    FadeToDark(0, 0, -1)
    OP_6D(-344380, 4000, -855980, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xA, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_23_3D94 end

    SaveToFile()

Try(main)
