from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5308   ._SN',
        MapName             = 'Other',
        Location            = 'C5308.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        '怪盗布卢布兰',                         # 9
        '跳梁小丑',                             # 10
        '跳梁小丑',                             # 11
        '目标用照相机',                         # 12
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 32500,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = 32500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_14E",          # 00, 0
        "Function_1_19C",          # 01, 1
        "Function_2_1D3",          # 02, 2
        "Function_3_364",          # 03, 3
        "Function_4_36D",          # 04, 4
        "Function_5_1E35",         # 05, 5
        "Function_6_2688",         # 06, 6
        "Function_7_26D0",         # 07, 7
        "Function_8_2746",         # 08, 8
        "Function_9_27BC",         # 09, 9
        "Function_10_27E2",        # 0A, 10
        "Function_11_2808",        # 0B, 11
        "Function_12_282E",        # 0C, 12
        "Function_13_2854",        # 0D, 13
        "Function_14_2883",        # 0E, 14
        "Function_15_2898",        # 0F, 15
        "Function_16_28AD",        # 10, 16
        "Function_17_28C2",        # 11, 17
        "Function_18_292C",        # 12, 18
        "Function_19_2A41",        # 13, 19
        "Function_20_2AC8",        # 14, 20
    )


    def Function_0_14E(): pass

    label("Function_0_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_15F")
    OP_A3(0x10F0)
    Event(0, 18)
    Jump("loc_179")

    label("loc_15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_179")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_14E end

    def Function_1_19C(): pass

    label("Function_1_19C")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 3)), scpexpr(EXPR_END)), "loc_1B1")
    OP_64(0x0, 0x1)
    OP_71(0x1, 0x4)

    label("loc_1B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x460), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1")
    Call(0, 2)

    label("loc_1C1")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_19C end

    def Function_2_1D3(): pass

    label("Function_2_1D3")

    OP_D2(0x2701C9, 0x2701CE, 0x0)
    OP_D2(0x2900A2, 0x2900A6, 0x1)
    OP_D2(0x2900A3, 0x2900A7, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270130, 0x270140, 0x4)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_22E"),
        (5, "loc_23B"),
        (3, "loc_248"),
        (4, "loc_255"),
        (6, "loc_262"),
        (7, "loc_26F"),
        (8, "loc_27C"),
        (10, "loc_289"),
        (SWITCH_DEFAULT, "loc_296"),
    )


    label("loc_22E")

    OP_D2(0x701D0, 0x701DC, 0x5)
    Jump("loc_296")

    label("loc_23B")

    OP_D2(0x70218, 0x70224, 0x5)
    Jump("loc_296")

    label("loc_248")

    OP_D2(0x701E8, 0x701F4, 0x5)
    Jump("loc_296")

    label("loc_255")

    OP_D2(0x27036E, 0x27037B, 0x5)
    Jump("loc_296")

    label("loc_262")

    OP_D2(0x70230, 0x7023C, 0x5)
    Jump("loc_296")

    label("loc_26F")

    OP_D2(0x70248, 0x70254, 0x5)
    Jump("loc_296")

    label("loc_27C")

    OP_D2(0x270176, 0x270183, 0x5)
    Jump("loc_296")

    label("loc_289")

    OP_D2(0x702B4, 0x702BB, 0x5)
    Jump("loc_296")

    label("loc_296")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2BF"),
        (5, "loc_2CC"),
        (3, "loc_2D9"),
        (4, "loc_2E6"),
        (6, "loc_2F3"),
        (7, "loc_300"),
        (8, "loc_30D"),
        (10, "loc_31A"),
        (SWITCH_DEFAULT, "loc_327"),
    )


    label("loc_2BF")

    OP_D2(0x701D0, 0x701DC, 0x6)
    Jump("loc_327")

    label("loc_2CC")

    OP_D2(0x70218, 0x70224, 0x6)
    Jump("loc_327")

    label("loc_2D9")

    OP_D2(0x701E8, 0x701F4, 0x6)
    Jump("loc_327")

    label("loc_2E6")

    OP_D2(0x27036E, 0x27037B, 0x6)
    Jump("loc_327")

    label("loc_2F3")

    OP_D2(0x70230, 0x7023C, 0x6)
    Jump("loc_327")

    label("loc_300")

    OP_D2(0x70248, 0x70254, 0x6)
    Jump("loc_327")

    label("loc_30D")

    OP_D2(0x270176, 0x270183, 0x6)
    Jump("loc_327")

    label("loc_31A")

    OP_D2(0x702B4, 0x702BB, 0x6)
    Jump("loc_327")

    label("loc_327")

    OP_D2(0x27026B, 0x270275, 0x7)
    OP_D2(0x27026E, 0x270278, 0x8)
    OP_D2(0x26020D, 0x260212, 0x9)
    OP_D2(0x26008F, 0x260094, 0xA)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    Return()

    # Function_2_1D3 end

    def Function_3_364(): pass

    label("Function_3_364")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_364 end

    def Function_4_36D(): pass

    label("Function_4_36D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38E")
    Call(0, 19)
    Call(0, 20)

    label("loc_38E")

    Call(0, 2)
    OP_6D(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x0, 0x0, 0x9)
    Sleep(80)
    OP_43(0x102, 0x0, 0x0, 0xA)
    Sleep(50)
    OP_43(0xF8, 0x0, 0x0, 0xB)
    Sleep(100)
    OP_43(0xF9, 0x0, 0x0, 0xC)

    def lambda_400():
        OP_6B(3960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_400)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1020F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1042F#6P出来了呢……\x02",
    )

    CloseMessageWindow()

    def lambda_45A():
        OP_6D(-1010, 0, 4630, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45A)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        (
            "#1002F#5P好像已经登上\x01",
            "相当的高度了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #3
        0x101,
        "#1004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_508():
        OP_6D(-1540, 0, 34870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_508)

    def lambda_520():
        OP_67(0, 4200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_520)

    def lambda_538():
        OP_6B(2780, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_538)

    def lambda_548():
        OP_6E(382, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_548)

    def lambda_558():
        OP_6C(327000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_558)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    def lambda_572():
        OP_8E(0xFE, 0x6AE, 0x0, 0x636A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_572)
    Sleep(50)

    def lambda_592():
        OP_8E(0xFE, 0x15E, 0x0, 0x636A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_592)
    Sleep(100)

    def lambda_5B2():
        OP_8E(0xFE, 0x7C6, 0x0, 0x5DC0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5B2)
    Sleep(60)

    def lambda_5D2():
        OP_8E(0xFE, 0x26C, 0x0, 0x5DC0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5D2)

    def lambda_5ED():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5ED)

    def lambda_5FD():
        OP_6D(-1140, 0, 29790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5FD)

    def lambda_615():
        OP_67(0, 4780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_615)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x101,
        "#1015F#6P那个……是什么呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A5")

    ChrTalk(    #5
        0x108,
        (
            "#072F#6P……唔。\x02\x03",

            "像是什么东西的终端\x01",
            "不过感觉好奇怪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1")

    label("loc_6A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_707")

    ChrTalk(    #6
        0x106,
        (
            "#555F#6P哼……\x02\x03",

            "像是什么东西的终端……\x01",
            "不过摆在这种地方，不觉得太奇怪了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1")

    label("loc_707")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_764")

    ChrTalk(    #7
        0x104,
        (
            "#033F#6P哟……\x02\x03",

            "#035F像是什么装置的终端，\x01",
            "不过放在这里明显像是陷阱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1")

    label("loc_764")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B5")

    ChrTalk(    #8
        0x109,
        (
            "#1063F#6P唔～\x02\x03",

            "像是什么终端设备，\x01",
            "不过放在这里太可疑了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1")

    label("loc_7B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_807")

    ChrTalk(    #9
        0x103,
        (
            "#023F#6P哎呀……\x02\x03",

            "像是什么设备的终端，\x01",
            "不过感觉太不对劲了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1")

    label("loc_807")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85D")

    ChrTalk(    #10
        0x10B,
        (
            "#212F#6P嗯……\x02\x03",

            "像是什么东西的终端，\x01",
            "不过在这里出现也太奇怪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C1")

    label("loc_85D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C1")

    ChrTalk(    #11
        0x105,
        (
            "#1164F#6P……………………………\x02\x03",

            "#1162F像是什么装置的终端，\x01",
            "不过总觉得很可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(    #12
        0x107,
        (
            "#062F#6P那，看来要\x01",
            "好好调查一下为好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x107,
        "#064F#6P啊……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_93D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B7")

    ChrTalk(    #15
        0x105,
        (
            "#1162F#6P看来有必要\x01",
            "调查一下看看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        "#1164F#6P咦……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_9B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2F")

    ChrTalk(    #18
        0x10B,
        (
            "#212F#6P看来最好是\x01",
            "好好调查一下呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10B,
        "#213F#6P咦……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA9")

    ChrTalk(    #21
        0x103,
        (
            "#022F#6P这似乎要好好\x01",
            "调查一下比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        "#023F#6P咦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_AA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #24
        0x109,
        (
            "#1063F#6P这似乎要好好\x01",
            "调查一下比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1064F#6P哦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA1")

    ChrTalk(    #27
        0x104,
        (
            "#035F#6P呼，这看来需要\x01",
            "好好调查一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x104,
        "#033F#6P哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_BA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1C")

    ChrTalk(    #30
        0x106,
        (
            "#051F#6P嘿，这可有必要\x01",
            "好好地调查一下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1035F#5P不……\x01",
            "还是等一下再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        "#052F#6P什么……\x02",
    )

    CloseMessageWindow()

    label("loc_C1C")

    SetChrChipByIndex(0x8, 7)
    SetChrPos(0x8, 3070, 6620, 33000, 180)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_20(0x3E8)
    OP_21()

    NpcTalk(    #33
        0x8,
        "男人的声音",
        (
            "#6P呼呼，不愧是『漆黑之牙』。\x02\x03",

            "不仅善于隐藏自己的气息，\x01",
            "也很擅长察觉别人的藏匿啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEE")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D2C")

    label("loc_CEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D15")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D2C")

    label("loc_D15")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D2C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D96")

    label("loc_D58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D96")

    label("loc_D7F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D96")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)
    Fade(1000)
    OP_71(0x0, 0x4)
    ClearMapFlags(0x10)
    OP_6D(3030, 4570, 31690, 0)
    OP_67(0, 3680, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(0, 0)
    OP_6E(382, 0)

    def lambda_DF4():
        OP_6D(3030, 7260, 31690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DF4)

    def lambda_E0C():
        OP_67(0, 3400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E0C)
    Sleep(1500)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    def lambda_E68():
        OP_6B(2390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E68)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x6)
    Sleep(500)

    def lambda_E8C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E8C)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#1020F#2P假、假面男……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1042F#5P布卢布兰……是你吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(    #36
        0x8,
        (
            "#231F#5P欢迎，约修亚……\x01",
            "还有艾丝蒂尔·布莱特。\x02\x03",

            "虽然我的公主和好对手没来，\x01",
            "令我无比遗憾……\x02\x03",

            "但还是让我衷心向各位表示欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1002F#2P欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1042F#5P……看来你就是\x01",
            "第一道障碍了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1293")

    label("loc_FC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(    #39
        0x8,
        (
            "#231F#5P约修亚、艾丝蒂尔·布莱特，\x01",
            "还有我高贵的公主也来了啊。\x02\x03",

            "虽然我的好对手不在\x01",
            "让人略感遗憾……\x02\x03",

            "但还是让我衷心向各位表示欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1002F#2P欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#1162F#5P……看来你就是\x01",
            "第一道障碍了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1293")

    label("loc_10B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1192")

    ChrTalk(    #42
        0x8,
        (
            "#231F#5P约修亚、艾丝蒂尔·布莱特，\x01",
            "还有我的好对手也来了啊。\x02\x03",

            "高贵的公主不在\x01",
            "让人略感遗憾……\x02\x03",

            "但还是让我衷心向各位表示欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1002F#2P欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x104,
        (
            "#035F#5P呼，看来你就是\x01",
            "第一道障碍了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1293")

    label("loc_1192")


    ChrTalk(    #45
        0x8,
        (
            "#231F#5P欢迎，约修亚……\x01",
            "还有艾丝蒂尔·布莱特。\x02\x03",

            "而且没想到，连我的公主\x01",
            "和好对手也在一起……\x02\x03",

            "请让我怪盗绅士，以最高的喜悦\x01",
            "欢迎诸位的到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1002F#2P欢、欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x104,
        (
            "#035F#5P呼，相当做作的\x01",
            "登场方式嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#1162F#5P……看来你就是\x01",
            "第一道障碍了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1293")


    ChrTalk(    #49
        0x8,
        (
            "#230F#5P呵呵……\x01",
            "是第一道，也是最后一道障碍。\x02\x03",

            "摆在这里的装置是\x01",
            "锁住通往『中枢塔』上层之门\x01",
            "的终端。\x02\x03",

            "只要这个装置还在运转，\x01",
            "诸位就永远无法到达『环』的所在处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1019F#2P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1035F#5P……布卢布兰。\x02\x03",

            "#1042F在为了此次计划\x01",
            "而来到利贝尔的众位执行者中，\x01",
            "你和我们的因缘应该是最浅的。\x02\x03",

            "既然如此，你听命于教授，\x01",
            "来与我们作战的理由到底是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#230F#5P呵呵……我其实\x01",
            "并不是听命于教授。\x02\x03",

            "如你所知，我们『执行者』没有义务遵从\x01",
            "违背自己意愿的命令。\x02\x03",

            "不要说是『使徒』，\x01",
            "纵使是『盟主』的命令也一样。\x02\x03",

            "#231F呵呵，不过身为教授人偶的你\x01",
            "似乎是有些不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#1043F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1003F#2P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#232F#5P我之所以拘泥于此，理由只有一个…\x02\x03",

            "那就是这里有值得我盗取的\x01",
            "美妙之物。\x02\x03",

            "为了它，我才会守在此地。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16F6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D7")

    ChrTalk(    #56
        0x106,
        (
            "#555F#5P值得盗取的美妙之物……\x01",
            "那究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F3")

    label("loc_15D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1621")

    ChrTalk(    #57
        0x103,
        (
            "#022F#5P值得盗取的美妙之物……\x01",
            "那到底是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F3")

    label("loc_1621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1669")

    ChrTalk(    #58
        0x107,
        (
            "#065F#5P值得盗取的美妙之物……\x01",
            "那、那到底是……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F3")

    label("loc_1669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16AF")

    ChrTalk(    #59
        0x10B,
        (
            "#214F#5P值得盗取的美妙之物……\x01",
            "那到底是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F3")

    label("loc_16AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F3")

    ChrTalk(    #60
        0x109,
        (
            "#1063F#5P值得盗取的美妙之物……\x01",
            "那究竟是什么呀？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F3")

    Jump("loc_17E4")

    label("loc_16F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174C")

    ChrTalk(    #61
        0x105,
        (
            "#1163F#5P值得盗取的美妙之物……\x01",
            "那到底是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E4")

    label("loc_174C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179F")

    ChrTalk(    #62
        0x104,
        (
            "#033F#5P值得盗取的美妙之物……\x01",
            "唔，那到底是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E4")

    label("loc_179F")


    ChrTalk(    #63
        0x105,
        "#1163F#5P值得盗取的美妙之物……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x104,
        "#033F#5P唔，那到底是什么？\x02",
    )

    CloseMessageWindow()

    label("loc_17E4")


    ChrTalk(    #65
        0x8,
        (
            "#231F#5P呵呵……\x01",
            "那就是诸位的『希望』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1020F#2P#3S！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#231F#5P正因面临着逆境，\x01",
            "所谓的『希望』才会散发出美丽的光芒。\x02\x03",

            "为了看到那璀灿绚烂的光辉，\x01",
            "我才会在此等待诸位。\x02\x03",

            "#232F即使这『希望』的光芒如夏日的烟火\x01",
            "一般转瞬即逝……\x02\x03",

            "#234F我也希望见证它的存在！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0xE, 0x7D0)
    Sleep(200)
    Fade(1000)
    OP_72(0x0, 0x4)
    OP_6D(2800, 4330, 23050, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(315000, 0)
    OP_6E(340, 0)
    OP_0D()

    def lambda_195B():
        OP_67(0, 4680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_195B)
    OP_43(0x9, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_43(0xA, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DF")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A1D")

    label("loc_19DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A06")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A1D")

    label("loc_1A06")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A1D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A49")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A87")

    label("loc_1A49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A70")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A87")

    label("loc_1A70")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A87")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0xF8, 5)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_1AC4():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1AC4)
    Sleep(100)
    OP_8C(0xF8, 135, 400)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #68
        0x8,
        (
            "#231F来吧，就让我看看！\x02\x03",

            "名为希望的宝石\x01",
            "在破碎散落时所绽放出的光辉！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE2")

    ChrTalk(    #69
        0x101,
        (
            "#1005F#6P别，别在那里\x01",
            "说些自以为是的话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        (
            "#1167F#5P那我们也向你证明吧……\x02\x03",

            "#1162F由羁绊所产生出的希望\x01",
            "是绝不会破碎散落的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5C")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C88")

    ChrTalk(    #71
        0x101,
        (
            "#1005F#6P少，少在那里\x01",
            "说些自以为是的话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x104,
        (
            "#035F#5P呼，那就让你好好领会一下吧……\x02\x03",

            "#530F只要有爱，希望的灯火\x01",
            "就会永远燃烧下去的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5C")

    label("loc_1C88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D5C")

    ChrTalk(    #73
        0x101,
        (
            "#1005F#6P少，少在那里\x01",
            "说些自以为是的话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x105,
        (
            "#1167F#5P那我们也向你证明吧……\x02\x03",

            "#1162F由羁绊所产生出的希望\x01",
            "是绝不会破碎散落的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x104,
        (
            "#035F#5P只要有爱，希望的灯火\x01",
            "就会永远燃烧下去的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5C")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_1D70():
        OP_6D(190, 980, 24880, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D70)

    def lambda_1D88():
        OP_67(0, 4830, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D88)

    def lambda_1DA0():
        OP_6B(2800, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1DA0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1DBF():
        OP_96(0xFE, 0x384, 0x0, 0x6446, 0x320, 0x36B0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1DBF)

    def lambda_1DDD():
        OP_8E(0xFE, 0xFFFFFE5C, 0x320, 0x5BCC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1DDD)
    Sleep(80)

    def lambda_1DFD():
        OP_8E(0xFE, 0x94C, 0x320, 0x5A82, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1DFD)
    WaitChrThread(0x101, 0x1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0xFF)
    Battle(0x460, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_36D end

    def Function_5_1E35(): pass

    label("Function_5_1E35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    EventBegin(0x0)
    SetChrPos(0x101, 1370, 0, 20520, 0)
    SetChrPos(0x102, -70, 0, 20470, 0)
    SetChrPos(0xF8, 1600, 0, 18950, 0)
    SetChrPos(0xF9, -70, 0, 19040, 0)
    SetChrPos(0x8, 300, 0, 28070, 180)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    OP_6D(-410, 0, 24050, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6B(4000, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #76
        0x8,
        (
            "#236F#2P……唔……不可能………\x02\x03",

            "居然将我的假面……\x01",
            "……打出裂痕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1005F#6P呼……呼……\x01",
            "怎样……体会到了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1035F#6P……破碎散落的\x01",
            "看来是你的傲慢呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2019")

    ChrTalk(    #79
        0x105,
        (
            "#1162F羁绊所产生出的希望有多强大……\x01",
            "你现在明白了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_211B")

    label("loc_2019")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_207A")

    ChrTalk(    #80
        0x104,
        (
            "#030F呼……\x01",
            "让希望之灯火燃烧不断\x01",
            "的爱的伟大，你已经体会到了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_211B")

    label("loc_207A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_211B")

    ChrTalk(    #81
        0x105,
        (
            "#1162F羁绊所产生出的希望有多强大……\x01",
            "你现在明白了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x104,
        (
            "#030F呼……\x01",
            "而让希望之灯火燃烧不断\x01",
            "的“爱”的伟大，你也已经体会到了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211B")


    ChrTalk(    #83
        0x8,
        (
            "#236F#2P……………………………………\x02\x03",

            "#237F好吧……\x01",
            "按照约定，我就撤退好了……\x02\x03",

            "但是，教授的游戏\x01",
            "才刚刚开始而已。\x02\x03",

            "你们最好有所觉悟，\x01",
            "如这次一般的幸运未必还会有第二次。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x8, 8)
    OP_0D()
    Sleep(100)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    def lambda_2204():
        OP_6D(-410, 0, 25050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2204)

    def lambda_221C():
        OP_67(0, 4800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_221C)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(3000)

    ChrTalk(    #84
        0x8,
        (
            "#238F#2P别忘了……\x01",
            "诸位可是将我击退的人……\x02\x03",

            "越过矗立在面前的绝望之壁后，\x01",
            "最终一定能到达美丽的彼岸吧。\x02\x03",

            "……那么，再见吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    OP_82(0x0, 0x2)
    OP_43(0x8, 0x3, 0x0, 0x6)
    Sleep(1500)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #85
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #86
        0x102,
        (
            "#1035F#5P……看来……\x01",
            "真的已经离开了啊。\x02\x03",

            "#1040F他的自尊心很强，\x01",
            "我想应该不会违背约定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1025F#6P是嘛……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E0")

    ChrTalk(    #88
        0x104,
        (
            "#031F#6P哼哼……\x01",
            "虽是敌人，但还是值得赞赏吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_240D")

    ChrTalk(    #89
        0x105,
        "#1168F#6P……这就放心了。\x02",
    )

    CloseMessageWindow()

    label("loc_240D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2449")

    ChrTalk(    #90
        0x10B,
        (
            "#210F#6P呼……\x01",
            "真是个只会添乱的家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FE")

    label("loc_2449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2485")

    ChrTalk(    #91
        0x103,
        (
            "#524F#6P呼……\x01",
            "真是个只会添乱的男人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FE")

    label("loc_2485")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C3")

    ChrTalk(    #92
        0x106,
        (
            "#051F#6P嘿……\x01",
            "真是个只会添麻烦的小子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FE")

    label("loc_24C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FE")

    ChrTalk(    #93
        0x108,
        (
            "#071F#6P哈哈……\x01",
            "真是个只会添乱的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2533")

    ChrTalk(    #94
        0x109,
        (
            "#1068F#6P呀～……\x01",
            "还好撤退了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_2533")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2564")

    ChrTalk(    #95
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "还好撤退了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2564")


    def lambda_256A():
        OP_6D(340, 0, 21000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_256A)

    def lambda_2582():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2582)

    def lambda_259A():
        OP_6B(3760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_259A)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #96
        0x102,
        (
            "#1040F#5P那么\x01",
            "就把那里的终端停止吧。\x02\x03",

            "这样应该能打开\x01",
            "通往上层的门了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #97
        0x101,
        "#1006F#4P嗯……明白！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_266B")
    OP_A2(0x223F)

    label("loc_266B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_267C")
    OP_A2(0x2241)

    label("loc_267C")

    OP_A2(0x2232)
    OP_28(0x9F, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_5_1E35 end

    def Function_6_2688(): pass

    label("Function_6_2688")

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

    # Function_6_2688 end

    def Function_7_26D0(): pass

    label("Function_7_26D0")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, -2900, 15000, 20260, 45)
    ClearChrFlags(0xFE, 0x80)

    def lambda_26F6():
        OP_96(0xFE, 0xFFFFF4AC, 0x320, 0x4F24, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26F6)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)

    def lambda_2738():

        label("loc_2738")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2738")

    QueueWorkItem2(0xFE, 3, lambda_2738)
    Return()

    # Function_7_26D0 end

    def Function_8_2746(): pass

    label("Function_8_2746")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, 5630, 15000, 19970, 315)
    ClearChrFlags(0xFE, 0x80)

    def lambda_276C():
        OP_96(0xFE, 0x15FE, 0x320, 0x4E02, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_276C)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)

    def lambda_27AE():

        label("loc_27AE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_27AE")

    QueueWorkItem2(0xFE, 3, lambda_27AE)
    Return()

    # Function_8_2746 end

    def Function_9_27BC(): pass

    label("Function_9_27BC")

    SetChrPos(0xFE, 870, 0, -25040, 0)
    OP_8E(0xFE, 0x366, 0x0, 0xFFFFB988, 0xBB8, 0x0)
    Return()

    # Function_9_27BC end

    def Function_10_27E2(): pass

    label("Function_10_27E2")

    SetChrPos(0xFE, -390, 0, -25050, 0)
    OP_8E(0xFE, 0xFFFFFE7A, 0x0, 0xFFFFB97E, 0xBB8, 0x0)
    Return()

    # Function_10_27E2 end

    def Function_11_2808(): pass

    label("Function_11_2808")

    SetChrPos(0xFE, 1150, 0, -26400, 0)
    OP_8E(0xFE, 0x47E, 0x0, 0xFFFFB438, 0xBB8, 0x0)
    Return()

    # Function_11_2808 end

    def Function_12_282E(): pass

    label("Function_12_282E")

    SetChrPos(0xFE, -210, 0, -26410, 0)
    OP_8E(0xFE, 0xFFFFFF2E, 0x0, 0xFFFFB42E, 0xBB8, 0x0)
    Return()

    # Function_12_282E end

    def Function_13_2854(): pass

    label("Function_13_2854")

    OP_8E(0xFE, 0x23A, 0x0, 0x1162, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_2854 end

    def Function_14_2883(): pass

    label("Function_14_2883")

    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0x1068, 0xFA0, 0x0)
    Return()

    # Function_14_2883 end

    def Function_15_2898(): pass

    label("Function_15_2898")

    OP_8E(0xFE, 0x3C0, 0x0, 0xBC2, 0xFA0, 0x0)
    Return()

    # Function_15_2898 end

    def Function_16_28AD(): pass

    label("Function_16_28AD")

    OP_8E(0xFE, 0xFFFFFE66, 0x0, 0xB86, 0xFA0, 0x0)
    Return()

    # Function_16_28AD end

    def Function_17_28C2(): pass

    label("Function_17_28C2")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #98
        (
            "\x07\x05解除通向上层区域的隔离壁，\x01",
            "以及传送门的锁定。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5301   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_17_28C2 end

    def Function_18_292C(): pass

    label("Function_18_292C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2943")
    Call(0, 19)
    Call(0, 20)

    label("loc_2943")

    OP_6D(-390, 0, 32400, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 920, 0, 31200, 0)
    SetChrPos(0x102, -200, 0, 31200, 0)
    SetChrPos(0xF8, 1490, 0, 29660, 0)
    SetChrPos(0xF9, -40, 0, 29880, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #99
        (
            "\x07\x05通向上层区域的隔离墙，\x01",
            "以及传送门的锁定已经解除了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x1, 0x4)
    OP_0D()
    Sleep(500)
    OP_64(0x0, 0x1)
    OP_A2(0x2233)
    OP_28(0x9F, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_18_292C end

    def Function_19_2A41(): pass

    label("Function_19_2A41")

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
        (0, "loc_2ABB"),
        (1, "loc_2AC1"),
        (SWITCH_DEFAULT, "loc_2AC7"),
    )


    label("loc_2ABB")

    OP_A2(0x1200)
    Jump("loc_2AC7")

    label("loc_2AC1")

    OP_A2(0x1201)
    Jump("loc_2AC7")

    label("loc_2AC7")

    Return()

    # Function_19_2A41 end

    def Function_20_2AC8(): pass

    label("Function_20_2AC8")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
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

    # Function_20_2AC8 end

    SaveToFile()

Try(main)
