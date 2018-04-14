from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2610   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        '基尔巴特',                             # 9
        '莉秋儿',                               # 10
        '小丑肯帕雷拉',                         # 11
        '基库',                                 # 12
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -80200,
        TriggerZ            = 250,
        TriggerY            = 31450,
        TriggerRange        = 1000,
        ActorX              = -80240,
        ActorZ              = 250,
        ActorY              = 32100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_14E",          # 00, 0
        "Function_1_173",          # 01, 1
        "Function_2_1DA",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_2FA",          # 04, 4
        "Function_5_14FC",         # 05, 5
        "Function_6_25C7",         # 06, 6
        "Function_7_2604",         # 07, 7
        "Function_8_2685",         # 08, 8
        "Function_9_26CD",         # 09, 9
        "Function_10_2715",        # 0A, 10
        "Function_11_275D",        # 0B, 11
        "Function_12_27A5",        # 0C, 12
        "Function_13_27FD",        # 0D, 13
        "Function_14_2846",        # 0E, 14
        "Function_15_28A6",        # 0F, 15
        "Function_16_2924",        # 10, 16
        "Function_17_293A",        # 11, 17
        "Function_18_2982",        # 12, 18
    )


    def Function_0_14E(): pass

    label("Function_0_14E")

    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_172")
    Event(0, 3)
    Jump("loc_172")

    label("loc_172")

    Return()

    # Function_0_14E end

    def Function_1_173(): pass

    label("Function_1_173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 1)), scpexpr(EXPR_END)), "loc_183")
    OP_10(0x5, 0x0)
    OP_10(0x17, 0x1)
    Jump("loc_189")

    label("loc_183")

    OP_10(0x5, 0x1)
    OP_10(0x17, 0x0)

    label("loc_189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B")
    OP_6F(0xB, 0)
    Jump("loc_1A2")

    label("loc_19B")

    OP_6F(0xB, 60)

    label("loc_1A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xF40), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D9")

    label("loc_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1C4")
    Jump("loc_1D9")

    label("loc_1C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_1D9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_1D9")

    Return()

    # Function_1_173 end

    def Function_2_1DA(): pass

    label("Function_2_1DA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_249")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1341)
    Jump("loc_2AF")

    label("loc_249")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF5\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_2AF")

    Jump("loc_2E3")

    label("loc_2B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1DA end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_2F1 end

    def Function_4_2FA(): pass

    label("Function_4_2FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_D2(0x2601B4, 0x2601B9, 0x0)
    OP_D2(0x260068, 0x26006D, 0x1)
    OP_D2(0x704AA, 0x704AE, 0x2)
    OP_D2(0x2601BA, 0x2601BF, 0x3)
    OP_D2(0x70113, 0x70117, 0x4)
    OP_D2(0x2701DA, 0x2701DF, 0x5)
    OP_D2(0x70180, 0x70184, 0x6)
    OP_D2(0x270110, 0x270120, 0x7)
    OP_D2(0x270111, 0x270121, 0x8)
    OP_D2(0x270130, 0x270140, 0x9)
    OP_D2(0x270131, 0x270141, 0xA)
    OP_D2(0x70326, 0x7032D, 0xB)
    OP_D2(0x70327, 0x7032E, 0xC)
    OP_D2(0x70318, 0x7031F, 0xD)
    OP_D2(0x70319, 0x70320, 0xE)
    OP_D2(0x2701F8, 0x2701FD, 0xF)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xA, 5)
    SetChrChipByIndex(0xB, 6)
    OP_6D(510, 0, 2770, 0)
    OP_67(0, 6890, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(311, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x8)
    Sleep(80)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(200)
    OP_43(0x10A, 0x1, 0x0, 0xA)
    Sleep(70)
    OP_43(0x10E, 0x1, 0x0, 0xB)
    OP_6D(520, 0, 6900, 1500)
    SetChrPos(0x8, 30, 0, 16059, 180)

    NpcTalk(    #3
        0x8,
        "青年的声音",
        "#4P果然是你们啊……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x8, -190, 2000, 25350, 180)
    SetChrPos(0x9, 360, 2000, 25240, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-50, 2000, 24730, 2500)
    OP_1D(0x29)
    Sleep(1000)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x10A, 11)
    SetChrChipByIndex(0x10E, 13)

    def lambda_563():
        OP_6D(50, 1800, 20880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_563)

    def lambda_57B():
        OP_67(0, 3650, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_57B)

    def lambda_593():
        OP_6B(2550, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_593)

    def lambda_5A3():
        OP_6E(405, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5A3)

    def lambda_5B3():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFFCE, 0x47AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B3)
    Sleep(80)

    def lambda_5D3():
        OP_8E(0xFE, 0x3A2, 0xFFFFFFCE, 0x4736, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D3)
    Sleep(70)

    def lambda_5F3():
        OP_8E(0xFE, 0xFFFFFBE6, 0x0, 0x40CE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5F3)
    Sleep(80)

    def lambda_613():
        OP_8E(0xFE, 0x24E, 0x0, 0x4042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_613)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #4
        0x101,
        "#1005F#6P基尔巴特……是你！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1221F哟，不要\x01",
            "再靠近了嘛。\x02\x03",

            "如果不想\x01",
            "伤害这位小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #6
        0x9,
        "#2P不、不要……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1020F#6P（啊……！\x01",
            "科洛丝的学妹……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1042F#4P（是击剑部\x01",
            "的女孩吧……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#1222F你们每次\x01",
            "都来妨碍我……\x02\x03",

            "#1225F但是！\x01",
            "这次，你们休想得逞！\x02\x03",

            "我要用这女孩作为礼物，\x01",
            "提高在『结社』中的地位！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1004F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1226F看来『噬身之蛇』\x01",
            "是个超乎想象的巨大组织。\x02\x03",

            "现在来到利贝尔的\x01",
            "也只是极少的一部分……\x02\x03",

            "恐怕其影响力\x01",
            "应该波及到大陆全境了。\x02\x03",

            "#1221F呵呵，一定\x01",
            "有出人头地的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        (
            "#814F#4P原来如此……\x01",
            "还有这种想法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1007F#6P怎么说呢……\x01",
            "这种向上爬的志向也过于可怜点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#1225F住口！\x02\x03",

            "说到底，利贝尔这种\x01",
            "小国岂能容得下我！\x02\x03",

            "#1226F『噬身之蛇』\x01",
            "才是我应该活跃的舞台！\x02\x03",

            "#1221F岂能容你们来捣乱！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1007F#6P嗯，本来想\x01",
            "让你加油努力……\x02\x03",

            "#1019F不过，我觉得就算你绑架了那孩子\x01",
            "好像对你并不能有多大的帮助？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#1226F哼，看来你们\x01",
            "好像完全不知道……\x02\x03",

            "#1221F这女孩是隐姓埋名的\x01",
            "利贝尔王室的公主！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #17
        0x9,
        (
            "#2P不、不是告诉你\x01",
            "不是了吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#1221F哼……\x01",
            "少来这套了。\x02\x03",

            "#1226F据我打听\x01",
            "那位公主似乎经常使用细剑。\x02\x03",

            "而现在，击剑部的\x01",
            "女学生只有你一个……\x02\x03",

            "#1225F那么除了你还有谁！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0x9)
    Sleep(500)

    ChrTalk(    #19
        0x9,
        "#2P这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1019F#6P唉……怎么说你呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#1035F#4P也太会钻牛角尖了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#1224F你、你们这是什么意思……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F#6P我说啊……\x02\x03",

            "#1019F你啊，还记不记得以前\x01",
            "在巴伦诺灯塔被捕的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#1225F怎、怎么可能忘记！？\x02\x03",

            "一想到当时的事\x01",
            "现在还一肚子火呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1048F#4P那和我们在一起的\x01",
            "女学生你还记得吗？\x02\x03",

            "多少也算是见过一面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#1221F……啊啊，是科洛丝吧。\x02\x03",

            "这么说来关起来的学生中\x01",
            "好像没看到她……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #27
        0x8,
        "#1224F#3S啊啊。\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1006F#6P就是这么回事。\x02\x03",

            "在灯塔科洛丝\x01",
            "也用了细剑吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1224F这么说来……\x02\x03",

            "#1225F……不、不对！\x01",
            "不可能有这种蠢事！\x02\x03",

            "事到如今\x01",
            "我所做的一切都是白费吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10A,
        (
            "#819F#4P嗯……\x01",
            "开始逃避现实了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10E,
        "#843F#4P……真可怜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#1227F住、住口！\x02\x03",

            "#1225F无论如何，只要手上有人质\x01",
            "我就是有利的！\x02\x03",

            "如果你们不想她受到伤害\x01",
            "就全体人员立即放下武器！\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        "#2P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1019F#6P（……真想把他\x01",
            "  一脚踢飞。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1043F#4P（看看有什么机会……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#1221F干、干什么！\x02\x03",

            "如果不照我说的做\x01",
            "我就在她这可爱的脸蛋上──\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    OP_22(0x197, 0x0, 0x64)
    OP_20(0x7D0)
    OP_22(0x8C, 0x0, 0x64)
    SetChrPos(0xB, -410, 5000, 5000, 0)
    SetChrFlags(0xB, 0x40)
    OP_7D(0x0, 0xB, 0x32, 0x1F4)
    ClearChrFlags(0xB, 0x80)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 6)
    OP_43(0xB, 0x1, 0x0, 0x10)

    def lambda_FDB():
        OP_6D(90, 3500, 13500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FDB)

    def lambda_FF3():
        OP_6E(343, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FF3)
    WaitChrThread(0x101, 0x2)
    OP_1D(0x2C)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1013():
        OP_6D(430, 2000, 25000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1013)

    def lambda_102B():
        OP_6B(2300, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_102B)
    OP_8F(0xB, 0xC8, 0x960, 0x6270, 0x6590, 0x0)
    OP_7D(0x1, 0xB, 0x0, 0x0)
    PlayEffect(0x1, 0x0, 0x8, 0, 1600, 700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)

    ChrTalk(    #37 op#A op#5
        0x8,
        "#1227F#20A呜！？\x05\x02",
    )


    ChrTalk(    #38 op#A op#5
        0x9,
        "#2P#20A呀！？\x05\x02",
    )

    OP_44(0x101, 0x0)
    OP_44(0x102, 0x2)
    OP_44(0x10A, 0x2)
    OP_44(0x10E, 0x2)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)
    OP_8C(0x10A, 0, 0)
    OP_8C(0x10E, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x9, 0, 0)
    SetChrChipByIndex(0xB, 1)
    OP_44(0xB, 0x1)

    def lambda_1110():

        label("loc_1110")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1110")

    QueueWorkItem2(0xB, 1, lambda_1110)

    def lambda_1123():
        OP_8F(0xB, 0x1F4, 0x15E0, 0x6C98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1123)

    def lambda_113E():
        OP_8C(0xFE, 225, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_113E)

    def lambda_114C():
        OP_8F(0xFE, 0x3C0, 0x7D0, 0x6040, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_114C)
    OP_43(0x8, 0x0, 0x0, 0xD)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_11DE():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11DE)

    def lambda_11EC():
        OP_67(0, 3490, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11EC)

    def lambda_1204():
        OP_6B(2610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1204)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #39
        0x101,
        "#1005F#5P莉秋儿，这边！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #40
        0x9,
        "#5P是、是！\x02",
    )

    CloseMessageWindow()

    def lambda_1258():
        OP_6D(-340, 2000, 22200, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1258)

    def lambda_1270():
        OP_67(0, 5880, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1270)

    def lambda_1288():
        OP_6B(2640, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1288)

    def lambda_1298():
        OP_6E(360, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1298)
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0xB, 0x2, 0x0, 0xE)
    OP_43(0x9, 0x1, 0x0, 0xC)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #41
        0xB,
        "#310F#6P啾！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x12C, 1500, 0x28, 0x2B, 0xC8, 0x0)
    Sleep(200)
    SetChrSubChip(0x8, 1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #42
        0x8,
        "#1224F#8P什、什、什…么…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1018F#5P基库……\x01",
            "你怎么在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1044F#2P难不成\x01",
            "是科洛丝要你来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        "#311F#6P啾～～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10E,
        "#841F#2P哈哈，真是佩服。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        "#811F好厉害！太厉害了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#1224F#8P不、不可能……\x02\x03",

            "#1227F这不可能啊啊啊啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        "#1035F#2P好了，那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1028F#5P开始惩罚吧⊙\x02",
    )

    CloseMessageWindow()

    def lambda_142C():
        OP_6D(370, 2000, 24910, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_142C)

    def lambda_1444():
        OP_6B(2000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1444)

    def lambda_1454():
        OP_8F(0xFE, 0xFFFFFDBC, 0x6D6, 0x640A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1454)
    Sleep(30)

    def lambda_1474():
        OP_8F(0xFE, 0x2A8, 0x6D6, 0x63D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1474)

    def lambda_148F():
        OP_8F(0xFE, 0xFFFFFDB2, 0x2EE, 0x646E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_148F)
    Sleep(30)

    def lambda_14AF():
        OP_8F(0xFE, 0x348, 0x2EE, 0x643C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_14AF)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0xF40, 0x30000E, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_14F6"),
        (SWITCH_DEFAULT, "loc_14FB"),
    )


    label("loc_14F6")

    OP_B4(0x0)
    Jump("loc_14FB")

    label("loc_14FB")

    Return()

    # Function_4_2FA end

    def Function_5_14FC(): pass

    label("Function_5_14FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_D2(0x2601B4, 0x2601B9, 0x0)
    OP_D2(0x260068, 0x26006D, 0x1)
    OP_D2(0x704AA, 0x704AE, 0x2)
    OP_D2(0x2601BA, 0x2601BF, 0x3)
    OP_D2(0x70113, 0x70117, 0x4)
    OP_D2(0x2701DA, 0x2701DF, 0x5)
    OP_D2(0x70180, 0x70184, 0x6)
    OP_D2(0x270110, 0x270120, 0x7)
    OP_D2(0x270111, 0x270121, 0x8)
    OP_D2(0x270130, 0x270140, 0x9)
    OP_D2(0x270131, 0x270141, 0xA)
    OP_D2(0x70326, 0x7032D, 0xB)
    OP_D2(0x70327, 0x7032E, 0xC)
    OP_D2(0x70318, 0x7031F, 0xD)
    OP_D2(0x70319, 0x70320, 0xE)
    OP_D2(0x26021E, 0x260223, 0x10)
    OP_D2(0x26021F, 0x260224, 0x11)
    OP_D2(0x2600C1, 0x2600C6, 0x12)
    OP_D2(0x2600D2, 0x2600D7, 0x13)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -680, 1000, 22880, 0)
    SetChrPos(0x102, 620, 1000, 22880, 0)
    SetChrPos(0x10A, -750, 0, 21730, 0)
    SetChrPos(0x10E, 650, 0, 21730, 0)
    SetChrPos(0x8, 240, 2000, 27150, 180)
    SetChrPos(0x9, 130, 0, 16730, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x10A, 11)
    SetChrChipByIndex(0x10E, 13)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3900, 5400, 25090, 90)
    SetChrChipByIndex(0xB, 2)
    SetChrSubChip(0xB, 0)
    OP_6D(270, 2000, 24030, 0)
    OP_67(0, 3150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(32000, 0)
    OP_6E(337, 0)
    LoadEffect(0x0, "map\\mp055_00.eff")
    LoadEffect(0x1, "map\\mp093_00.eff")
    LoadEffect(0x2, "map\\mp093_01.eff")
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x8,
        "#1224F#5P……呜呜……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 17)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0x218, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x6, 0x5DC)
    OP_43(0x8, 0x1, 0x0, 0x6)

    ChrTalk(    #52
        0x8,
        (
            "#1227F#5P求、求求你们……\x01",
            "饶我一条小命吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007F#6P真受不了……\x01",
            "不至于突然这么卑躬屈膝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#819F#6P啊哈哈，到最后感觉\x01",
            "好像在欺负弱者一样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10E,
        (
            "#843F#4P这是自作自受。\x02\x03",

            "#842F那么根据协会条约，\x01",
            "在此逮捕你──\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #56
        "\x07\x05那可不妙啊。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_44(0x8, 0x1)
    SetChrSubChip(0x8, 7)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xA, 190, 2000, 25290, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_190E():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_190E)

    def lambda_191E():
        OP_6D(870, 2000, 26560, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_191E)

    def lambda_1936():
        OP_67(0, 4830, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1936)

    def lambda_194E():
        OP_6E(391, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_194E)
    PlayEffect(0x0, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x7)
    WaitChrThread(0x101, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1A19():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A19)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_43(0xA, 0x3, 0x0, 0x11)
    SetChrSubChip(0x8, 8)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #57
        0x101,
        "#1005F#5P你、你是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        "#815F#5P废坑时出现的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1042F#5P……肯帕雷拉吗。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 19)
    SetChrSubChip(0xA, 0)
    OP_99(0xA, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #60
        0xA,
        "#853F#5P哈哈哈，诸位好。\x02",
    )

    CloseMessageWindow()
    OP_99(0xA, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    Sleep(500)

    ChrTalk(    #61
        0xA,
        (
            "#854F#5P我从你们突入学院开始\x01",
            "就一直在旁观战……\x02\x03",

            "#851F呀～这实在是太有趣了！\x02\x03",

            "没想到在这个时机\x01",
            "临时演员突然登场啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#310F#6P啾？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#1221F#5P肯、肯帕雷拉大人……\x01",
            "您是来救我的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_1BD8():
        OP_6D(920, 2000, 27360, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BD8)
    Sleep(500)
    OP_63(0xA)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #64
        0xA,
        (
            "#850F#6P……我说，基尔巴特。\x02\x03",

            "我可不记得有命令你\x01",
            "掳走王室的公主啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "#1224F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#853F#6P当然，根据现场状况\x01",
            "而随机应变倒也不错。\x02\x03",

            "我也并不打算\x01",
            "计较这种小事。\x02\x03",

            "#854F……只是…\x01",
            "如果失败的话，就毫无意义了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #67
        0x8,
        "#1224F#5P呜……呜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x8, 0x20)
    OP_8F(0x8, 0x64, 0x7D0, 0x6C34, 0x3E8, 0x0)
    ClearChrFlags(0x8, 0x20)
    Sleep(300)
    Fade(250)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 18)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_99(0xA, 0x1, 0x2, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    Fade(500)
    OP_6D(-90, 2500, 26730, 0)
    OP_67(0, 3870, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(1000, 0)
    OP_6E(391, 0)
    SetChrPos(0x101, -1090, 0, 18620, 0)
    SetChrPos(0x102, 180, -50, 18470, 0)
    SetChrPos(0x10A, -1290, 0, 16900, 0)
    SetChrPos(0x10E, -40, 0, 16760, 0)
    SetChrPos(0x9, -220, 0, 15100, 0)
    SetChrPos(0x8, -500, 2000, 26910, 180)
    SetChrPos(0xA, 0, 2000, 24750, 180)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_22(0x87, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 0)

    def lambda_1E8E():

        label("loc_1E8E")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1E8E")

    QueueWorkItem2(0x8, 3, lambda_1E8E)
    OP_8F(0x8, 0xFFFFFE0C, 0x834, 0x68B0, 0x1F40, 0x0)
    Sleep(500)

    ChrTalk(    #68
        0x8,
        "#1227F#5P呜啊啊啊……！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #69
        0x101,
        "#1020F#5P怎、怎么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#1035F#5P炎之舌……\x02\x03",

            "#1042F和露茜奥拉使用的一样\x01",
            "是一种攻击性幻术吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#851F#5P哈哈哈，我可\x01",
            "没她用得那么好。\x02\x03",

            "#854F不过，这种水平的话还是可以应付的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x1)

    def lambda_1FA6():
        OP_6D(-90, 3500, 26730, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FA6)
    OP_82(0x1, 0x0)
    OP_22(0x87, 0x0, 0x64)
    PlayEffect(0x2, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)

    def lambda_1FFB():

        label("loc_1FFB")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1FFB")

    QueueWorkItem2(0x8, 3, lambda_1FFB)
    OP_8F(0x8, 0xFFFFFE0C, 0xC80, 0x68B0, 0x1F40, 0x0)
    Sleep(500)

    ChrTalk(    #72
        0x8,
        "#1227F#5P呜哇啊啊啊啊啊啊！！！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #73
        0xA,
        (
            "#851F#5P不过，基尔巴特小丑一样的举动\x01",
            "也挺让人开心的。\x02\x03",

            "这次就免你一死，\x01",
            "稍微惩罚一下就算了吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x2, 0x2)
    OP_23(0x87)

    def lambda_20D1():
        OP_6D(0, 2000, 26730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20D1)
    OP_44(0x8, 0x3)
    OP_8F(0x8, 0xFFFFFE0C, 0x7D0, 0x68B0, 0x1F40, 0x0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x8, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #74
        0x8,
        "#5P……呜呜呜………\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#1005F#5P慢、慢着！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10A,
        "#815F#5P又、又想逃跑吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "#851F#5P啊哈哈，这次嘛，\x01",
            "我就向大家赔个不是吧。\x02\x03",

            "我发誓今后，『结社』\x01",
            "绝不会再对这个学院出手。\x02\x03",

            "#854F那么各位──打扰了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x99, 0x0, 0x64)

    def lambda_223B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_223B)

    def lambda_224D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_224D)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_43(0xA, 0x3, 0x0, 0x11)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    Fade(1000)
    OP_20(0x7D0)
    OP_6D(170, 2000, 25490, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(45000, 0)
    OP_6E(353, 0)
    SetChrPos(0x101, -730, 0, 18400, 0)
    SetChrPos(0x102, 790, 0, 18470, 0)
    SetChrPos(0x10A, -1130, 0, 16880, 0)
    SetChrPos(0x10E, 530, -50, 16790, 0)
    SetChrPos(0x9, -300, 0, 15300, 0)
    OP_0D()
    OP_43(0xB, 0x2, 0x0, 0xF)

    def lambda_2321():
        OP_6D(1020, -50, 18700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2321)

    def lambda_2339():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2339)

    def lambda_2351():
        OP_6B(2310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2351)
    Sleep(2500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    Sleep(500)

    ChrTalk(    #78
        0x101,
        "#1003F#6P又、又来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        "#1316F#6P被他逃跑了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10E,
        (
            "#844F#4P『小丑』肯帕雷拉……\x01",
            "真是个深不可测的少年啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1043F#2P嗯嗯……是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_2414():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2414)
    Sleep(100)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #82
        0x102,
        (
            "#1040F#5P不过，他的承诺\x01",
            "在某种程度上应该可信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10E,
        "#845F#4P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1007F#5P唉，虽然不算圆满……\x02\x03",

            "#1025F但也\x01",
            "算是告一段落了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24BA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24BA)
    Sleep(100)
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(    #85
        0x10A,
        "#816F#6P嗯，这样也好。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x2)

    ChrTalk(    #86
        0xB,
        "#311F#6P啾⊙\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x05就这样，强化猎兵\x01",
            "侵占学院事件落下了帷幕。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x05王国军部队到达时\x01",
            "学院内外的猎兵们\x01",
            "已全数撤退……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05经过学院长和乔儿等人的努力\x01",
            "学生们的不安也平息了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2500   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_5_14FC end

    def Function_6_25C7(): pass

    label("Function_6_25C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2603")
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_6_25C7")

    label("loc_2603")

    Return()

    # Function_6_25C7 end

    def Function_7_2604(): pass

    label("Function_7_2604")


    def lambda_260A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_260A)
    Sleep(50)

    def lambda_262A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_262A)
    Sleep(200)

    def lambda_264A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_264A)
    Sleep(50)

    def lambda_266A():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_266A)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_7_2604 end

    def Function_8_2685(): pass

    label("Function_8_2685")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -470, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_26AC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26AC)
    OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x19FA, 0x1388, 0x0)
    Return()

    # Function_8_2685 end

    def Function_9_26CD(): pass

    label("Function_9_26CD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 630, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_26F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26F4)
    OP_8E(0xFE, 0x2BC, 0x0, 0x1996, 0x1388, 0x0)
    Return()

    # Function_9_26CD end

    def Function_10_2715(): pass

    label("Function_10_2715")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -470, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_273C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_273C)
    OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x14C8, 0x1388, 0x0)
    Return()

    # Function_10_2715 end

    def Function_11_275D(): pass

    label("Function_11_275D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 630, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2784():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2784)
    OP_8E(0xFE, 0x1D6, 0x0, 0x14B4, 0x1388, 0x0)
    Return()

    # Function_11_275D end

    def Function_12_27A5(): pass

    label("Function_12_27A5")

    OP_8E(0xFE, 0x226, 0x0, 0x5230, 0x1388, 0x0)
    OP_8E(0xFE, 0x88E, 0x0, 0x4C5E, 0x1388, 0x0)
    OP_8E(0xFE, 0x758, 0x0, 0x396C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFFBA, 0x0, 0x396C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_27A5 end

    def Function_13_27FD(): pass

    label("Function_13_27FD")

    OP_8C(0xFE, 180, 0)

    def lambda_280A():
        OP_96(0xFE, 0xFFFFFFA6, 0x7D0, 0x65EA, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_280A)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_13_27FD end

    def Function_14_2846(): pass

    label("Function_14_2846")

    SetChrChipByIndex(0xB, 6)
    OP_97(0xB, 0xFFFFFAB0, 0x6A7C, 0x27100, 0x1770, 0x1)
    SetChrChipByIndex(0xB, 1)
    OP_8C(0xFE, 90, 300)
    OP_8F(0xFE, 0xFFFFF0C4, 0x13EC, 0x6202, 0x3E8, 0x0)
    Fade(250)
    OP_44(0xB, 0x1)
    SetChrPos(0xB, -3900, 5400, 25090, 90)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 2)
    OP_0D()
    Return()

    # Function_14_2846 end

    def Function_15_28A6(): pass

    label("Function_15_28A6")

    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0xB, 1)

    def lambda_28B6():

        label("loc_28B6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_28B6")

    QueueWorkItem2(0xB, 1, lambda_28B6)
    OP_8F(0xFE, 0xFFFFF4AC, 0x1770, 0x6202, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFF830, 0x60E, 0x55E6, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 300)
    Sleep(100)
    Fade(250)
    OP_44(0xB, 0x1)
    SetChrPos(0xB, -2000, 1750, 21990, 135)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 2)
    OP_0D()
    Return()

    # Function_15_28A6 end

    def Function_16_2924(): pass

    label("Function_16_2924")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2939")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_16_2924")

    label("loc_2939")

    Return()

    # Function_16_2924 end

    def Function_17_293A(): pass

    label("Function_17_293A")

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

    # Function_17_293A end

    def Function_18_2982(): pass

    label("Function_18_2982")

    NewScene("ED6_DT21/T2611   ._SN", 120, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2982 end

    SaveToFile()

Try(main)
