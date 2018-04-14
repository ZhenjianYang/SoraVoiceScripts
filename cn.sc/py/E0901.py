from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0901   ._SN',
        MapName             = 'Event',
        Location            = 'E0901.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '小船',                                 # 9
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
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT07/CH00023 ._CH',             # 01
        'ED6_DT07/CH00053 ._CH',             # 02
        'ED6_DT07/CH00033 ._CH',             # 03
        'ED6_DT07/CH00043 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
        'ED6_DT07/CH00073 ._CH',             # 06
        'ED6_DT27/CH03083 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT07/CH00023P._CP',             # 01
        'ED6_DT07/CH00053P._CP',             # 02
        'ED6_DT07/CH00033P._CP',             # 03
        'ED6_DT07/CH00043P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
        'ED6_DT07/CH00073P._CP',             # 06
        'ED6_DT27/CH03083P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_119",          # 01, 1
        "Function_2_11A",          # 02, 2
        "Function_3_1402",         # 03, 3
        "Function_4_1438",         # 04, 4
        "Function_5_148E",         # 05, 5
        "Function_6_1518",         # 06, 6
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_118")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_118")

    Return()

    # Function_0_10A end

    def Function_1_119(): pass

    label("Function_1_119")

    Return()

    # Function_1_119 end

    def Function_2_11A(): pass

    label("Function_2_11A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131")
    Call(0, 5)
    Call(0, 6)

    label("loc_131")

    FadeToDark(0, 0, -1)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x1, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x0, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_6D(1210, -2990, -360, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(271000, 0)
    OP_6E(370, 0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, -28690, -2850, 20660, 305)
    OP_48()
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x109, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_89(0x101, -27480, -2750, 20350, 125)
    OP_89(0x109, -27880, -2750, 19880, 125)
    OP_89(0xF8, -28750, -2750, 21200, 125)
    OP_89(0xF9, -29110, -2750, 20650, 125)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x109, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x109, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280")
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 1)

    label("loc_280")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298")
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 2)

    label("loc_298")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 3)

    label("loc_2B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C8")
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 4)

    label("loc_2C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E0")
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 5)

    label("loc_2E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8")
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 6)

    label("loc_2F8")

    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)
    LoadEffect(0x1, "map\\\\mp013_00.eff")
    LoadEffect(0x2, "map\\\\mp013_01.eff")
    PlayEffect(0x1, 0x1, 0x8, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x8, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x1CC, 0x0, 0x64)
    OP_22(0xDA, 0x1, 0x4B)
    Sleep(2000)

    def lambda_3B6():
        OP_8F(0xFE, 0x0, 0xFFFFF4DE, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3B6)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_3DB():
        OP_6B(3200, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DB)
    WaitChrThread(0x8, 0x0)
    OP_44(0x101, 0x0)
    Fade(1000)
    OP_6D(330, -2830, -510, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(180000, 0)
    OP_6E(229, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    OP_89(0x101, 1050, -2750, -300, 125)
    OP_89(0x109, 620, -2750, -850, 125)
    OP_89(0xF8, -50, -2750, 450, 125)
    OP_89(0xF9, -500, -2750, 0, 125)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#1003F#6P呼……好安静。\x02\x03",

            "#1002F差不多快能\x01",
            "看见对岸了吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D4():
        OP_67(0, 6500, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D4)

    def lambda_4EC():
        OP_6B(3050, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_545")

    ChrTalk(    #1
        0x108,
        (
            "#074F#4P嗯……\x01",
            "方向应该是对的。\x02\x03",

            "#070F没必要那么着急吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58D")

    ChrTalk(    #2
        0x106,
        (
            "#053F#4P方向应该是对的。\x02\x03",

            "#050F别着急，继续前进。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_58D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DA")

    ChrTalk(    #3
        0x103,
        (
            "#026F#4P方向应该是对的哦。\x02\x03",

            "#020F别着急，\x01",
            "继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_5DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62F")

    ChrTalk(    #4
        0x104,
        (
            "#035F#4P根据地图，\x01",
            "方向应该没问题。\x02\x03",

            "#030F别着急，继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_62F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_675")

    ChrTalk(    #5
        0x105,
        (
            "#542F#4P方向应该是对的。\x02\x03",

            "继续前进的话就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_675")

    Sleep(100)
    SetChrSubChip(0x109, 2)
    Sleep(400)

    ChrTalk(    #6
        0x109,
        (
            "#1062F#6P嗯～话说回来，\x01",
            "今晚的月色可真美啊。\x02\x03",

            "#1061F在这种夜晚，\x01",
            "本该带着女朋友来\x01",
            "约会的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(400)

    ChrTalk(    #7
        0x101,
        (
            "#1007F#6P又说这么悠哉的话……\x02\x03",

            "#1008F不过想不到\x01",
            "凯文先生你有女朋友啊？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x109, 1)
    Sleep(400)

    ChrTalk(    #8
        0x109,
        (
            "#1071F#5P哼，我在大陆各地的城市里\x01",
            "可都有一位候补恋人哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1028F#6P候补恋人也就等于\x01",
            "没有哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1068F#5P啊唔……\x01",
            "再让我多吹嘘一下嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_806")

    ChrTalk(    #11
        0x105,
        "#045F#4P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82A")

    ChrTalk(    #12
        0x107,
        "#061F#4P嘻嘻……\x02",
    )

    CloseMessageWindow()

    label("loc_82A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_850")

    ChrTalk(    #13
        0x103,
        "#027F#4P哎呀呀……\x02",
    )

    CloseMessageWindow()

    label("loc_850")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_885")

    ChrTalk(    #14
        0x104,
        (
            "#035F#4P呵呵，你的\x01",
            "修行还不够啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_885")


    ChrTalk(    #15
        0x101,
        (
            "#1015F#6P……不过凯文先生你\x01",
            "为什么是一个人单独行动呢？\x02\x03",

            "『星杯骑士团』\x01",
            "真有这么欠缺人手吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1067F#5P总之这次是因为有\x01",
            "各种各样的原因……\x02\x03",

            "#1065F于是最后就派遣\x01",
            "我一个人来了……\x02\x03",

            "#1060F视情况需要，\x01",
            "其他人也有可能来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1004F#6P原来如此……\x02\x03",

            "#1015F嗯，你以前说过\x01",
            "『星杯骑士团』的工作\x01",
            "是回收古代遗物对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1060F#5P确切地说是调查、管理、回收。\x02\x03",

            "其中回收的对象\x01",
            "主要是个人所持有的古代遗物。\x02\x03",

            "#1065F因为教会严格禁止\x01",
            "个人随意地持有\x01",
            "能够运作的古代遗物。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A97")

    ChrTalk(    #19
        0x107,
        (
            "#064F#4P请问请问，为什么\x01",
            "必须要进行管制呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC5")

    label("loc_A97")


    ChrTalk(    #20
        0x101,
        (
            "#1004F#6P不过，为什么\x01",
            "必须要进行管制呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC5")


    ChrTalk(    #21
        0x109,
        (
            "#1063F#5P古代遗物的种类\x01",
            "虽然是五花八门……\x02\x03",

            "但却没有人知道\x01",
            "它们的运作原理如何。\x02\x03",

            "#1065F因此，依使用方式的不同，\x01",
            "也有可能发挥出惊人的能量。\x02\x03",

            "#1067F那种东西如果让个人持有的话，\x01",
            "你觉得会发生什么样的情况？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCA")

    ChrTalk(    #22
        0x107,
        (
            "#063F#4P啊……\x01",
            "到底会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF4")

    label("loc_BCA")


    ChrTalk(    #23
        0x101,
        (
            "#1015F#6P嗯、嗯……\x01",
            "到底会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF4")


    ChrTalk(    #24
        0x109,
        (
            "#1063F#5P他们大多会被迷惑住。\x02\x03",

            "因无法抵抗这种力量的诱惑\x01",
            "而做出不正当的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C70")

    ChrTalk(    #25
        0x107,
        "#065F#4P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    label("loc_C70")


    ChrTalk(    #26
        0x101,
        "#1002F#6P这、这是真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1065F#5P很遗憾，历史就是\x01",
            "这么证明给我们看的……\x02\x03",

            "#1063F艾丝蒂尔你们也\x01",
            "知道戴尔蒙市长的事吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D82")

    ChrTalk(    #28
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#049F#4P的确，那时候的市长\x01",
            "让人感觉十分地残忍。\x02\x03",

            "与其说是被操纵了，倒不如说\x01",
            "是已经无法控制自己了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFF")

    label("loc_D82")


    ChrTalk(    #30
        0x101,
        (
            "#1020F#6P啊……\x02\x03",

            "#1007F的确，那时候的市长\x01",
            "让人感觉十分地残忍。\x02\x03",

            "与被操纵了的空贼头目不同，\x01",
            "好像是自己无法控制自己了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFF")


    ChrTalk(    #31
        0x109,
        (
            "#1065F#5P人一旦拥有了绝对的力量\x01",
            "就会产生一种扭曲的自信，\x01",
            "使之丧失自制能力……\x02\x03",

            "#1060F因此，『星杯骑士团』的使命\x01",
            "就是为了防止这样的事情再次发生。\x02\x03",

            "#1068F当然，不能完全说得这么好听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1004F#6P是、是吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101C")

    ChrTalk(    #33
        0x104,
        (
            "#035F#4P呵，教会也有着\x01",
            "各种不为人知的隐情呢。\x02\x03",

            "#030F好像有时候\x01",
            "也会允许个人\x01",
            "持有古代遗物吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F74")

    ChrTalk(    #34
        0x103,
        "#027F#4P……………………………\x02",
    )

    CloseMessageWindow()

    label("loc_F74")


    ChrTalk(    #35
        0x109,
        (
            "#1064F#5P……你知道的还真多。\x02\x03",

            "#1071F不过对于这件事\x01",
            "我无可奉告。\x02\x03",

            "因为我有保守秘密的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x104,
        "#035F#4P呵呵，这也是当然的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1019F#6P多少有点可疑啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_101C")


    ChrTalk(    #38
        0x109,
        (
            "#1062F#5P不过游击士协会\x01",
            "也有不可公开的事情吧？\x02\x03",

            "这都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1007F#6P嗯、嗯……\x01",
            "这一点的确无法否认。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108E")


    def lambda_1094():
        OP_6E(315, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1094)
    OP_43(0x8, 0x2, 0x0, 0x4)
    Sleep(1000)
    StopSound(0x3E8, 0xEA60, 0x1F40)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    OP_20(0x7D0)
    OP_82(0x80, 0x2)
    OP_82(0x81, 0x2)
    OP_82(0x82, 0x2)
    Sleep(100)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(    #40
        0x101,
        "#1005F#6P啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A0")

    ChrTalk(    #41
        0x103,
        (
            "#022F#4P看来我们已经接近\x01",
            "敌人的据点了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_11A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E0")

    ChrTalk(    #42
        0x106,
        (
            "#057F#4P看来我们已经接近\x01",
            "敌人的据点了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_11E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1220")

    ChrTalk(    #43
        0x108,
        (
            "#072F#4P看来我们已经接近\x01",
            "敌人的据点了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_1220")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1264")

    ChrTalk(    #44
        0x107,
        (
            "#065F#4P一接近『结社』的据点\x01",
            "就会产生浓雾……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_1264")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A5")

    ChrTalk(    #45
        0x105,
        (
            "#042F#4P看来我们已经接近\x01",
            "『结社』的据点了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A5")

    Sleep(500)
    OP_21()
    OP_1D(0x7D)
    Sleep(1000)

    ChrTalk(    #46
        0x109,
        (
            "#1063F#5P那么，现在看来\x01",
            "只能一直前进了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1002F#6P嗯……\x02\x03",

            "敌人也有可能设下埋伏，\x01",
            "提高警觉小心前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_43(0x8, 0x3, 0x0, 0x3)
    StopSound(0x3E8, 0x7530, 0x7D0)

    def lambda_1341():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1341)
    Sleep(500)

    def lambda_135C():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_135C)
    Sleep(400)

    def lambda_1377():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1377)
    Sleep(300)

    def lambda_1392():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1392)
    Sleep(200)

    def lambda_13AD():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13AD)
    Sleep(100)

    def lambda_13C8():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13C8)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x2)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_11A end

    def Function_3_1402(): pass

    label("Function_3_1402")

    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x15E)
    OP_73(0x0)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)
    Return()

    # Function_3_1402 end

    def Function_4_1438(): pass

    label("Function_4_1438")

    OP_22(0x1C3, 0x1, 0x64)
    Sleep(3000)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_23(0x1C3)
    Return()

    # Function_4_1438 end

    def Function_5_148E(): pass

    label("Function_5_148E")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_150B"),
        (1, "loc_1511"),
        (SWITCH_DEFAULT, "loc_1517"),
    )


    label("loc_150B")

    OP_A2(0x1200)
    Jump("loc_1517")

    label("loc_1511")

    OP_A2(0x1201)
    Jump("loc_1517")

    label("loc_1517")

    Return()

    # Function_5_148E end

    def Function_6_1518(): pass

    label("Function_6_1518")

    ClearMapFlags(0x1)
    OP_6D(15460, -2990, 171130, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_6_1518 end

    SaveToFile()

Try(main)
