from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'E0013_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0013_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_86D",          # 01, 1
        "Function_2_8E1",          # 02, 2
        "Function_3_913",          # 03, 3
        "Function_4_945",          # 04, 4
        "Function_5_99C",          # 05, 5
        "Function_6_A2D",          # 06, 6
        "Function_7_A7C",          # 07, 7
        "Function_8_ACB",          # 08, 8
        "Function_9_B2B",          # 09, 9
        "Function_10_15B3",        # 0A, 10
        "Function_11_1606",        # 0B, 11
        "Function_12_1656",        # 0C, 12
        "Function_13_16AB",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B")
    SetChrPos(0x101, 87360, 0, -6520, 0)
    SetChrPos(0x103, 86500, 100, -7110, 0)
    SetChrPos(0xF8, 87360, 100, -7640, 0)
    SetChrPos(0xF9, 86500, 100, -8410, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, 87360, 100, -7640, 0)
    SetChrPos(0xF8, 86500, 100, -8410, 0)

    label("loc_12B")

    OP_6D(87000, 0, 4940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_177():
        OP_6D(87000, 0, -2480, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_177)
    Sleep(400)

    def lambda_194():
        OP_8E(0xFE, 0x15540, 0x0, 0xFFFFF8A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_194)
    Sleep(1000)

    def lambda_1B4():
        OP_8E(0xFE, 0x151E4, 0x0, 0xFFFFF466, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B4)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F9")

    def lambda_1E1():
        OP_8E(0xFE, 0x151E4, 0x0, 0xFFFFEEA8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1E1)
    Jump("loc_214")

    label("loc_1F9")


    def lambda_1FF():
        OP_8E(0xFE, 0x15540, 0x0, 0xFFFFF222, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1FF)

    label("loc_214")

    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244")

    def lambda_22C():
        OP_8E(0xFE, 0x15540, 0x0, 0xFFFFF222, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_22C)
    Jump("loc_25F")

    label("loc_244")


    def lambda_24A():
        OP_8E(0xFE, 0x151E4, 0x0, 0xFFFFEEA8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_24A)

    label("loc_25F")

    WaitChrThread(0x101, 0x0)
    Sleep(400)
    OP_8C(0x101, 90, 400)
    Sleep(400)
    OP_8C(0x101, 315, 400)
    Sleep(800)
    OP_8C(0x101, 0, 400)
    Jump("loc_400")

    label("loc_28B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(96680, 0, 3000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    OP_6F(0x2, 59)
    FadeToBright(2000, 0)

    def lambda_2FE():
        OP_6D(87190, 0, 2230, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2FE)
    Sleep(1500)
    Sleep(400)
    OP_43(0x101, 0x0, 0x1, 0x1)
    Sleep(1000)
    OP_43(0x103, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_43(0xF8, 0x0, 0x1, 0x3)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x1, 0x4)
    WaitChrThread(0x101, 0x0)
    Jump("loc_400")

    label("loc_34D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(82680, 0, 3000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    FadeToBright(2000, 0)

    def lambda_3B9():
        OP_6D(87180, 0, 3000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B9)
    Sleep(3000)
    OP_43(0x101, 0x0, 0x1, 0x5)
    Sleep(1000)
    OP_43(0x103, 0x0, 0x1, 0x6)
    Sleep(1000)
    OP_43(0xF8, 0x0, 0x1, 0x7)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x1, 0x8)
    WaitChrThread(0x101, 0x0)

    label("loc_400")


    ChrTalk(    #0
        0x101,
        (
            "#1004F哇……\x01",
            "真是好暗啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_452")

    ChrTalk(    #1
        0x107,
        (
            "#060F嗯……\x01",
            "导力灯也熄灭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC")

    label("loc_452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_489")

    ChrTalk(    #2
        0x105,
        (
            "#040F嗯，灯光也都\x01",
            "完全熄灭了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC")

    label("loc_489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CA")

    ChrTalk(    #3
        0x108,
        (
            "#070F嗯，没有导力灯，\x01",
            "而且今晚也没有月光。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC")

    label("loc_4CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FC")

    ChrTalk(    #4
        0x104,
        (
            "#030F嗯，灯光也都\x01",
            "完全熄灭了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_562")

    ChrTalk(    #5
        0x106,
        (
            "#552F不过，这无人的\x01",
            "座位给人感觉真不舒服。\x02\x03",

            "现在好像都还能\x01",
            "听见说话的声音一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F")

    label("loc_562")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A7")

    ChrTalk(    #6
        0x104,
        (
            "#030F不过，现在好像都还能\x01",
            "听见乘客的声音一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F")

    label("loc_5A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EC")

    ChrTalk(    #7
        0x108,
        (
            "#070F不过，现在好像都还能\x01",
            "听见乘客的声音一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F")

    label("loc_5EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63F")

    ChrTalk(    #8
        0x105,
        (
            "#040F不过，白天的喧闹\x01",
            "好像还残留着呢。\x02\x03",

            "让人回忆起\x01",
            "夜间的校舍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F")


    ChrTalk(    #9
        0x103,
        (
            "#026F嗯，让人有点不舒服。\x02\x03",

            "感觉会有什么鬼怪跳出来似的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_9E(0x101, 0xA, 0x0, 0x1F4, 0xBB8)
    Sleep(400)

    ChrTalk(    #10
        0x101,
        "#1019F唔…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6F6")

    ChrTalk(    #11
        0x103,
        (
            "#023F咦，你现在还怕\x01",
            "那种事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71E")

    label("loc_6F6")


    ChrTalk(    #12
        0x103,
        (
            "#023F咦，你还没克服\x01",
            "幽灵恐惧症吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_734")
    OP_8C(0x101, 180, 400)
    Jump("loc_73B")

    label("loc_734")

    OP_8C(0x101, 0, 400)

    label("loc_73B")


    ChrTalk(    #13
        0x101,
        (
            "#1022F啊，先别说这个了！\x02\x03",

            "#1005F好了，赶快找到猫，\x01",
            "然后从这里撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BD")

    ChrTalk(    #14
        0x108,
        (
            "#070F说得也是……\x01",
            "那么就开工吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_864")

    label("loc_7BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F2")

    ChrTalk(    #15
        0x106,
        (
            "#050F嗯，是啊。\x01",
            "那么就开工吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_864")

    label("loc_7F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_839")

    ChrTalk(    #16
        0x104,
        (
            "#030F那么，赶快开始吧。\x02\x03",

            "维修员也在\x01",
            "等着我们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_864")

    label("loc_839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_864")

    ChrTalk(    #17
        0x105,
        "#040F嗯，那么就开始吧。\x02",
    )

    CloseMessageWindow()

    label("loc_864")

    OP_28(0x74, 0x1, 0x4000)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_86D(): pass

    label("Function_1_86D")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x157A2, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x153CE, 0x0, 0x726, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(800)
    OP_8C(0x101, 135, 400)
    Sleep(800)
    OP_8C(0x101, 180, 400)
    Sleep(1000)
    Return()

    # Function_1_86D end

    def Function_2_8E1(): pass

    label("Function_2_8E1")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1511C, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_2_8E1 end

    def Function_3_913(): pass

    label("Function_3_913")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x156D0, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_913 end

    def Function_4_945(): pass

    label("Function_4_945")

    SetChrPos(0xFE, 90790, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x15C34, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_72(0x2, 0x800)
    OP_70(0x2, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x2)
    Sleep(1000)
    OP_71(0x2, 0x800)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_945 end

    def Function_5_99C(): pass

    label("Function_5_99C")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C3)
    OP_8E(0xFE, 0x14FD2, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x153CE, 0x0, 0x726, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(800)
    OP_8C(0x101, 135, 400)
    Sleep(800)
    OP_8C(0x101, 180, 400)
    Sleep(1000)
    Return()

    # Function_5_99C end

    def Function_6_A2D(): pass

    label("Function_6_A2D")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A54():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A54)
    OP_8E(0xFE, 0x15694, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_A2D end

    def Function_7_A7C(): pass

    label("Function_7_A7C")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AA3)
    OP_8E(0xFE, 0x150F4, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_A7C end

    def Function_8_ACB(): pass

    label("Function_8_ACB")

    SetChrPos(0xFE, 82560, 100, 2860, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AF2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF2)
    OP_8E(0xFE, 0x14A8C, 0x0, 0xB2C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_ACB end

    def Function_9_B2B(): pass

    label("Function_9_B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B45")
    Return()

    label("loc_B45")

    EventBegin(0x0)
    SoundLoad(348)
    Fade(1000)
    OP_6D(30000, 0, 7620, 0)
    OP_67(0, 10620, -10000, 0)
    SetChrPos(0x101, 30000, 0, 5860, 0)
    SetChrPos(0xF7, 29320, 0, 4760, 0)
    SetChrPos(0xF8, 30680, 0, 4760, 0)
    SetChrPos(0xF9, 30000, 0, 3770, 0)
    OP_6D(30270, 0, 6020, 0)
    OP_67(0, 10620, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(59000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrPos(0x8, 27420, 400, 10420, 90)
    OP_22(0x192, 0x0, 0x64)

    NpcTalk(    #18
        0x8,
        "鸣叫声",
        "#6P喵～～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #19
        0x101,
        "#1004F#2P啊！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C81")

    ChrTalk(    #20
        0x107,
        "#064F刚、刚才的叫声是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D06")

    label("loc_C81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CAB")

    ChrTalk(    #21
        0x105,
        "#044F刚才的叫声……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D06")

    label("loc_CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDB")

    ChrTalk(    #22
        0x104,
        "#033F哎呀，刚才的叫声……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D06")

    label("loc_CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #23
        0x106,
        "#052F刚才有叫声传过来。\x02",
    )

    CloseMessageWindow()

    label("loc_D06")


    def lambda_D0C():
        OP_6D(30000, 0, 7620, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D0C)

    def lambda_D24():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_D24)

    def lambda_D34():
        OP_67(0, 10620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_D34)
    OP_43(0x8, 0x0, 0x1, 0xA)

    def lambda_D53():
        OP_94(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D53)
    Sleep(150)

    def lambda_D6E():
        OP_94(0x1, 0xF7, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_D6E)
    Sleep(150)

    def lambda_D89():
        OP_94(0x1, 0xF8, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_D89)
    Sleep(150)

    def lambda_DA4():
        OP_94(0x1, 0xF9, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_DA4)
    WaitChrThread(0x8, 0x0)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #24
        0x8,
        "喵～～\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 2)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DE7")
    OP_A2(0x1)

    label("loc_DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E67")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过【小猫的搜索】】\x01",        # 0
            "【◇没完成过【小猫的搜索】】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E5B"),
        (1, "loc_E61"),
        (SWITCH_DEFAULT, "loc_E67"),
    )


    label("loc_E5B")

    OP_A2(0x1)
    Jump("loc_E67")

    label("loc_E61")

    OP_A3(0x1)
    Jump("loc_E67")

    label("loc_E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EA8")

    ChrTalk(    #25
        0x101,
        (
            "#1016F#2P找到你了，安莉尔。\x02\x03",

            "你还是一样地调皮呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDA")

    label("loc_EA8")


    ChrTalk(    #26
        0x101,
        (
            "#1001F#2P终于找到了～\x02\x03",

            "她大概就是\x01",
            "安莉尔吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDA")


    ChrTalk(    #27
        0x103,
        (
            "#020F#3P和委托人描述的一样，\x01",
            "是褐色的毛色……\x02\x03",

            "应该是这只猫了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F54")

    ChrTalk(    #28
        0x105,
        (
            "#048F太好了……\x01",
            "顺利找到了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1015")

    label("loc_F54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(    #29
        0x107,
        (
            "#561F太、太好了……\x01",
            "顺利找到了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1015")

    label("loc_F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCF")

    ChrTalk(    #30
        0x104,
        (
            "#030F看来确实如此呢。\x02\x03",

            "她能没事真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1015")

    label("loc_FCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1015")

    ChrTalk(    #31
        0x106,
        (
            "#051F看来的确是这样啊。\x02\x03",

            "真是的……\x01",
            "终于找到了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1015")


    ChrTalk(    #32
        0x101,
        (
            "#1015F#2P都是你害我们\x01",
            "走了那么多路。\x02\x03",

            "你躲在这里\x01",
            "到底要干什么啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #33
        0x8,
        "喵～～\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 27420, 400, 10420, 90)
    SetChrPos(0xA, 27420, 400, 10420, 90)
    SetChrPos(0xB, 27420, 400, 10420, 90)
    OP_22(0x15C, 0x0, 0x64)

    ChrTalk(    #34
        0x9,
        "咪～\x02",
    )

    CloseMessageWindow()
    OP_22(0x15C, 0x0, 0x64)

    ChrTalk(    #35
        0xA,
        "咪咪～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1011F#2P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_10E2():
        OP_6D(30000, 0, 7000, 2000)
        ExitThread()

    QueueWorkItem(0xF6, 3, lambda_10E2)

    def lambda_10FA():
        OP_6B(2350, 2000)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_10FA)

    def lambda_110A():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_110A)

    def lambda_111A():
        OP_67(0, 10680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_111A)
    OP_43(0x9, 0x0, 0x1, 0xB)
    OP_43(0xA, 0x0, 0x1, 0xC)
    OP_43(0xB, 0x0, 0x1, 0xD)
    Sleep(3000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11D9")

    label("loc_119B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C2")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11D9")

    label("loc_11C2")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_11D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1200")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_123E")

    label("loc_1200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1227")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_123E")

    label("loc_1227")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_123E")


    ChrTalk(    #37
        0x101,
        "#1004F#1P啊啊！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1281")

    ChrTalk(    #38
        0x107,
        "#065F小、小猫……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_12FC")

    label("loc_1281")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A9")

    ChrTalk(    #39
        0x105,
        "#044F小猫……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_12FC")

    label("loc_12A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D7")

    ChrTalk(    #40
        0x104,
        "#031F哟，这可不得了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12FC")

    label("loc_12D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FC")

    ChrTalk(    #41
        0x106,
        "#052F真让人吃惊。\x02",
    )

    CloseMessageWindow()

    label("loc_12FC")

    WaitChrThread(0xB, 0x0)

    ChrTalk(    #42
        0x103,
        (
            "#021F呵呵，好可爱㈱\x01",
            "好像是刚出生的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1015F那、那么……\x01",
            "就是说是在这里出生的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D8")

    ChrTalk(    #44
        0x108,
        (
            "#070F嗯，有可能是为了\x01",
            "产仔才潜入了这里。\x02\x03",

            "虽然说是为了找个安全的地方，\x01",
            "不过母亲的伟大真令人佩服……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_13D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1444")

    ChrTalk(    #45
        0x106,
        (
            "#051F嗯，有可能是为了\x01",
            "产仔才来这里的。\x02\x03",

            "不知道是不是动物的本能，\x01",
            "不过母亲真是伟大啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_1444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AA")

    ChrTalk(    #46
        0x105,
        (
            "#047F嗯，有可能是为了\x01",
            "产仔才潜入了这里。\x02\x03",

            "为了寻找对孩子们来说\x01",
            "最安全的地方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_14AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1516")

    ChrTalk(    #47
        0x107,
        (
            "#060F有可能是为了\x01",
            "产仔才潜入了这里……\x02\x03",

            "#067F嘿嘿，这么这么小却又\x01",
            "是个非常伟大的妈妈呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1516")


    ChrTalk(    #48
        0x101,
        (
            "#1007F#2P呼，不过也没必要\x01",
            "跑到飞船上吧……\x02\x03",

            "#1000F好了，算了。\x01",
            "现在得回去报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x103,
        (
            "#021F嗯，是啊。\x02\x03",

            "想必阿姨也会\x01",
            "吓一跳吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0136   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_9_B2B end

    def Function_10_15B3(): pass

    label("Function_10_15B3")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7530, 0x0, 0x24CC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7530, 0x0, 0x1F54, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_15B3 end

    def Function_11_1606(): pass

    label("Function_11_1606")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0x3E8, 0x0)
    OP_8E(0xFE, 0x767A, 0x0, 0x22E2, 0x3E8, 0x0)
    OP_43(0x9, 0x2, 0x0, 0x2)
    TurnDirection(0xFE, 0x8, 400)
    ClearChrFlags(0xFE, 0x4)
    OP_A6(0x0)
    OP_43(0x9, 0x1, 0x0, 0x3)
    Return()

    # Function_11_1606 end

    def Function_12_1656(): pass

    label("Function_12_1656")

    Sleep(1500)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0x3E8, 0x0)
    OP_8E(0xFE, 0x73E6, 0x0, 0x23DC, 0x3E8, 0x0)
    OP_43(0xA, 0x2, 0x0, 0x2)
    TurnDirection(0xFE, 0x8, 400)
    ClearChrFlags(0xFE, 0x4)
    OP_A6(0x0)
    OP_43(0xA, 0x1, 0x0, 0x3)
    Return()

    # Function_12_1656 end

    def Function_13_16AB(): pass

    label("Function_13_16AB")

    Sleep(3000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x724C, 0xC8, 0x28B4, 0x3E8, 0x0)
    OP_8E(0xFE, 0x751C, 0x0, 0x25F8, 0x3E8, 0x0)
    OP_43(0xB, 0x2, 0x0, 0x2)
    TurnDirection(0xFE, 0x8, 400)
    ClearChrFlags(0xFE, 0x4)
    OP_A2(0x0)
    OP_43(0xB, 0x1, 0x0, 0x3)
    Return()

    # Function_13_16AB end

    SaveToFile()

Try(main)
