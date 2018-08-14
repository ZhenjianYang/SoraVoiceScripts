from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U2501   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2501.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        '迪恩',                                 # 9
        '雷斯',                                 # 10
        '洛克',                                 # 11
        '',                                     # 12
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
        'ED6_DT07/CH02510 ._CH',             # 00
        'ED6_DT07/CH02520 ._CH',             # 01
        'ED6_DT07/CH02530 ._CH',             # 02
        'ED6_DT07/CH00450 ._CH',             # 03
        'ED6_DT07/CH00451 ._CH',             # 04
        'ED6_DT07/CH00454 ._CH',             # 05
        'ED6_DT07/CH00460 ._CH',             # 06
        'ED6_DT07/CH00461 ._CH',             # 07
        'ED6_DT07/CH00464 ._CH',             # 08
        'ED6_DT07/CH00470 ._CH',             # 09
        'ED6_DT07/CH00471 ._CH',             # 0A
        'ED6_DT07/CH00474 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02510P._CP',             # 00
        'ED6_DT07/CH02520P._CP',             # 01
        'ED6_DT07/CH02530P._CP',             # 02
        'ED6_DT07/CH00450P._CP',             # 03
        'ED6_DT07/CH00451P._CP',             # 04
        'ED6_DT07/CH00454P._CP',             # 05
        'ED6_DT07/CH00460P._CP',             # 06
        'ED6_DT07/CH00461P._CP',             # 07
        'ED6_DT07/CH00464P._CP',             # 08
        'ED6_DT07/CH00470P._CP',             # 09
        'ED6_DT07/CH00471P._CP',             # 0A
        'ED6_DT07/CH00474P._CP',             # 0B
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 123000,
        Y                   = -1000,
        Z                   = 35650,
        Range               = 126920,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x470E,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_18B",          # 01, 1
        "Function_2_19E",          # 02, 2
        "Function_3_1AF",          # 03, 3
        "Function_4_1276",         # 04, 4
        "Function_5_200E",         # 05, 5
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Return()

    # Function_0_18A end

    def Function_1_18B(): pass

    label("Function_1_18B")

    OP_16(0x2, 0xFA0, 0x0, 0xFFFE7960, 0x23004D)
    Return()

    # Function_1_18B end

    def Function_2_19E(): pass

    label("Function_2_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 7)), scpexpr(EXPR_END)), "loc_1A6")
    Return()

    label("loc_1A6")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_19E end

    def Function_3_1AF(): pass

    label("Function_3_1AF")

    EventBegin(0x0)
    OP_E0(238, 0x4C, 0x2)
    OP_E0(238, 0x4D, 0x3)
    OP_E0(239, 0x4E, 0x2)
    OP_E0(239, 0x4F, 0x3)
    OP_E0(240, 0x50, 0x2)
    OP_E0(240, 0x51, 0x3)
    OP_E0(241, 0x52, 0x2)
    OP_E0(241, 0x53, 0x3)
    Fade(500)
    OP_6D(123920, 0, 28610, 0)
    OP_67(0, 8230, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(51000, 0)
    OP_6E(277, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 137580, 0, 28380, 270)
    SetChrPos(0x11, 138190, 0, 26340, 270)
    SetChrPos(0x12, 136390, 0, 27380, 270)
    SetChrPos(0x109, 123540, 0, 27340, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    SetChrPos(0xEF, 123400, 0, 28560, 90)
    SetChrPos(0xF0, 122060, 0, 26970, 90)
    SetChrPos(0xF1, 121870, 0, 28460, 90)
    Jump("loc_337")

    label("loc_2B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0xF0, 123400, 0, 28560, 90)
    SetChrPos(0xEF, 122060, 0, 26970, 90)
    SetChrPos(0xF1, 121870, 0, 28460, 90)
    Jump("loc_337")

    label("loc_2F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337")
    SetChrPos(0xF1, 123400, 0, 28560, 90)
    SetChrPos(0xEF, 122060, 0, 26970, 90)
    SetChrPos(0xF0, 121870, 0, 28460, 90)

    label("loc_337")

    OP_0D()
    Sleep(300)

    NpcTalk(    #0
        0x10,
        "青年的声音",
        (
            "#3P嘿嘿……\x01",
            "终于来了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3E8():
        OP_6D(127110, 500, 28500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E8)

    def lambda_400():
        OP_67(0, 7330, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_400)

    def lambda_418():
        OP_6B(2610, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_418)

    def lambda_428():
        OP_6C(57000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_428)

    def lambda_438():
        OP_6E(338, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_438)

    def lambda_448():
        OP_8F(0xFE, 0x1FA36, 0x0, 0x6BEE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_448)
    Sleep(100)

    def lambda_468():
        OP_8F(0xFE, 0x1FE5A, 0x0, 0x70D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_468)
    Sleep(100)

    def lambda_488():
        OP_8F(0xFE, 0x1FE14, 0x0, 0x67B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_488)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_1D(0xAC)

    ChrTalk(    #1
        0x109,
        "#1064F#6P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x105,
        "#1164F#6P哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_523")

    ChrTalk(    #3
        0x106,
        "#055F#6P是、是你们……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C")

    label("loc_523")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(    #4
        0x101,
        "#1005F#6P是、是你们！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C")

    label("loc_558")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_589")

    ChrTalk(    #5
        0x102,
        "#1504F#6P你们是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C")

    label("loc_589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BE")

    ChrTalk(    #6
        0x104,
        "#1543F#6P哦，是你们……\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C")

    label("loc_5BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EE")

    ChrTalk(    #7
        0x108,
        "#073F#6P你们是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C")

    label("loc_5EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61C")

    ChrTalk(    #8
        0x103,
        "#1523F#6P你们是……\x02",
    )

    CloseMessageWindow()

    label("loc_61C")


    ChrTalk(    #9
        0x10,
        (
            "#1741F#5P嘿嘿，不出所料，\x01",
            "都是些如同鸽子被弹弓\x01",
            "打到了那样的表情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#1751F#11P哇哈哈！\x01",
            "我们会出现在这里，\x01",
            "就让你们感到这么不可思议吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1063F#6P你们是谁啊……\x01",
            "我怎么不记得。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F5")

    ChrTalk(    #12
        0x106,
        (
            "#551F#6P他们是以卢安为根据地，\x01",
            "被称为『渡鸦帮』的\x01",
            "流氓团伙……\x02\x03",

            "#057F应该刚刚取得\x01",
            "准游击士资格才对啊……\x01",
            "怎么会出现在这里！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C2")

    ChrTalk(    #13
        0x101,
        "#1004F#6P嘿，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F2")

    label("loc_7C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F2")

    ChrTalk(    #14
        0x102,
        "#1502F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_7F2")

    Jump("loc_948")

    label("loc_7F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_873")

    ChrTalk(    #15
        0x101,
        (
            "#1007F#6P他们是在卢安市\x01",
            "被称为『渡鸦帮』的\x01",
            "不良团伙……\x02\x03",

            "#1005F可是为什么会出现在这里！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_948")

    label("loc_873")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E3")

    ChrTalk(    #16
        0x102,
        (
            "#1505F#6P他们是在\x01",
            "卢安市被称为\x01",
            "『渡鸦帮』的团伙……\x02\x03",

            "#1502F为什么会在这里？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_948")

    label("loc_8E3")


    ChrTalk(    #17
        0x105,
        (
            "#1163F#6P他们是聚集在\x01",
            "卢安码头那里的\x01",
            "『渡鸦帮』的各位……\x02\x03",

            "不过，为什么会在这里？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_948")


    ChrTalk(    #18
        0x12,
        (
            "#1763F#11P哼，\x01",
            "这我们可不知道。\x02\x03",

            "#1761F只不过是一清醒过来，\x01",
            "就『存在』于这个地方而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        (
            "#1162F#6P『存在』……\x01",
            "听你这种语气，难不成！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1746F#5P是啊，\x01",
            "看来我们并不是本人呢。\x02\x03",

            "#1740F估计是某人准备的\x01",
            "专门用来与你们战斗的冒牌货吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x109,
        (
            "#1065F#6P也就是说和赛雷斯托小姐一样，\x01",
            "在『影之国』中被再现的人格吗。\x02\x03",

            "#1063F要说不一样的地方，\x01",
            "那就是这几位是被『影之王』所再现的……\x02\x03",

            "看来想阻拦我们的干劲十足嘛？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#1750F#2P嘿嘿，虽然跟你们没有过节，\x01",
            "不过看来这就是\x01",
            "『我们』的任务了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    Sleep(50)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 6)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    OP_21()
    OP_1D(0xC4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6B")

    ChrTalk(    #23
        0x12,
        (
            "#1761F#11P那我们也就不客气了，\x01",
            "放马过来吧。\x02\x03",

            "正好还可以让\x01",
            "那边的红毛小子\x01",
            "好好偿还之前欠下的人情……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        "#051F#6P哼……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D17")

    label("loc_C6B")


    ChrTalk(    #25
        0x12,
        (
            "#1761F#11P那我们也就不客气了，\x01",
            "放马过来吧。\x02\x03",

            "也可以让你们见识一下\x01",
            "被那个红毛小子所\x01",
            "训练出来的成果……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1840F#6P红毛小子……\x01",
            "是说阿加特吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D17")


    ChrTalk(    #27
        0x105,
        (
            "#1167F#6P看来这场战斗\x01",
            "似乎无法避免了呢……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 12)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 14)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 16)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 18)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #28
        0x10,
        (
            "#1749F#5P唉……\x01",
            "我也在怀疑为什么会选中我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        "#1756F#11P唉，这也是某种缘分吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "#1766F#11P我可不会手软……\x01",
            "尽管放马过来吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7E")

    ChrTalk(    #31
        0x102,
        "#1506F#6P嘿……！\x02",
    )

    CloseMessageWindow()

    label("loc_E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB4")

    ChrTalk(    #32
        0x10F,
        "#1441F#6P那就不客气了……！\x02",
    )

    CloseMessageWindow()

    label("loc_EB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EEA")

    ChrTalk(    #33
        0x101,
        (
            "#1006F#6P OK～！\x01",
            "正合我意！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(    #34
        0x10B,
        "#210F#6P那就来吧！\x02",
    )

    CloseMessageWindow()

    label("loc_F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F5B")

    ChrTalk(    #35
        0x110,
        (
            "#268F#6P呼……\x01",
            "看来哥哥们真是憋闷得很呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F95")

    ChrTalk(    #36
        0x107,
        (
            "#065F#6P啊……\x01",
            "我、我会努力的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCA")

    ChrTalk(    #37
        0x10A,
        "#816F#6P嗯，来比试一下吧！\x02",
    )

    CloseMessageWindow()

    label("loc_FCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1007")

    ChrTalk(    #38
        0x103,
        (
            "#1536F#6P呵呵……\x01",
            "有这种气势就好！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1007")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_103A")

    ChrTalk(    #39
        0x108,
        "#070F#6P这种气势不错嘛！\x02",
    )

    CloseMessageWindow()

    label("loc_103A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1071")

    ChrTalk(    #40
        0x104,
        (
            "#1545F#6P呵……\x01",
            "来吧，看招！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(    #41
        0x10E,
        "#172F#6P……来吧！\x02",
    )

    CloseMessageWindow()

    label("loc_109E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CD")

    ChrTalk(    #42
        0x10D,
        "#271F#6P……要上了！\x02",
    )

    CloseMessageWindow()

    label("loc_10CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FA")

    ChrTalk(    #43
        0x10C,
        "#114F#6P来吧……！\x02",
    )

    CloseMessageWindow()

    label("loc_10FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1133")

    ChrTalk(    #44
        0x106,
        "#054F#6P让我看看你们的实力吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1133")

    Sleep(300)

    def lambda_113E():
        OP_6D(127600, 0, 28260, 200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_113E)

    def lambda_1156():
        OP_67(0, 8109, -10000, 200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1156)

    def lambda_116E():
        OP_6B(2000, 200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_116E)

    def lambda_117E():
        OP_6E(304, 200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_117E)
    SetChrChipByIndex(0x12, 9)

    def lambda_1193():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1193)
    SetChrChipByIndex(0x10, 4)

    def lambda_11B3():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_11B3)
    SetChrChipByIndex(0x11, 7)

    def lambda_11D3():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_11D3)

    def lambda_11EE():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_11EE)

    def lambda_1209():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1209)

    def lambda_1224():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1224)

    def lambda_123F():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_123F)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x29E, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1AF end

    def Function_4_1276(): pass

    label("Function_4_1276")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x12, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(127810, 200, 28300, 0)
    OP_67(0, 6970, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(57000, 0)
    OP_6E(307, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 130080, 0, 28990, 270)
    SetChrPos(0x11, 129970, 0, 26970, 270)
    SetChrPos(0x12, 128789, 0, 27720, 270)
    OP_43(0x10, 0x3, 0x0, 0x5)
    OP_43(0x11, 0x3, 0x0, 0x5)
    OP_43(0x12, 0x3, 0x0, 0x5)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 3)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x11, 3)
    SetChrChipByIndex(0x12, 11)
    SetChrSubChip(0x12, 3)
    SetChrPos(0x109, 125640, 0, 27100, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B3")
    SetChrPos(0xEF, 125510, 0, 28500, 90)
    SetChrPos(0xF0, 124170, 0, 26900, 90)
    SetChrPos(0xF1, 123920, 0, 28340, 90)
    Jump("loc_1438")

    label("loc_13B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetChrPos(0xF0, 125510, 0, 28500, 90)
    SetChrPos(0xEF, 124170, 0, 26900, 90)
    SetChrPos(0xF1, 123920, 0, 28340, 90)
    Jump("loc_1438")

    label("loc_13F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1438")
    SetChrPos(0xF1, 125510, 0, 28500, 90)
    SetChrPos(0xEF, 124170, 0, 26900, 90)
    SetChrPos(0xF0, 123920, 0, 28340, 90)

    label("loc_1438")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 100, 500, 100, 0, 0, 0, 2000, 2100, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0x11, 100, 500, 100, 0, 0, 0, 2000, 2100, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0x12, 100, 500, 100, 0, 0, 0, 2000, 2100, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0x10,
        "#1749F#5P呼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#1757F浑、浑身酸疼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x12,
        (
            "#1763F#11P嘿……\x01",
            "这就是正游击士\x01",
            "级别的实力吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        (
            "#1066F#6P哎呀……\x01",
            "你们干的也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x105,
        "#1168F#6P呵呵……真是场不错的战斗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16CB")

    ChrTalk(    #50
        0x106,
        (
            "#053F#6P测试的时候我也说过了，\x01",
            "你们欠缺的是经验和心态。\x02\x03",

            "#051F就按照这种步调\x01",
            "好好努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        "#1761F#11P哼，又在装伟大……\x02",
    )

    CloseMessageWindow()
    Jump("loc_178E")

    label("loc_16CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178E")

    ChrTalk(    #52
        0x101,
        (
            "#1001F#6P嗯嗯，真是让我吃了一惊。\x02\x03",

            "#1006F虽说已经知道你们当上了游击士，\x01",
            "不过今天的水平还真是出乎意料啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x11,
        (
            "#1756F哦，\x01",
            "被艾丝蒂尔这么称赞\x01",
            "还真是光荣啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178E")


    ChrTalk(    #54
        0x10,
        (
            "#1746F#5P不管怎么说……\x01",
            "这样一来『我们』的任务\x01",
            "也已经结束了。\x02\x03",

            "#1740F虽然不知道\x01",
            "真正的『我们』会不会\x01",
            "记得这次的切磋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        (
            "#1751F不过再有机会的话，\x01",
            "到时候就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x12,
        (
            "#1763F#11P话说在前面……\x01",
            "在里面等着的家伙\x01",
            "与我们可不是同一级别的。\x02\x03",

            "#1761F你们可要小心，\x01",
            "别被打趴下了哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x10, 0, -500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x4, 0x11, 0, -500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x5, 0x12, 0, -500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)

    def lambda_19AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19AD)

    def lambda_19BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19BF)

    def lambda_19D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_19D1)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1A7F():
        OP_6D(125860, 0, 28600, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A7F)

    def lambda_1A97():
        OP_67(0, 8130, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A97)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #57
        0x105,
        "#1164F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B17")

    ChrTalk(    #58
        0x106,
        (
            "#556F#6P哦……\x01",
            "就这么自说自话地\x01",
            "消失了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B63")

    label("loc_1B17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B63")

    ChrTalk(    #59
        0x104,
        (
            "#1541F#6P呼……\x01",
            "就这么自说自话地\x01",
            "就这样消失了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB2")

    ChrTalk(    #60
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "好像还给了我们\x01",
            "闯关的建议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C94")

    label("loc_1BB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFF")

    ChrTalk(    #61
        0x102,
        (
            "#1514F#6P哈哈……\x01",
            "好像还给了我们\x01",
            "闯关的建议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C94")

    label("loc_1BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4B")

    ChrTalk(    #62
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "好像还给了我们\x01",
            "闯关的建议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C94")

    label("loc_1C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C94")

    ChrTalk(    #63
        0x10A,
        (
            "#811F#6P呵呵……\x01",
            "好像还给了我们\x01",
            "闯关的建议呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDE")

    ChrTalk(    #64
        0x10F,
        (
            "#1447F#6P呵呵……\x01",
            "真是让人恨不起来的几位啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAF")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D25")

    ChrTalk(    #65
        0x10B,
        (
            "#210F#6P呵呵……\x01",
            "真是不遭人恨的家伙们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAF")

    label("loc_1D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6B")

    ChrTalk(    #66
        0x103,
        (
            "#1527F#6P呵呵……\x01",
            "还真是可爱的孩子们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAF")

    label("loc_1D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DAF")

    ChrTalk(    #67
        0x108,
        (
            "#070F#6P哈哈……\x01",
            "一群让人恨不起来的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF2")

    ChrTalk(    #68
        0x110,
        (
            "#261F#6P嘻嘻……\x01",
            "还真是一群老好人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E30")

    label("loc_1DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E30")

    ChrTalk(    #69
        0x10D,
        (
            "#278F#6P呵……\x01",
            "还真是一群老好人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E8C")

    ChrTalk(    #70
        0x10E,
        (
            "#171F#6P哈哈……\x01",
            "他们会成为什么样的游击士，\x01",
            "还真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE5")

    label("loc_1E8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE5")

    ChrTalk(    #71
        0x10C,
        (
            "#111F#6P哈哈……\x01",
            "他们会成为什么样的游击士，\x01",
            "还真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE5")


    ChrTalk(    #72
        0x109,
        (
            "#1065F#5P不过，他们说前面等待着的\x01",
            "不是同一级别的人物……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #73
        0x109,
        (
            "#1063F#12P……我记得前面应该是\x01",
            "一座古旧的建筑物吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)
    Sleep(300)

    ChrTalk(    #74
        0x105,
        (
            "#1167F#5P是的，那是数十年前\x01",
            "使用的石质旧校舍。\x02\x03",

            "#1162F做好完全的准备之后，\x01",
            "再去挑战比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B07)
    OP_28(0x37, 0x1, 0x100)
    OP_28(0x37, 0x1, 0x200)
    OP_28(0x37, 0x1, 0x400)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_1276 end

    def Function_5_200E(): pass

    label("Function_5_200E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202F")
    Sleep(100)
    Jump("loc_20AA")

    label("loc_202F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2044")
    Sleep(200)
    Jump("loc_20AA")

    label("loc_2044")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2059")
    Sleep(300)
    Jump("loc_20AA")

    label("loc_2059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206E")
    Sleep(400)
    Jump("loc_20AA")

    label("loc_206E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2083")
    Sleep(500)
    Jump("loc_20AA")

    label("loc_2083")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2098")
    Sleep(600)
    Jump("loc_20AA")

    label("loc_2098")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AA")
    Sleep(700)

    label("loc_20AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20CC")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_20AA")

    label("loc_20CC")

    Return()

    # Function_5_200E end

    SaveToFile()

Try(main)
