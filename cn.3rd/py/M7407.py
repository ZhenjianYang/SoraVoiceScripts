from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7407   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7407.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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


    DeclActor(
        TriggerX            = 6940,
        TriggerZ            = 0,
        TriggerY            = 42960,
        TriggerRange        = 1000,
        ActorX              = 6940,
        ActorZ              = 1000,
        ActorY              = 42960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 82100,
        TriggerRange        = 2000,
        ActorX              = 0,
        ActorZ              = 1500,
        ActorY              = 82100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_FA",           # 02, 2
        "Function_3_A94",          # 03, 3
        "Function_4_135B",         # 04, 4
        "Function_5_139B",         # 05, 5
        "Function_6_13E0",         # 06, 6
        "Function_7_1425",         # 07, 7
        "Function_8_146A",         # 08, 8
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    OP_72(0x1000, 0x0)
    ExitThread()
    Return()

    # Function_1_F3 end

    def Function_2_FA(): pass

    label("Function_2_FA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890")
    OP_A2(0x2C29)
    Fade(1000)
    OP_6D(340, 6750, 76730, 0)
    OP_67(0, 3130, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(404, 0)
    SetChrPos(0xFA, -750, 0, 78490, 0)
    SetChrPos(0xFB, 750, 0, 78380, 0)
    SetChrPos(0xFC, -1250, 0, 76780, 0)
    SetChrPos(0xFD, 1250, 0, 76810, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_1BB():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_1BB)
    OP_0D()
    WaitChrThread(0xFA, 0x0)
    Fade(500)
    OP_6D(1110, 0, 79950, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(45000, 0)
    OP_6E(357, 0)
    SetChrPos(0xFA, -1120, 0, 78970, 0)
    SetChrPos(0xFB, 410, 0, 78980, 0)
    SetChrPos(0xFC, -1330, 0, 77010, 0)
    SetChrPos(0xFD, 210, 0, 77060, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28F")

    ChrTalk(    #0
        0x101,
        "#1020F#12P这、这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_28F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C3")

    ChrTalk(    #1
        0x102,
        "#1502F#12P这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_2C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FA")

    ChrTalk(    #2
        0x107,
        "#065F#12P这、这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_2FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_333")

    ChrTalk(    #3
        0x10B,
        "#216F#12P怎么了，这扇门……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_333")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B")

    ChrTalk(    #4
        0x10A,
        "#1317F#12P这、这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_36B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5")

    ChrTalk(    #5
        0x105,
        "#1162F#12P……这扇门是………\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_3A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D9")

    ChrTalk(    #6
        0x103,
        "#1522F#12P这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_3D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_410")

    ChrTalk(    #7
        0x106,
        "#057F#12P……这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_447")

    ChrTalk(    #8
        0x108,
        "#072F#12P唔，这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A")

    ChrTalk(    #9
        0x10E,
        "#172F#12P这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_47A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B2")

    ChrTalk(    #10
        0x104,
        "#1542F#12P哦？这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_4B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E5")

    ChrTalk(    #11
        0x10D,
        "#270F#12P这扇门是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_515")

    label("loc_4E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_515")

    ChrTalk(    #12
        0x10C,
        "#112F#12P这扇门是……\x02",
    )

    CloseMessageWindow()

    label("loc_515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55A")

    ChrTalk(    #13
        0x110,
        (
            "#1306F#12P嘻嘻……\x01",
            "似乎不是普通的门呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_55A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A2")

    ChrTalk(    #14
        0x10C,
        (
            "#112F#12P这种气势……\x01",
            "似乎不是普通的门啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_5A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E6")

    ChrTalk(    #15
        0x10D,
        (
            "#276F#12P这种气势……\x01",
            "不是普通的门啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_629")

    ChrTalk(    #16
        0x104,
        (
            "#1540F#12P唔……\x01",
            "似乎不是普通的门呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66D")

    ChrTalk(    #17
        0x10E,
        (
            "#178F#12P这种气势……\x01",
            "不是普通的门啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_66D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AF")

    ChrTalk(    #18
        0x108,
        (
            "#070F#12P哦……\x01",
            "这可不是普通的门啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_6AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EF")

    ChrTalk(    #19
        0x106,
        (
            "#051F#12P哦……　\x01",
            "相当气派的门嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_6EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72E")

    ChrTalk(    #20
        0x103,
        (
            "#1527F#12P哦……\x01",
            "相当气派的门呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_72E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(    #21
        0x105,
        (
            "#1162F#12P这种气势……\x01",
            "不是普通的门呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")

    ChrTalk(    #22
        0x10A,
        (
            "#819F#12P感、感觉……\x01",
            "好像不是普通的门呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_803")

    ChrTalk(    #23
        0x10B,
        (
            "#216F#12P感、感觉……\x01",
            "好像不是普通的门呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_803")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_847")

    ChrTalk(    #24
        0x107,
        (
            "#065F#12P这、这个……\x01",
            "不是普通的门吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88D")

    label("loc_847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88D")

    ChrTalk(    #25
        0x102,
        (
            "#1502F#12P这种气势……\x01",
            "似乎不是普通的门呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88D")

    Jump("loc_944")

    label("loc_890")

    Fade(500)
    OP_6D(1110, 0, 79950, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(45000, 0)
    OP_6E(357, 0)
    SetChrPos(0xFA, -1120, 0, 78970, 0)
    SetChrPos(0xFB, 410, 0, 78980, 0)
    SetChrPos(0xFC, -1330, 0, 77010, 0)
    SetChrPos(0xFD, 210, 0, 77060, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    label("loc_944")


    ChrTalk(    #26
        0x109,
        (
            "#1063F#6P看来这里……\x01",
            "就是『幻影城』的终点了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10F,
        (
            "#1936F#12P……嗯。\x01",
            "我感觉到了姐姐的存在。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFB, 270, 400)
    Sleep(300)

    ChrTalk(    #28
        0x10F,
        "#1933F#11P凯文……怎么办？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C26)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A91")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "打开门\x01",        # 0
            "离开这里\x01",      # 1
        )
    )

    Jump("loc_A45")

    label("loc_A45")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A6B"),
        (SWITCH_DEFAULT, "loc_A7C"),
    )


    label("loc_A6B")

    Call(0, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8E")

    label("loc_A7C")

    Fade(1000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8E")

    label("loc_A8E")

    Jump("loc_A0A")

    label("loc_A91")

    EventEnd(0x0)
    Return()

    # Function_2_FA end

    def Function_3_A94(): pass

    label("Function_3_A94")

    OP_20(0x7D0)

    def lambda_A9F():
        OP_6D(1390, 0, 79820, 1500)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_A9F)

    def lambda_AB7():
        OP_67(0, 5400, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_AB7)

    def lambda_ACF():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0xFA, 2, lambda_ACF)
    OP_8C(0xFA, 180, 400)
    WaitChrThread(0xFA, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C37")

    ChrTalk(    #29
        0x109,
        (
            "#1840F#5P你们两个……\x01",
            "能陪我们来到这里，\x01",
            "真的非常感谢。\x02\x03",

            "话虽如此，希望你们\x01",
            "能再助我一臂之力。\x02\x03",

            "#1065F对手是『影之王』……\x01",
            "能自由操纵这个世界之理的、\x01",
            "至高无上的存在。\x02\x03",

            "#1063F恐怕需要赌上全部\x01",
            "去挑战才行吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D26")

    label("loc_C37")


    ChrTalk(    #30
        0x109,
        (
            "#1840F#5P你们两个……\x01",
            "能陪我们来到这里，\x01",
            "真的非常感谢。\x02\x03",

            "话虽如此，希望你们\x01",
            "能再助我一臂之力。\x02\x03",

            "#1065F对手是『影之王』……\x01",
            "能自由操纵这个世界之理的、\x01",
            "至高无上的存在。\x02\x03",

            "#1063F恐怕需要赌上全部\x01",
            "去挑战才行吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D59")

    ChrTalk(    #31
        0x101,
        "#1006F#12P嗯……当然了！\x02",
    )

    CloseMessageWindow()

    label("loc_D59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8A")

    ChrTalk(    #32
        0x102,
        "#1500F#12P明白了……！\x02",
    )

    CloseMessageWindow()

    label("loc_D8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC6")

    ChrTalk(    #33
        0x10C,
        "#119F#12P早就做好心理准备了……！\x02",
    )

    CloseMessageWindow()

    label("loc_DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF4")

    ChrTalk(    #34
        0x10E,
        "#170F#12P明白……！\x02",
    )

    CloseMessageWindow()

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E28")

    ChrTalk(    #35
        0x106,
        "#051F#12P嘿……交给我吧！\x02",
    )

    CloseMessageWindow()

    label("loc_E28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E61")

    ChrTalk(    #36
        0x108,
        (
            "#070F#12P啊啊……\x01",
            "正如我所愿！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E95")

    ChrTalk(    #37
        0x10D,
        "#275F#12P交给我们吧……！\x02",
    )

    CloseMessageWindow()

    label("loc_E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED2")

    ChrTalk(    #38
        0x107,
        (
            "#067F#12P哇哇……\x01",
            "我、我会努力的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(    #39
        0x10A,
        (
            "#816F#12P嗯！\x01",
            "加油吧！\x02",
        )
    )

    Jump("loc_F0E")

    label("loc_F0E")

    CloseMessageWindow()

    label("loc_F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F48")

    ChrTalk(    #40
        0x105,
        "#1168F#12P我会尽一切努力……！\x02",
    )

    CloseMessageWindow()

    label("loc_F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7D")

    ChrTalk(    #41
        0x10B,
        (
            "#210F#12P哼哼！\x01",
            "那就上吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC3")

    ChrTalk(    #42
        0x103,
        (
            "#1536F#12P呵呵……\x01",
            "事到如今可没法抽身了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(    #43
        0x104,
        (
            "#1541F#12P呼，\x01",
            "终于要拉开最终章的帷幕了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106D")

    ChrTalk(    #44
        0x110,
        (
            "#263F#12P嘻嘻……好啊。\x02\x03",

            "#1306F玲也想和『影之王』\x01",
            "认真比试一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106D")


    ChrTalk(    #45
        0x109,
        "#1075F#5P……太感谢了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFA, 90, 400)
    Sleep(300)

    ChrTalk(    #46
        0x109,
        (
            "#1078F#6P好……\x01",
            "那就上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        "#1938F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    def lambda_10E9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_10E9)
    Sleep(100)
    OP_8C(0xFB, 0, 400)
    OP_1D(0xD4)
    Sleep(500)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_110F():

        label("loc_110F")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_110F")

    QueueWorkItem2(0xFA, 3, lambda_110F)
    Sleep(300)
    OP_22(0x85, 0x1, 0x50)

    def lambda_1134():

        label("loc_1134")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1134")

    QueueWorkItem2(0xFA, 3, lambda_1134)
    Sleep(300)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1159():

        label("loc_1159")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1159")

    QueueWorkItem2(0xFA, 3, lambda_1159)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)
    Sleep(500)
    Fade(1000)
    OP_6D(0, -1000, 81330, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(311, 0)
    SetChrPos(0xFA, -850, 0, 78490, 0)
    SetChrPos(0xFB, 680, 0, 78380, 0)
    SetChrPos(0xFC, -1250, 0, 76780, 0)
    SetChrPos(0xFD, 1190, 0, 76810, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_1235():
        OP_6D(0, 4800, 81080, 7500)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_1235)

    def lambda_124D():
        OP_67(0, 3200, -10000, 7500)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_124D)

    def lambda_1265():
        OP_6B(3820, 7500)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_1265)

    def lambda_1275():
        OP_6E(431, 7500)
        ExitThread()

    QueueWorkItem(0xFD, 1, lambda_1275)
    WaitChrThread(0xFA, 0x1)
    OP_44(0xFA, 0x3)
    OP_23(0xD2)
    OP_23(0x85)

    def lambda_1294():
        OP_7C(0x28, 0x28, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_1294)
    OP_22(0x88, 0x0, 0x64)
    Sleep(2000)

    def lambda_12B6():
        OP_6D(0, 3800, 81080, 10000)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_12B6)

    def lambda_12CE():
        OP_67(0, 2500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xFB, 3, lambda_12CE)

    def lambda_12E6():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0xFC, 3, lambda_12E6)
    OP_43(0xFA, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0xFB, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0xFC, 0x0, 0x0, 0x6)
    Sleep(100)
    OP_43(0xFD, 0x0, 0x0, 0x7)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xFA, 0x0)
    OP_44(0xFB, 0x0)
    OP_44(0xFC, 0x0)
    OP_44(0xFD, 0x0)
    OP_44(0xFA, 0x3)
    OP_44(0xFB, 0x3)
    OP_44(0xFC, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_3_A94 end

    def Function_4_135B(): pass

    label("Function_4_135B")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_137A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_137A)
    OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_4_135B end

    def Function_5_139B(): pass

    label("Function_5_139B")

    Sleep(200)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x2BC, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_13BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13BF)
    OP_8E(0xFE, 0x2BC, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_5_139B end

    def Function_6_13E0(): pass

    label("Function_6_13E0")

    Sleep(330)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_1404():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1404)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_6_13E0 end

    def Function_7_1425(): pass

    label("Function_7_1425")

    Sleep(360)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x44C, 0x0, 0x14FBE, 0x7D0, 0x0)

    def lambda_1449():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1449)
    OP_8E(0xFE, 0x44C, 0x0, 0x157B6, 0x7D0, 0x0)
    Return()

    # Function_7_1425 end

    def Function_8_146A(): pass

    label("Function_8_146A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05有一股不可思议的力量涌出。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    Jump("loc_14D8")

    label("loc_14D8")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1502"),
        (1, "loc_15A0"),
        (SWITCH_DEFAULT, "loc_15A0"),
    )


    label("loc_1502")

    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x82, 0x0)
    OP_1D(0xE1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_15A0")

    TalkEnd(0xFF)
    Return()

    # Function_8_146A end

    SaveToFile()

Try(main)
