from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '强化猎兵',                             # 9
        '强化猎兵',                             # 10
        '强化猎兵',                             # 11
        '多伦',                                 # 12
        '吉尔',                                 # 13
        '空贼',                                 # 14
        '空贼',                                 # 15
        '空贼',                                 # 16
        '空贼',                                 # 17
        '空贼',                                 # 18
        '空贼',                                 # 19
        '空贼',                                 # 20
        '空贼',                                 # 21
        '目标',                                 # 22
        '工业区域『法克特里亚』２',             # 23
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
        "Function_2_47F",          # 02, 2
        "Function_3_1A39",         # 03, 3
        "Function_4_2518",         # 04, 4
        "Function_5_2521",         # 05, 5
        "Function_6_2CBF",         # 06, 6
        "Function_7_2F57",         # 07, 7
        "Function_8_2F6E",         # 08, 8
        "Function_9_2F85",         # 09, 9
        "Function_10_2FC6",        # 0A, 10
        "Function_11_2FE2",        # 0B, 11
        "Function_12_2FFE",        # 0C, 12
        "Function_13_301A",        # 0D, 13
        "Function_14_3036",        # 0E, 14
        "Function_15_3066",        # 0F, 15
        "Function_16_3096",        # 10, 16
        "Function_17_30C6",        # 11, 17
        "Function_18_30F6",        # 12, 18
        "Function_19_336E",        # 13, 19
        "Function_20_33FA",        # 14, 20
        "Function_21_3419",        # 15, 21
        "Function_22_34A0",        # 16, 22
        "Function_23_3533",        # 17, 23
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x518), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E")
    OP_D2(0x270312, 0x27031C, 0x6)
    OP_D2(0x270315, 0x27031F, 0x7)
    OP_D2(0x270316, 0x270320, 0x8)
    OP_D2(0x26020B, 0x260210, 0x9)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    OP_D2(0x702B4, 0x702BB, 0xE)
    OP_D2(0x702B5, 0x702BC, 0xF)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_3DD"),
        (3, "loc_3F4"),
        (4, "loc_40B"),
        (5, "loc_422"),
        (6, "loc_439"),
        (7, "loc_450"),
        (8, "loc_467"),
        (SWITCH_DEFAULT, "loc_47E"),
    )


    label("loc_3DD")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_47E")

    label("loc_3F4")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_47E")

    label("loc_40B")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_47E")

    label("loc_422")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_47E")

    label("loc_439")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_47E")

    label("loc_450")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_47E")

    label("loc_467")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_47E")

    label("loc_47E")

    Return()

    # Function_1_317 end

    def Function_2_47F(): pass

    label("Function_2_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48B")
    Return()

    label("loc_48B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B0")
    Call(0, 21)
    Call(0, 22)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_4B0")

    SetChrPos(0x8, 37090, 16000, -74080, 135)
    SetChrPos(0x9, 40420, 16000, -76420, 270)
    SetChrPos(0xA, 37590, 16000, -77170, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)
    OP_43(0x9, 0x0, 0x6, 0x2)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_62(0x107, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56A")

    label("loc_52D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_62(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56A")

    label("loc_553")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_56A")

    Sleep(1000)
    StopSound(0x186A0, 0x9C400, 0x2710)

    def lambda_582():
        OP_6D(62050, 16000, -34780, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_582)

    def lambda_59A():
        OP_67(0, 10390, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59A)

    def lambda_5B2():
        OP_6B(14610, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B2)

    def lambda_5C2():
        OP_6C(343000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5C2)

    def lambda_5D2():
        OP_6E(599, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D2)
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

    ChrTalk(    #0
        0x9,
        (
            "#4P──想不到会被\x01",
            "带来这种地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#4P接下来要让我们\x01",
            "干什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#5P谁知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#5P不过教授和执行者们\x01",
            "都出去了，看来应该不会\x01",
            "留下什么重大的任务吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#5P顶多就是捕捉\x01",
            "那帮空贼之类的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#6P说到这个……\x01",
            "利贝尔的飞船\x01",
            "应该已经迫降了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "#6P准备好如何应对了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#5P命令上说，在教授他们\x01",
            "回来之前暂时先放着不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#5P反正除了修理飞船之外，\x01",
            "他们什么事情也不能做吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E")
    SetChrPos(0x101, 65519, 16000, -92680, 315)
    SetChrPos(0x102, 65540, 16000, -94040, 315)
    SetChrPos(0xF8, 67240, 16000, -92700, 315)
    SetChrPos(0xF9, 67200, 16000, -94120, 315)
    Jump("loc_8A0")

    label("loc_82E")

    SetChrPos(0x10B, 65519, 16000, -92680, 315)
    SetChrPos(0x101, 65540, 16000, -94040, 315)
    SetChrPos(0x102, 67240, 16000, -92700, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_882")
    SetChrPos(0xF9, 67200, 16000, -94120, 315)
    Jump("loc_8A0")

    label("loc_882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    SetChrPos(0xF8, 67200, 16000, -94120, 315)

    label("loc_8A0")


    def lambda_8A6():
        OP_6D(64690, 16000, -92130, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A6)

    def lambda_8BE():
        OP_67(0, 7850, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BE)
    OP_6C(294000, 5000)
    Fade(500)
    OP_6D(65129, 16000, -94170, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(243000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_970")
    SetChrPos(0x101, 65519, 16000, -92680, 270)
    SetChrPos(0x102, 65540, 16000, -94040, 0)
    SetChrPos(0xF8, 67240, 16000, -92700, 270)
    SetChrPos(0xF9, 67200, 16000, -94120, 0)
    Jump("loc_9E2")

    label("loc_970")

    SetChrPos(0x10B, 65519, 16000, -92680, 270)
    SetChrPos(0x101, 65540, 16000, -94040, 0)
    SetChrPos(0x102, 67240, 16000, -92700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C4")
    SetChrPos(0xF9, 67200, 16000, -94120, 270)
    Jump("loc_9E2")

    label("loc_9C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E2")
    SetChrPos(0xF8, 67200, 16000, -94120, 0)

    label("loc_9E2")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E6")

    ChrTalk(    #9
        0x101,
        (
            "#1020F#6P（『古罗力亚斯』……\x01",
            "  原来停在这里啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A68")

    ChrTalk(    #10
        0x107,
        (
            "#065F#6P（哇……\x01",
            "  好大的飞船……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C05")

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")

    ChrTalk(    #11
        0x105,
        (
            "#1167F#6P（正如基库所说，\x01",
            "  是在浮游都市的东侧呢……）\x02\x03",

            "#1162F（话说回来，还真是大啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C05")

    label("loc_AD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B26")

    ChrTalk(    #12
        0x109,
        (
            "#1063F#6P（嗯～近距离看起来\x01",
            "  还真是大得不可思议……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C05")

    label("loc_B26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B72")

    ChrTalk(    #13
        0x103,
        (
            "#025F#6P（嗯～近距离看起来\x01",
            "  还真是大得不可思议……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C05")

    label("loc_B72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBE")

    ChrTalk(    #14
        0x104,
        (
            "#032F#6P（嗯，就近看的话\x01",
            "  还真是大得不可思议啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C05")

    label("loc_BBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C05")

    ChrTalk(    #15
        0x106,
        (
            "#555F#6P（哟，近看的话\x01",
            "  还真是大得不可思议呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C43")

    ChrTalk(    #16
        0x108,
        (
            "#072F#6P（不过……\x01",
            "  看来是个好机会。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_C43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C81")

    ChrTalk(    #17
        0x106,
        (
            "#057F#6P（不过……\x01",
            "  看来是个好机会。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_C81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBF")

    ChrTalk(    #18
        0x104,
        (
            "#030F#6P（不过……\x01",
            "  看来是个好机会。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFD")

    ChrTalk(    #19
        0x103,
        (
            "#022F#6P（不过……\x01",
            "  看来是个好机会。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_CFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3C")

    ChrTalk(    #20
        0x109,
        (
            "#1063F#6P（不过……\x01",
            "  看来是个好机会。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D78")

    ChrTalk(    #21
        0x105,
        (
            "#1162F#6P（不过……\x01",
            "  看来是个好机会。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D78")


    ChrTalk(    #22
        0x102,
        (
            "#1035F#5P（教授不在，\x01",
            "  确实是个绝佳的机会……）\x02\x03",

            "#1042F（毕竟还要救出空贼团，\x01",
            "  干脆一口气突入如何？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_DF2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_DF2)
    Sleep(50)

    def lambda_E05():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_E05)
    Sleep(250)

    ChrTalk(    #23
        0x101,
        (
            "#1004F#4P（等、等一下。）\x02\x03",

            "#1015F（突入是无所谓，\x01",
            "  不过是不是应该\x01",
            "  给乔丝特打声招呼？？）\x02\x03",

            "（因为要救出的是\x01",
            "  她的哥哥们啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1044F#5P（艾丝蒂尔……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #25
        0x101,
        (
            "#1013F#4P（你、你可别误会哦，）\x02\x03",

            "（我可没替她在\x01",
            "  着想什么的……\x01",
            "  只是……出于游击士的道义而已。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(    #26
        0x107,
        (
            "#061F#6P（嘻嘻……\x01",
            "  真像姐姐的风格。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_F72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB5")

    ChrTalk(    #27
        0x105,
        (
            "#1168F#6P（呵呵……\x01",
            "  真像艾丝蒂尔的风格。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF0")

    ChrTalk(    #28
        0x109,
        (
            "#1061F#6P（哈哈……\x01",
            "  不用害羞吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_FF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102E")

    ChrTalk(    #29
        0x104,
        (
            "#031F#6P（呼……\x01",
            "  没什么好害羞的吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_102E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1068")

    ChrTalk(    #30
        0x103,
        (
            "#021F#6P（呵呵……\x01",
            "  不用害羞吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_1068")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A5")

    ChrTalk(    #31
        0x108,
        (
            "#071F#6P（哈哈……\x01",
            "  没什么好害羞的吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10EF")

    ChrTalk(    #32
        0x106,
        (
            "#051F#6P（那，这样的话\x01",
            "  就暂时先返回埃尔赛尤吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125E")

    label("loc_10EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1139")

    ChrTalk(    #33
        0x108,
        (
            "#070F#6P（好，这样的话\x01",
            "  就暂时先返回埃尔赛尤吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125E")

    label("loc_1139")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1185")

    ChrTalk(    #34
        0x104,
        (
            "#035F#6P（呵呵，这样的话\x01",
            "  就暂时先返回埃尔赛尤吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125E")

    label("loc_1185")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CF")

    ChrTalk(    #35
        0x103,
        (
            "#027F#6P（嗯，这样的话\x01",
            "  就暂时先返回埃尔赛尤吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125E")

    label("loc_11CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121A")

    ChrTalk(    #36
        0x109,
        (
            "#1062F#6P（好，这样的话\x01",
            "  就暂时先返回埃尔赛尤吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125E")

    label("loc_121A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125E")

    ChrTalk(    #37
        0x105,
        (
            "#1168F#6P（这样的话\x01",
            "  就暂时先返回埃尔赛尤吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125E")


    ChrTalk(    #38
        0x101,
        "#1013F#4P（真、真是的……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇看到过车站的终端】\x01",        # 0
            "【◇没看到过车站的终端】\x01",      # 1
            "【◇什么也没有变更】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1313"),
        (1, "loc_1319"),
        (SWITCH_DEFAULT, "loc_131F"),
    )


    label("loc_1313")

    OP_A2(0x222F)
    Jump("loc_131F")

    label("loc_1319")

    OP_A3(0x222F)
    Jump("loc_131F")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 7)), scpexpr(EXPR_END)), "loc_135B")

    ChrTalk(    #39
        0x102,
        (
            "#1040F#5P（那就快点使用\x01",
            "  『光环轨道』吧？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BD")

    label("loc_135B")


    ChrTalk(    #40
        0x102,
        (
            "#1035F#5P（不过，要回埃尔赛尤的话，\x01",
            "  先去找车站会比较快呢。）\x02\x03",

            "#1040F（调查一下工业区域吧）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BD")


    ChrTalk(    #41
        0x101,
        "#1006F#4P（嗯，是啊。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2220)
    OP_28(0x9E, 0x1, 0x4)
    Jump("loc_199C")

    label("loc_13E6")


    ChrTalk(    #42
        0x101,
        (
            "#1002F#5P（『古罗力亚斯』……\x01",
            "  原来停在这里啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1458")

    ChrTalk(    #43
        0x107,
        (
            "#065F#6P（哇……\x01",
            "  好大的飞船……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_1458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(    #44
        0x105,
        (
            "#1167F#6P（正如基库所说，\x01",
            "  是在浮游都市的东侧呢……）\x02\x03",

            "#1162F（话说回来，还真是大啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_14C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1516")

    ChrTalk(    #45
        0x109,
        (
            "#1063F#6P（嗯～近距离看起来\x01",
            "  还真是大得不可思议……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_1516")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1562")

    ChrTalk(    #46
        0x103,
        (
            "#025F#6P（嗯～近距离看起来\x01",
            "  还真是大得不可思议……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_1562")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15AE")

    ChrTalk(    #47
        0x104,
        (
            "#032F#6P（嗯，就近看的话\x01",
            "  还真是大得不可思议啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_15AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F5")

    ChrTalk(    #48
        0x106,
        (
            "#555F#6P（哟，近看的话\x01",
            "  还真是大得不可思议呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F5")

    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10B)
    Sleep(500)

    ChrTalk(    #49
        0x10B,
        (
            "#212F#6P（总之……\x01",
            "  敌人的头目不在，\x01",
            "  看来是个好机会呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 90, 400)
    Sleep(300)

    ChrTalk(    #50
        0x10B,
        (
            "#210F#2P（谢谢你们了。\x01",
            "  接下来我一个人去救哥哥们……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16A5():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16A5)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C9")
    TurnDirection(0xF9, 0x10B, 400)
    Jump("loc_16DD")

    label("loc_16C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DD")
    TurnDirection(0xF8, 0x10B, 400)

    label("loc_16DD")


    ChrTalk(    #51
        0x101,
        (
            "#1019F#5P（我说你啊……\x01",
            "  在说些什么梦话呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x10B, 0x101, 400)

    ChrTalk(    #52
        0x10B,
        "#216F#4P（你、你说什么～！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1040F#6P（怎么可能让你\x01",
            "  自己一个人进去呢？）\x02\x03",

            "（我们也会帮忙的哦。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10B,
        "#215F#2P（可、可是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1022F#5P（哎～这也属于\x01",
            "  游击士的工作范围嘛！）\x02\x03",

            "#1009F（别说废话了，\x01",
            "  快点确认一下装备吧！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10B,
        (
            "#413F#4P（……嗯、嗯…………）\x02\x03",

            "#214F（我先声明，可别指望\x01",
            "  我会感恩图报哦？）\x02\x03",

            "（因为各种原因，\x01",
            "  我可不想和你混熟！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1019F#5P（哼，这句话是我要说的吧。）\x02\x03",

            "#1007F（真是的……\x01",
            "  小小年纪一点也不可爱。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#1052F#6P（咦……）\x02\x03",

            "#1048F（总之做好准备后，\x01",
            "  就将守卫打倒，入侵舰内吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 90, 400)

    ChrTalk(    #59
        0x10B,
        "#213F#2P（嗯、嗯。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #60
        0x101,
        "#1013F#5P（明～白。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2221)
    OP_28(0x9E, 0x1, 0x8)

    label("loc_199C")

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
    EventEnd(0x0)
    Return()

    # Function_2_47F end

    def Function_3_1A39(): pass

    label("Function_3_1A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1F4F")
    EventBegin(0x0)
    TurnDirection(0x102, 0x0, 400)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1A79"),
        (1, "loc_1AE8"),
        (10, "loc_1B3D"),
        (6, "loc_1BAB"),
        (4, "loc_1C19"),
        (8, "loc_1C88"),
        (2, "loc_1CF9"),
        (3, "loc_1D6B"),
        (5, "loc_1DD9"),
        (7, "loc_1E49"),
        (SWITCH_DEFAULT, "loc_1EB9"),
    )


    label("loc_1A79")


    ChrTalk(    #61
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1AE8")


    ChrTalk(    #63
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1B3D")


    ChrTalk(    #64
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10B,
        "#212F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1BAB")


    ChrTalk(    #66
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x107,
        "#062F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1C19")


    ChrTalk(    #68
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        "#1162F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1C88")


    ChrTalk(    #70
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x109,
        "#1063F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1CF9")


    ChrTalk(    #72
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x103,
        "#022F嗯嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1D6B")


    ChrTalk(    #74
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "赶快回头吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x104,
        "#032F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1DD9")


    ChrTalk(    #76
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x106,
        "#050F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1E49")


    ChrTalk(    #78
        0x102,
        (
            "#1042F现在前面的警戒应该\x01",
            "变得相当森严了……\x02\x03",

            "再次潜入的话很危险。\x01",
            "折回去好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x108,
        "#072F好！　明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB9")

    label("loc_1EB9")

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
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2517")

    label("loc_1F4F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F74")
    Call(0, 21)
    Call(0, 22)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_1F74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2297")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1FAE"),
        (1, "loc_2011"),
        (6, "loc_205B"),
        (4, "loc_20A8"),
        (8, "loc_20EE"),
        (2, "loc_2142"),
        (3, "loc_2190"),
        (5, "loc_21EC"),
        (7, "loc_2240"),
        (SWITCH_DEFAULT, "loc_2294"),
    )


    label("loc_1FAE")


    ChrTalk(    #80
        0x101,
        (
            "#1007F（……必须先返回埃尔赛尤\x01",
            "  去叫乔丝特才行。）\x02\x03",

            "#1019F（真是的……\x01",
            "  让人这么费事。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_2011")


    ChrTalk(    #81
        0x102,
        (
            "#1044F（不行……）\x02\x03",

            "#1042F（先返回埃尔赛尤\x01",
            "  去叫乔丝特过来吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_205B")


    ChrTalk(    #82
        0x107,
        (
            "#065F（不、不行。）\x02\x03",

            "（首先要返回埃尔赛尤\x01",
            "  去叫空贼姐姐来才行……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_20A8")


    ChrTalk(    #83
        0x105,
        (
            "#1162F（不行……）\x02\x03",

            "（得先返回埃尔赛尤\x01",
            "  把乔丝特叫来才行。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_20EE")


    ChrTalk(    #84
        0x109,
        (
            "#1064F（且慢……）\x02\x03",

            "#1060F（必须先返回埃尔赛尤\x01",
            "  把空贼小姑娘带来才行呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_2142")


    ChrTalk(    #85
        0x103,
        (
            "#023F（等等……）\x02\x03",

            "#020F（先得返回埃尔赛尤\x01",
            "  把那小姑娘带来才行呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_2190")


    ChrTalk(    #86
        0x104,
        (
            "#035F（呵呵，这可不行。）\x02\x03",

            "#037F（首先得返回埃尔赛尤\x01",
            "  把那只小猫咪给带来才行呢㈱）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_21EC")


    ChrTalk(    #87
        0x106,
        (
            "#052F（等等……）\x02\x03",

            "#053F（先得返回埃尔赛尤\x01",
            "  把那个空贼小姑娘带来才行呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_2240")


    ChrTalk(    #88
        0x108,
        (
            "#073F（等等……）\x02\x03",

            "#070F（先得返回埃尔赛尤\x01",
            "  把那个空贼小姑娘带来才行呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_2294")

    Jump("loc_2484")

    label("loc_2297")

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

    ChrTalk(    #89
        0x102,
        (
            "#1042F（一旦进入了舰内，\x01",
            "  在救出吉尔他们之前\x01",
            "  就没有多余时间逃出来了……）\x02\x03",

            "（要突入『古罗力亚斯』吗？）\x02",
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
            "【突入】\x01",          # 0
            "【还要准备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23F0")
    Jump("loc_2484")

    label("loc_23F0")


    ChrTalk(    #90
        0x101,
        "#1002F#6P（ＯＫ！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #91
        0x101,
        (
            "#1006F#6P（乔丝特……\x01",
            "好好跟着我们哦。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 400)
    Sleep(300)

    ChrTalk(    #92
        0x10B,
        "#214F#5P（这才是我要对你说的。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 4)

    label("loc_2484")

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
    Sleep(50)
    EventEnd(0x4)

    label("loc_2517")

    Return()

    # Function_3_1A39 end

    def Function_4_2518(): pass

    label("Function_4_2518")

    Call(0, 5)
    Call(0, 6)
    Return()

    # Function_4_2518 end

    def Function_5_2521(): pass

    label("Function_5_2521")

    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2546")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x2, 0xF9, 0xFF)

    label("loc_2546")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2561")
    RemoveParty(0x3, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)

    label("loc_2561")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257C")
    RemoveParty(0x4, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x4, 0xF9, 0xFF)

    label("loc_257C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2597")
    RemoveParty(0x5, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x5, 0xF9, 0xFF)

    label("loc_2597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B2")
    RemoveParty(0x6, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x6, 0xF9, 0xFF)

    label("loc_25B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25CD")
    RemoveParty(0x7, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x7, 0xF9, 0xFF)

    label("loc_25CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E8")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0xA, 0xFF)
    AddParty(0xA, 0xF8, 0xFF)
    AddParty(0x8, 0xF9, 0xFF)

    label("loc_25E8")

    OP_D2(0x270312, 0x27031C, 0x6)
    OP_D2(0x270315, 0x27031F, 0x7)
    OP_D2(0x270316, 0x270320, 0x8)
    OP_D2(0x26020B, 0x260210, 0x9)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    OP_D2(0x702B4, 0x702BB, 0xE)
    OP_D2(0x702B5, 0x702BC, 0xF)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2671"),
        (3, "loc_2688"),
        (4, "loc_269F"),
        (5, "loc_26B6"),
        (6, "loc_26CD"),
        (7, "loc_26E4"),
        (8, "loc_26FB"),
        (SWITCH_DEFAULT, "loc_2712"),
    )


    label("loc_2671")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_2712")

    label("loc_2688")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_2712")

    label("loc_269F")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_2712")

    label("loc_26B6")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_2712")

    label("loc_26CD")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_2712")

    label("loc_26E4")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_2712")

    label("loc_26FB")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_2712")

    label("loc_2712")

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

    def lambda_2925():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2925)
    OP_96(0x9, 0x986C, 0x3E80, 0xFFFED702, 0x64, 0x1B58)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 3)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)

    def lambda_2998():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2998)
    Sleep(100)
    OP_8C(0xA, 90, 400)
    OP_43(0x8, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x8)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #93
        0x8,
        "#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        "#5P敌、敌袭！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x2C)
    Sleep(500)

    def lambda_2A00():
        OP_6D(41870, 16000, -75460, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A00)

    def lambda_2A18():
        OP_67(0, 3690, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A18)

    def lambda_2A30():
        OP_6B(3300, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A30)

    def lambda_2A40():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A40)

    def lambda_2A50():
        OP_6E(322, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A50)
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

    ChrTalk(    #95
        0x9,
        "#5P你们……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "#5P你、你们的飞船\x01",
            "应该还在修理中吧！？\x02\x03",

            "你们是怎么来到这里的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1006F#6P不好意思，我们是\x01",
            "用自己的双脚一路走到这里的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10B,
        "#214F#6P把哥哥他们交出来！\x02",
    )

    CloseMessageWindow()

    def lambda_2B5B():
        OP_6D(42000, 16000, -76180, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B5B)

    def lambda_2B73():
        OP_67(0, 4860, -10000, 350)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B73)

    def lambda_2B8B():
        OP_6B(2650, 350)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B8B)

    def lambda_2B9B():
        OP_8F(0xFE, 0xAA82, 0x3E80, 0xFFFECFC8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B9B)
    Sleep(20)

    def lambda_2BBB():
        OP_8F(0xFE, 0xAAD2, 0x3E80, 0xFFFED4B4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2BBB)
    SetChrChipByIndex(0x8, 20)
    SetChrFlags(0x8, 0x1000)

    def lambda_2BE0():
        OP_8F(0xFE, 0xAC08, 0x3E80, 0xFFFED0E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2BE0)
    Sleep(30)
    SetChrChipByIndex(0x9, 18)
    SetChrFlags(0x9, 0x1000)

    def lambda_2C0A():
        OP_8F(0xFE, 0xA6AE, 0x3E80, 0xFFFED338, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2C0A)

    def lambda_2C25():
        OP_8F(0xFE, 0xB0C2, 0x3E80, 0xFFFECCF8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_2C25)
    Sleep(30)
    SetChrChipByIndex(0xA, 18)
    SetChrFlags(0xA, 0x1000)

    def lambda_2C4F():
        OP_8F(0xFE, 0xA780, 0x3E80, 0xFFFED13A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2C4F)

    def lambda_2C6A():
        OP_8F(0xFE, 0xB022, 0x3E80, 0xFFFED540, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2C6A)
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
        (1, "loc_2CB9"),
        (SWITCH_DEFAULT, "loc_2CBE"),
    )


    label("loc_2CB9")

    OP_B4(0x0)
    Jump("loc_2CBE")

    label("loc_2CBE")

    Return()

    # Function_5_2521 end

    def Function_6_2CBF(): pass

    label("Function_6_2CBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
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
    SetChrPos(0x101, 39540, 16000, -77330, 270)
    SetChrPos(0x102, 39390, 16000, -75710, 270)
    SetChrPos(0x10B, 41200, 16000, -77800, 270)
    SetChrPos(0xF9, 41070, 16000, -75780, 270)
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

    def lambda_2E0A():
        OP_6B(2230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E0A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #99
        0x101,
        "#1006F#6P好，解决了一批！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #100
        0x102,
        (
            "#1042F#5P很好……\x01",
            "就这样一口气突入舰内吧。\x02\x03",

            "乔丝特，跟着我们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x102, 400)

    ChrTalk(    #101
        0x10B,
        "#212F#6P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    def lambda_2EB5():
        OP_6D(34850, 16500, -55030, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EB5)

    def lambda_2ECD():
        OP_67(0, 4920, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2ECD)

    def lambda_2EE5():
        OP_6B(5000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2EE5)

    def lambda_2EF5():
        OP_6C(326000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2EF5)

    def lambda_2F05():
        OP_6E(449, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F05)
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

    # Function_6_2CBF end

    def Function_7_2F57(): pass

    label("Function_7_2F57")

    OP_8C(0xFE, 90, 400)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_7_2F57 end

    def Function_8_2F6E(): pass

    label("Function_8_2F6E")

    OP_8C(0xFE, 90, 400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 6)
    Return()

    # Function_8_2F6E end

    def Function_9_2F85(): pass

    label("Function_9_2F85")


    def lambda_2F8B():

        label("loc_2F8B")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_2F8B")

    QueueWorkItem2(0xFE, 2, lambda_2F8B)
    Sleep(200)
    OP_99(0xFE, 0x2, 0x0, 0x12C)
    Sleep(200)
    OP_44(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 6)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_2F85 end

    def Function_10_2FC6(): pass

    label("Function_10_2FC6")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xB946, 0x3E80, 0xFFFECE92, 0x1388, 0x0)
    Return()

    # Function_10_2FC6 end

    def Function_11_2FE2(): pass

    label("Function_11_2FE2")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xB978, 0x3E80, 0xFFFED3E2, 0x1388, 0x0)
    Return()

    # Function_11_2FE2 end

    def Function_12_2FFE(): pass

    label("Function_12_2FFE")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xBFEA, 0x3E80, 0xFFFECB54, 0x1388, 0x0)
    Return()

    # Function_12_2FFE end

    def Function_13_301A(): pass

    label("Function_13_301A")

    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xC026, 0x3E80, 0xFFFED266, 0x1388, 0x0)
    Return()

    # Function_13_301A end

    def Function_14_3036(): pass

    label("Function_14_3036")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x91B4, 0x3E80, 0xFFFEF070, 0x1B58, 0x0)
    OP_8E(0xFE, 0x91B4, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_14_3036 end

    def Function_15_3066(): pass

    label("Function_15_3066")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x95CE, 0x3E80, 0xFFFEF066, 0x1B58, 0x0)
    OP_8E(0xFE, 0x95CE, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_15_3066 end

    def Function_16_3096(): pass

    label("Function_16_3096")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x9B78, 0x3E80, 0xFFFEF066, 0x1B58, 0x0)
    OP_8E(0xFE, 0x9B78, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_16_3096 end

    def Function_17_30C6(): pass

    label("Function_17_30C6")

    OP_8C(0xFE, 0, 600)
    OP_8E(0xFE, 0x9664, 0x3E80, 0xFFFEF066, 0x1B58, 0x0)
    OP_8E(0xFE, 0x9664, 0x4074, 0xFFFF8DFA, 0x1B58, 0x0)
    Return()

    # Function_17_30C6 end

    def Function_18_30F6(): pass

    label("Function_18_30F6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310D")
    Call(0, 21)
    Call(0, 23)

    label("loc_310D")

    OP_D2(0x270111, 0x270121, 0xA)
    OP_D2(0x270131, 0x270141, 0xB)
    OP_D2(0x702B5, 0x702BC, 0xC)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_3150"),
        (3, "loc_315D"),
        (4, "loc_316A"),
        (5, "loc_3177"),
        (6, "loc_3184"),
        (7, "loc_3191"),
        (8, "loc_319E"),
        (SWITCH_DEFAULT, "loc_31AB"),
    )


    label("loc_3150")

    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_31AB")

    label("loc_315D")

    OP_D2(0x701E9, 0x701F5, 0xD)
    Jump("loc_31AB")

    label("loc_316A")

    OP_D2(0x27036F, 0x27037C, 0xD)
    Jump("loc_31AB")

    label("loc_3177")

    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_31AB")

    label("loc_3184")

    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_31AB")

    label("loc_3191")

    OP_D2(0x70249, 0x70255, 0xD)
    Jump("loc_31AB")

    label("loc_319E")

    OP_D2(0x270177, 0x270184, 0xD)
    Jump("loc_31AB")

    label("loc_31AB")

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

    def lambda_32F7():
        OP_6D(35620, 16500, -53400, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_32F7)

    def lambda_330F():
        OP_67(0, 6270, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_330F)

    def lambda_3327():
        OP_6B(5000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3327)

    def lambda_3337():
        OP_6C(311000, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_3337)

    def lambda_3347():
        OP_6E(403, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_3347)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_30F6 end

    def Function_19_336E(): pass

    label("Function_19_336E")

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

    # Function_19_336E end

    def Function_20_33FA(): pass

    label("Function_20_33FA")

    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFEC780, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_33FA end

    def Function_21_3419(): pass

    label("Function_21_3419")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3493"),
        (1, "loc_3499"),
        (SWITCH_DEFAULT, "loc_349F"),
    )


    label("loc_3493")

    OP_A2(0x1200)
    Jump("loc_349F")

    label("loc_3499")

    OP_A2(0x1201)
    Jump("loc_349F")

    label("loc_349F")

    Return()

    # Function_21_3419 end

    def Function_22_34A0(): pass

    label("Function_22_34A0")

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

    # Function_22_34A0 end

    def Function_23_3533(): pass

    label("Function_23_3533")

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

    # Function_23_3533 end

    SaveToFile()

Try(main)
