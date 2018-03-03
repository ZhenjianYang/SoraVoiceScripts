from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2110   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Mirano',                               # 9
        'Kanone',                               # 10
        'Mayor Norman',                         # 11
        'File 1',                               # 12
        'File 2',                               # 13
        'File 3',                               # 14
        'Letter',                               # 15
        'Target Camera',                        # 16
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
        'ED6_DT07/CH01230 ._CH',             # 00
        'ED6_DT26/CH20797 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01233 ._CH',             # 03
        'ED6_DT26/CH20679 ._CH',             # 04
        'ED6_DT06/CH20021 ._CH',             # 05
        'ED6_DT26/CH20798 ._CH',             # 06
        'ED6_DT26/CH20278 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01230P._CP',             # 00
        'ED6_DT26/CH20797P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01233P._CP',             # 03
        'ED6_DT26/CH20679P._CP',             # 04
        'ED6_DT06/CH20021P._CP',             # 05
        'ED6_DT26/CH20798P._CP',             # 06
        'ED6_DT26/CH20278P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1F6,
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
        Unknown3            = 1835013,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1F6,
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
        Unknown3            = 131079,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1F6,
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
        Unknown3            = 1114117,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1F6,
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
        "Function_0_1EA",          # 00, 0
        "Function_1_24E",          # 01, 1
        "Function_2_27A",          # 02, 2
        "Function_3_290",          # 03, 3
        "Function_4_2B4",          # 04, 4
        "Function_5_2D8",          # 05, 5
        "Function_6_195A",         # 06, 6
        "Function_7_19BB",         # 07, 7
        "Function_8_19FC",         # 08, 8
        "Function_9_1A64",         # 09, 9
        "Function_10_1AAC",        # 0A, 10
        "Function_11_1B14",        # 0B, 11
        "Function_12_1B41",        # 0C, 12
        "Function_13_1BCF",        # 0D, 13
        "Function_14_1C1D",        # 0E, 14
        "Function_15_1C83",        # 0F, 15
        "Function_16_22A6",        # 10, 16
        "Function_17_22FF",        # 11, 17
        "Function_18_2336",        # 12, 18
        "Function_19_2E3A",        # 13, 19
        "Function_20_2EC7",        # 14, 20
        "Function_21_2FC1",        # 15, 21
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_218")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_24D")

    label("loc_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_23A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_24D")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_24D")

    Return()

    # Function_0_1EA end

    def Function_1_24E(): pass

    label("Function_1_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_270")
    OP_A3(0x0)
    OP_B1("T2110_1")
    Jump("loc_279")

    label("loc_270")

    OP_B1("T2110_0")

    label("loc_279")

    Return()

    # Function_1_24E end

    def Function_2_27A(): pass

    label("Function_2_27A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_27A")

    label("loc_28F")

    Return()

    # Function_2_27A end

    def Function_3_290(): pass

    label("Function_3_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_8D(0xFE, -6630, 65280, -3270, 67330, 1000)
    Jump("Function_3_290")

    label("loc_2B3")

    Return()

    # Function_3_290 end

    def Function_4_2B4(): pass

    label("Function_4_2B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_8D(0xFE, -2620, 970, 1167, -2110, 3000)
    Jump("Function_4_2B4")

    label("loc_2D7")

    Return()

    # Function_4_2B4 end

    def Function_5_2D8(): pass

    label("Function_5_2D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-34700, 0, 70780, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(328000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -26820, 140, 63060, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -25760, 0, 68260, 180)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, -26680, 200, 66900, 180)
    SetChrChipByIndex(0x10C, 4)
    SetChrSubChip(0x10C, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -27060, 540, 64580, 0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_3AA():
        OP_6D(-28500, 0, 67500, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3AA)

    def lambda_3C2():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #0
        0x10,
        "#6PI see... You've sure found out a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#6PWith this many potential sales routes,\x01",
            "I've got nothing to fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#6PI'll be able to make my move into the\x01",
            "Erebonian capital as soon as I'm ready\x01",
            "with this kind of information!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x10C,
        "Richard",
        (
            "#11P#1850FYou asked us to investigate the current situation\x01",
            "with regards to orbment sales in Erebonia...\x02\x03",

            "...so I centered my investigation around stores in\x01",
            "the region itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "#6PAnd you did a fantastic job, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#6PStill, the problem of transport remains.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#6PAfter all, old Borden's got his grubby hands\x01",
            "all over the international liners already.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10C,
        "Richard",
        (
            "#11P#1855FIt's true that the Borden family has preferential \x01",
            "access to 40% of the load capacity of\x01",
            "international airliners leaving Liberl for Erebonia.\x02\x03",

            "#1850FHowever, they are no longer the only available\x01",
            "option. There are now private carriers as well.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x10C, 1)
    Sleep(400)
    OP_8C(0x11, 0, 400)

    def lambda_76D():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x10C5C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_76D)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)
    OP_8C(0x11, 135, 400)

    def lambda_799():
        OP_8E(0xFE, 0xFFFF9EBC, 0x0, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_799)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x10C, 0)

    def lambda_7BE():
        OP_8E(0xFE, 0xFFFF9EBC, 0x0, 0xFC1C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7BE)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 225, 400)
    Sleep(300)

    ChrTalk(    #8
        0x11,
        (
            "#1862FHere are some supplementary materials \x01",
            "regarding that issue.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x12, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x15, 0x800)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -26220, -50, 64450, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #9
        0x10,
        "#6PMy! You certainly come prepared, don't you?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x10C,
        "Richard",
        (
            "#11P#1851FWell, this request ended up taking a little longer\x01",
            "than originally anticipated.\x02\x03",

            "Consider this a little extra on us in exchange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#6PI like those who think two steps ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#6PYou sure you don't want to come and work\x01",
            "for me? I'd pay you handsomely!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x10C,
        "Richard",
        (
            "#11P#1850FI'm certainly flattered you think highly enough of\x01",
            "my skills to offer...\x02\x03",

            "#1859FI'm not sure I have what it takes to be successful\x01",
            "in the cutthroat world of business, though.\x02\x03",

            "I'm a rather timid man, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#6PCome, now. You can't fool me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#6POh, well. Do keep my offer in mind,\x01",
            "if you would.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, -26820, 0, 63660, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(    #16
        0x11,
        "#1862FPlease allow us to escort you out.\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x6)
    Sleep(600)
    OP_43(0x11, 0x3, 0x0, 0x7)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10C, 65535)
    SetChrSubChip(0x10C, 0)
    ClearChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, -26680, 0, 66240, 180)
    Sleep(250)

    def lambda_BA3():

        label("loc_BA3")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_BA3")

    QueueWorkItem2(0x10C, 2, lambda_BA3)
    Sleep(2700)
    OP_44(0x10C, 0x2)

    def lambda_BBD():
        OP_8E(0xFE, 0xFFFF932C, 0x0, 0x102C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_BBD)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 315, 400)
    WaitChrThread(0x10, 0x3)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #17
        0x10,
        "Oh, since I have you here...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 135, 400)
    Sleep(300)

    ChrTalk(    #18
        0x10,
        (
            "...maybe I should give you one more thing\x01",
            "to look into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "I've already had Simon get started,\x01",
            "but I'm not sure he's up to the task.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x10C,
        "Richard",
        (
            "#1850F#6PI'd be happy to help if I can.\x02\x03",

            "Will this be another request to research\x01",
            "a foreign market?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "It certainly will.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x10, 225, 400)
    Sleep(300)

    ChrTalk(    #22
        0x10,
        "Oh, look what you've got over there! Perfect.\x02",
    )

    CloseMessageWindow()

    def lambda_D99():
        OP_6D(-36660, 0, 66240, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_D99)

    def lambda_DB1():
        OP_67(0, 4500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_DB1)

    def lambda_DC9():
        OP_6C(306000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_DC9)

    def lambda_DD9():
        OP_6B(3340, 4000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_DD9)
    OP_43(0x10, 0x3, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x11, 0x3, 0x0, 0xA)
    Sleep(200)
    OP_43(0x10C, 0x3, 0x0, 0x9)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x11, 0x3)
    WaitChrThread(0x10C, 0x3)

    ChrTalk(    #23
        0x10,
        "#5PThis place right here.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x10C,
        "Richard",
        "#1853FOred State?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1864F#2PThat's an unusual choice... It's quite a small\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#5PThat just makes it easier to seize a majority\x01",
            "in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#5PSmall as it is, it's not like it isn't accessible by\x01",
            "airliner, and what market there may be there is\x01",
            "all but free for the taking right now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x10C,
        "Richard",
        (
            "#1859FSo you want us to research the potential size\x01",
            "of the market there, in other words?\x02\x03",

            "#1850FShall we focus entirely on the orbment market, \x01",
            "or broaden the scope of our investigation and\x01",
            "look into the market in general?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#5PThe market in general.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 400)
    Sleep(300)

    ChrTalk(    #30
        0x10,
        "#5PDo you think you can do it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0x10C,
        "Richard",
        (
            "#1850FWith ease.\x02\x03",

            "I'll get in touch with one of our staff members\x01",
            "stationed near the state right away and begin\x01",
            "weighing options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        "#5PThat's what I wanted to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#5PI'll be back here next week, anyway.\x01",
            "We can discuss the details then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11B0():
        OP_6D(-35190, 0, 67100, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_11B0)

    def lambda_11C8():

        label("loc_11C8")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_11C8")

    QueueWorkItem2(0x10C, 2, lambda_11C8)

    def lambda_11D9():

        label("loc_11D9")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_11D9")

    QueueWorkItem2(0x11, 2, lambda_11D9)

    def lambda_11EA():
        OP_8E(0xFE, 0xFFFF7D88, 0x0, 0x10360, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11EA)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    ChrTalk(    #34
        0x10,
        "#11PTa-ta!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #35
        0x10C,
        "Richard",
        "#1850F#5PUntil then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#1862F#5PTake care.\x02",
    )

    CloseMessageWindow()

    def lambda_1261():
        OP_6D(-33510, 0, 68790, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1261)

    def lambda_1279():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10360, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1279)
    WaitChrThread(0x10, 0x1)

    def lambda_1299():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10B6C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1299)
    WaitChrThread(0x10, 0x1)

    def lambda_12B9():
        OP_8E(0xFE, 0xFFFF7D38, 0xFFFFF830, 0x10B6C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12B9)
    WaitChrThread(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_44(0x10C, 0x2)
    OP_44(0x11, 0x2)
    Sleep(1000)
    OP_8C(0x10C, 215, 400)

    def lambda_12F2():
        OP_6D(-36660, 0, 66240, 2500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_12F2)

    def lambda_130A():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0xFC07, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_130A)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 215, 400)
    WaitChrThread(0x17, 0x0)
    Sleep(300)

    NpcTalk(    #37
        0x10C,
        "Richard",
        (
            "#1855F#6PHmm... Ored's quite far inland.\x02\x03",

            "#1850FWeren't the Reins brothers in that general\x01",
            "area of the continent?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #38
        0x11,
        (
            "#1860F#11PYes, they are. I'll get in contact with them \x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x10C,
        "Richard",
        "#1850F#6PThank you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #40
        0x10C,
        "Richard",
        (
            "#1859F#6PHaha. She's not a merchant of Bose for nothing,\x01",
            "is she? \x02\x03",

            "She's always coming in with such interesting,\x01",
            "ambitious requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        "#1861F#11PShe's not half as ambitious as you are.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #42
        0x10C,
        "Richard",
        (
            "#1851F#6PI think you may be overestimating me a\x01",
            "little, there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x11, 400)
    Sleep(300)

    NpcTalk(    #43
        0x10C,
        "Richard",
        "#1850F#6P...Well, can you show our next visitor in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#1862F#11PCertainly.\x02",
    )

    CloseMessageWindow()

    def lambda_15C6():

        label("loc_15C6")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_15C6")

    QueueWorkItem2(0x10C, 2, lambda_15C6)
    OP_8C(0x11, 90, 400)

    def lambda_15DE():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15DE)
    WaitChrThread(0x11, 0x1)
    OP_44(0x10C, 0x2)
    OP_43(0x10C, 0x3, 0x0, 0xB)

    def lambda_1609():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10C5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1609)
    WaitChrThread(0x11, 0x1)

    def lambda_1629():
        OP_8E(0xFE, 0xFFFF7D88, 0xFFFFF830, 0x10C5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1629)
    WaitChrThread(0x11, 0x1)
    Sleep(1500)

    def lambda_164E():
        OP_6D(-34360, 0, 68540, 3500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_164E)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -33400, -2000, 68460, 90)

    def lambda_167C():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0x10C5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_167C)
    Sleep(600)

    def lambda_169C():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10B6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_169C)
    Sleep(1000)
    OP_43(0x10C, 0x3, 0x0, 0xE)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 215, 400)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 215, 400)
    WaitChrThread(0x10C, 0x3)

    ChrTalk(    #45
        0x12,
        (
            "#11PHello there, Alan! Sorry for dropping in on\x01",
            "you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#11PI just wanted to get your input on another little\x01",
            "something regarding the city's finances...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #47
        0x10C,
        "Richard",
        (
            "#1851F#5POh, that won't be a bother at all.\x02\x03",

            "Please, take a seat.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17D5():
        OP_6D(-28500, 0, 67500, 5000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_17D5)

    def lambda_17ED():
        OP_67(0, 5480, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_17ED)

    def lambda_1805():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1805)

    def lambda_1815():
        OP_6B(3260, 5000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_1815)

    def lambda_1825():

        label("loc_1825")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_1825")

    QueueWorkItem2(0x10C, 2, lambda_1825)
    OP_8C(0x11, 270, 500)
    OP_8C(0x12, 90, 400)
    Sleep(500)
    SetChrFlags(0x11, 0x4)

    def lambda_184E():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0xF424, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_184E)
    Sleep(700)
    OP_43(0x12, 0x3, 0x0, 0xC)
    Sleep(800)
    OP_44(0x10C, 0x2)
    OP_43(0x10C, 0x3, 0x0, 0xD)
    WaitChrThread(0x11, 0x1)

    def lambda_188A():

        label("loc_188A")

        TurnDirection(0xFE, 0x12, 600)
        OP_48()
        Jump("loc_188A")

    QueueWorkItem2(0x11, 2, lambda_188A)
    WaitChrThread(0x12, 0x3)
    OP_44(0x11, 0x2)

    def lambda_18A4():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0x10AA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18A4)
    WaitChrThread(0x11, 0x1)

    def lambda_18C4():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x10AA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18C4)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 180, 500)
    WaitChrThread(0x10C, 0x3)

    NpcTalk(    #48
        0x10C,
        "Richard",
        "#1850F#11PSo what exactly can I help you with today?\x02",
    )

    CloseMessageWindow()

    def lambda_1932():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1932)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2D8 end

    def Function_6_195A(): pass

    label("Function_6_195A")


    def lambda_1960():
        OP_8E(0xFE, 0xFFFF905C, 0x0, 0xF8AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1960)
    WaitChrThread(0x10, 0x1)

    def lambda_1980():
        OP_8E(0xFE, 0xFFFF905C, 0x0, 0x10B6C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1980)
    WaitChrThread(0x10, 0x1)

    def lambda_19A0():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10B6C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19A0)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_6_195A end

    def Function_7_19BB(): pass

    label("Function_7_19BB")


    def lambda_19C1():
        OP_8E(0xFE, 0xFFFF9EBC, 0x0, 0x10B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19C1)
    WaitChrThread(0x11, 0x1)

    def lambda_19E1():
        OP_8E(0xFE, 0xFFFF923C, 0x0, 0x10B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19E1)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_7_19BB end

    def Function_8_19FC(): pass

    label("Function_8_19FC")


    def lambda_1A02():
        OP_8E(0xFE, 0xFFFF8CD8, 0x0, 0x10360, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A02)
    WaitChrThread(0x10, 0x1)

    def lambda_1A22():
        OP_8E(0xFE, 0xFFFF7D88, 0x0, 0x10360, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A22)
    WaitChrThread(0x10, 0x1)

    def lambda_1A42():
        OP_8E(0xFE, 0xFFFF75B8, 0x0, 0xFB90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A42)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 215, 400)
    Return()

    # Function_8_19FC end

    def Function_9_1A64(): pass

    label("Function_9_1A64")


    def lambda_1A6A():
        OP_8E(0xFE, 0xFFFF7BBC, 0x0, 0x102C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1A6A)
    WaitChrThread(0x10C, 0x1)

    def lambda_1A8A():
        OP_8E(0xFE, 0xFFFF7BBC, 0x0, 0xFC07, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1A8A)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 270, 400)
    Return()

    # Function_9_1A64 end

    def Function_10_1AAC(): pass

    label("Function_10_1AAC")


    def lambda_1AB2():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10B30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AB2)
    WaitChrThread(0x11, 0x1)

    def lambda_1AD2():
        OP_8E(0xFE, 0xFFFF8EB8, 0x0, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AD2)
    WaitChrThread(0x11, 0x1)

    def lambda_1AF2():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AF2)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 180, 400)
    Return()

    # Function_10_1AAC end

    def Function_11_1B14(): pass

    label("Function_11_1B14")

    SetChrFlags(0x10C, 0x4)

    def lambda_1B1F():
        OP_8E(0xFE, 0xFFFF770C, 0x0, 0xF99C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1B1F)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 120, 400)
    Return()

    # Function_11_1B14 end

    def Function_12_1B41(): pass

    label("Function_12_1B41")

    SetChrFlags(0x12, 0x4)

    def lambda_1B4C():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0x10748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B4C)
    WaitChrThread(0x12, 0x1)

    def lambda_1B6C():
        OP_8E(0xFE, 0xFFFF9174, 0x0, 0xF8AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B6C)
    WaitChrThread(0x12, 0x1)

    def lambda_1B8C():
        OP_8E(0xFE, 0xFFFF973C, 0x0, 0xF8AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B8C)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 0, 400)
    Fade(250)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -26820, 140, 63060, 0)
    OP_0D()
    Return()

    # Function_12_1B41 end

    def Function_13_1BCF(): pass

    label("Function_13_1BCF")


    def lambda_1BD5():
        OP_8E(0xFE, 0xFFFF97C8, 0x0, 0x102C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1BD5)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 180, 400)
    Fade(250)
    SetChrChipByIndex(0x10C, 4)
    SetChrSubChip(0x10C, 0)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, -26680, 200, 66900, 180)
    OP_0D()
    Return()

    # Function_13_1BCF end

    def Function_14_1C1D(): pass

    label("Function_14_1C1D")

    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x10C, 45, 500)
    Sleep(500)

    def lambda_1C41():
        OP_8E(0xFE, 0xFFFF7C34, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1C41)
    WaitChrThread(0x10C, 0x1)

    def lambda_1C61():
        OP_8E(0xFE, 0xFFFF8314, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1C61)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 45, 500)
    Return()

    # Function_14_1C1D end

    def Function_15_1C83(): pass

    label("Function_15_1C83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-5980, 0, 65300, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10C, -4880, -500, 60500, 0)
    SetChrPos(0x11, -4880, -500, 60500, 0)
    OP_9F(0x10C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -7600, 500, 64400, 0)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_1D38():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_1D38)

    def lambda_1D4A():
        OP_8E(0xFE, 0xFFFFECF0, 0x0, 0xFAEF, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1D4A)
    Sleep(1100)

    def lambda_1D6A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1D6A)
    OP_43(0x11, 0x3, 0x0, 0x11)
    WaitChrThread(0x10C, 0x1)
    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_8C(0x10C, 270, 400)
    Sleep(300)

    NpcTalk(    #49
        0x10C,
        "Richard",
        "#1853F#11P...Hmm?\x02",
    )

    CloseMessageWindow()

    def lambda_1DCA():
        OP_6D(-7800, 0, 65300, 2000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1DCA)

    def lambda_1DE2():
        OP_8E(0xFE, 0xFFFFE638, 0x0, 0xFAEF, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1DE2)
    WaitChrThread(0x10C, 0x1)
    Sleep(500)
    Fade(500)
    OP_22(0x12, 0x0, 0x50)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    Sleep(500)

    NpcTalk(    #50
        0x10C,
        "Richard",
        "#1852F#5P(It couldn't be...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    TurnDirection(0x11, 0x10C, 400)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    def lambda_1E85():
        OP_8E(0xFE, 0xFFFFE6D8, 0x0, 0xF690, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E85)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #51
        0x11,
        (
            "#1864F#6PSir?\x02\x03",

            "Is something the matter?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #52
        0x10C,
        "Richard",
        (
            "#1855F#11P...Oh, it's nothing of much importance.\x02\x03",

            "#1850FI just noticed that we seem to have mistakenly \x01",
            "received another letter intended for the mayor.\x02\x03",

            "It's understandable that it keeps happening\x01",
            "given that this building was previously his,\x01",
            "but it is a tad troublesome nonetheless...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 135, 400)
    Sleep(300)

    NpcTalk(    #53
        0x10C,
        "Richard",
        (
            "#1850F#5PI suppose I'd better go and deliver it to him.\x01",
            "It could be something important.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x168, 0x3C, 0x64)

    def lambda_208D():

        label("loc_208D")

        TurnDirection(0xFE, 0x10C, 500)
        OP_48()
        Jump("loc_208D")

    QueueWorkItem2(0x11, 2, lambda_208D)

    def lambda_209E():
        OP_8F(0xFE, 0xFFFFEBE2, 0x0, 0xF672, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_209E)
    WaitChrThread(0x10C, 0x1)

    def lambda_20BE():
        OP_8E(0xFE, 0xFFFFECF0, 0x0, 0xF384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_20BE)
    Sleep(300)

    ChrTalk(    #54
        0x11,
        (
            "#1864F#5PNow, sir?\x02\x03",

            "Couldn't it wait? It seems like it's going to\x01",
            "start raining any minute...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10C, 0x1)

    NpcTalk(    #55
        0x10C,
        "Richard",
        (
            "#1859F#11PIt's not too far. Even if it does start raining,\x01",
            "I won't be exposed to it for long.\x02\x03",

            "#1850FCan I ask you to handle the regular reports\x01",
            "in the meantime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        "#1864F#5PY-Yes. Of course...\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_2221():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_2221)

    def lambda_2233():
        OP_8E(0xFE, 0xFFFFECF0, 0xFFFFFE0C, 0xEC54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2233)
    WaitChrThread(0x10C, 0x1)
    OP_44(0x11, 0x2)

    def lambda_2257():
        OP_8C(0x11, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2257)
    OP_22(0x7, 0x0, 0x64)
    OP_20(0xFA0)

    def lambda_226F():
        OP_6D(-7800, 0, 62300, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_226F)
    OP_43(0x17, 0x3, 0x0, 0x10)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    WaitChrThread(0x17, 0x3)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1C83 end

    def Function_16_22A6(): pass

    label("Function_16_22A6")

    OP_24(0x168, 0x5A)
    Sleep(100)
    OP_24(0x168, 0x50)
    Sleep(100)
    OP_24(0x168, 0x46)
    Sleep(100)
    OP_24(0x168, 0x3C)
    Sleep(100)
    OP_24(0x168, 0x32)
    Sleep(100)
    OP_24(0x168, 0x28)
    Sleep(100)
    OP_24(0x168, 0x1E)
    Sleep(100)
    OP_24(0x168, 0x14)
    Sleep(100)
    OP_24(0x168, 0xA)
    Sleep(100)
    OP_24(0x168, 0x0)
    OP_23(0x168)
    Return()

    # Function_16_22A6 end

    def Function_17_22FF(): pass

    label("Function_17_22FF")


    def lambda_2305():
        OP_8E(0xFE, 0xFFFFECF0, 0x0, 0xF438, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2305)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_8C(0x11, 180, 500)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_17_22FF end

    def Function_18_2336(): pass

    label("Function_18_2336")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x100000)
    OP_24(0x1C9, 0x3C)
    OP_6D(-5860, 0, 66040, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_6D(-8560, 0, 69400, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10C, -5460, -500, 60500, 0)
    OP_9F(0x10C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -4500, -500, 60500, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2408():
        OP_6D(-5860, 0, 66040, 3500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2408)

    def lambda_2420():
        OP_6C(335000, 3500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2420)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_2448():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_2448)

    def lambda_245A():
        OP_8E(0xFE, 0xFFFFEAAC, 0x0, 0xF67C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_245A)
    Sleep(800)

    def lambda_247A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_247A)

    def lambda_248C():
        OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xF5A0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_248C)
    Sleep(700)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)

    NpcTalk(    #57
        0x10C,
        "Richard",
        "#1859F#5PI wasn't expecting to end up quite this soaked.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10C, 90, 400)
    Sleep(300)

    NpcTalk(    #58
        0x10C,
        "Richard",
        "#1850F#5PAre you all right?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #59
        0x11,
        (
            "#1861F#4PI'm fine. Don't worry about me.\x02\x03",

            "#1860FThis actually brings back fond memories\x01",
            "of the survival training I underwent back\x01",
            "at the academy.\x02\x03",

            "I do think you should go and get changed\x01",
            "into some dry clothes, though, sir.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x10C,
        "Richard",
        (
            "#1850F#5PA little rain never hurt anyone.\x02\x03",

            "I don't believe I was half bad at my own\x01",
            "survival training, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "#1864F#4PEven then...\x02",
    )

    CloseMessageWindow()
    OP_22(0xC3, 0x1, 0x32)
    Sleep(800)
    OP_62(0x10C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    def lambda_26FD():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_26FD)
    OP_8C(0x11, 0, 500)
    Sleep(500)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x32)
    Sleep(500)
    OP_22(0x2BB, 0x1, 0x32)
    Sleep(2200)

    NpcTalk(    #62
        0x10C,
        "Richard",
        "#1852F#5P...An encrypted call?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#1860F#6PDilens did mention that he had some information\x01",
            "of interest in his report earlier.\x02\x03",

            "Perhaps this relates to that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #64
        0x10C,
        "Richard",
        (
            "#1850F#5PSounds possible.\x02\x03",

            "#1855FWhich would mean that something has\x01",
            "happened over in the Republic...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_284D():
        OP_8E(0xFE, 0xFFFFEAAC, 0x7D0, 0x11364, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_284D)
    Sleep(400)

    def lambda_286D():
        OP_8E(0xFE, 0xFFFFEE6C, 0x7D0, 0x11364, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_286D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10C, 0xFF)
    OP_44(0x11, 0xFF)
    OP_6D(-35000, 0, 67900, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    LoadEffect(0x0, "map\\mp001_00.eff")
    LoadEffect(0x1, "map\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -35480, 2120, 67780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10C, -33500, -2000, 69060, 90)
    SetChrPos(0x11, -33500, -2000, 69060, 90)
    OP_24(0x2BB, 0x3C)
    Sleep(200)
    OP_24(0x2BB, 0x46)
    OP_43(0x10C, 0x3, 0x0, 0x13)
    OP_43(0x11, 0x3, 0x0, 0x14)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10C, 0x3)
    OP_23(0x2BB)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -35480, 2120, 67780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    NpcTalk(    #65
        0x10C,
        "Richard",
        (
            "#1850F#20W...Yes, it's me.\x02\x03",

            "#1499F#20WCan you please stop calling me that?\x02\x03",

            "#1855F#20W...Yes. That's right...\x02\x03",

            "#20WYes... Yes...\x02\x03",

            "#20WIn the Eastern Quarter?\x02\x03",

            "#20WWe don't have anyone there yet,\x01",
            "thinking about it...\x02\x03",

            "#1850F#20WAll right. I'll look into it as best I can.\x02\x03",

            "#20WRight... You be careful, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)
    WaitChrThread(0x11, 0x3)
    Sleep(500)
    OP_8C(0x10C, 180, 400)
    Sleep(300)

    def lambda_2B26():
        OP_6D(-35000, 0, 66900, 1500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2B26)
    OP_43(0x10C, 0x1, 0x0, 0x15)

    def lambda_2B45():

        label("loc_2B45")

        TurnDirection(0xFE, 0x10C, 400)
        OP_48()
        Jump("loc_2B45")

    QueueWorkItem2(0x11, 2, lambda_2B45)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #66
        0x11,
        "#1864FHas something happened?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10C, 0x1)
    OP_44(0x11, 0x2)
    Sleep(300)

    NpcTalk(    #67
        0x10C,
        "Richard",
        (
            "#1852F#5PAnother jaeger corps has entered the Eastern\x01",
            "Quarter.\x02\x03",

            "A sizable one, too. The Red Constellation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 225, 400)
    Sleep(100)

    def lambda_2C10():
        OP_6D(-35920, 0, 65780, 2500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C10)

    def lambda_2C28():
        OP_8E(0xFE, 0xFFFF79A0, 0x0, 0xFF50, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C28)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    OP_8C(0x11, 225, 400)
    Sleep(300)

    ChrTalk(    #68
        0x11,
        (
            "#1863F#12PReally? There seems to be rather a lot of \x01",
            "activity on the jaeger front of late.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0x10C,
        "Richard",
        (
            "#1855F#5PTheir arrival makes it very likely that the power\x01",
            "struggle there will begin to worsen, too.\x02\x03",

            "I doubt the old Intelligence Division network is\x01",
            "going to be sufficient to fully stay on top of the\x01",
            "situation...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #70
        0x10C,
        "Richard",
        (
            "#1850F#5PHmm...\x02\x03",

            "#1859FI think I may have to head there personally.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E0D():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2E0D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2336 end

    def Function_19_2E3A(): pass

    label("Function_19_2E3A")


    def lambda_2E40():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2E40)
    WaitChrThread(0x10C, 0x1)

    def lambda_2E60():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2E60)
    WaitChrThread(0x10C, 0x1)

    def lambda_2E80():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2E80)
    WaitChrThread(0x10C, 0x1)

    def lambda_2EA0():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0x1093C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2EA0)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 270, 400)
    Sleep(500)
    Return()

    # Function_19_2E3A end

    def Function_20_2EC7(): pass

    label("Function_20_2EC7")

    Sleep(1000)

    def lambda_2ED2():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10DC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2ED2)
    WaitChrThread(0x11, 0x1)

    def lambda_2EF2():
        OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2EF2)
    WaitChrThread(0x11, 0x1)

    def lambda_2F12():
        OP_8E(0xFE, 0xFFFF8364, 0x0, 0x10248, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F12)
    WaitChrThread(0x11, 0x1)

    def lambda_2F32():
        OP_8E(0xFE, 0xFFFF8364, 0x0, 0x103C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F32)
    WaitChrThread(0x11, 0x1)
    Sleep(2500)
    OP_8C(0x11, 180, 500)

    def lambda_2F5E():
        OP_8E(0xFE, 0xFFFF8261, 0x0, 0xFBF4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F5E)
    WaitChrThread(0x11, 0x1)
    Fade(250)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -32180, 700, 63400, 0)
    OP_0D()
    Sleep(1800)
    OP_8C(0x11, 0, 500)

    def lambda_2FA6():
        OP_8E(0xFE, 0xFFFF8364, 0x0, 0x103C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FA6)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_20_2EC7 end

    def Function_21_2FC1(): pass

    label("Function_21_2FC1")


    def lambda_2FC7():
        OP_8E(0xFE, 0xFFFF7748, 0x0, 0xFBF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_2FC7)
    WaitChrThread(0x10C, 0x2)
    OP_8C(0x10C, 225, 400)
    Return()

    # Function_21_2FC1 end

    SaveToFile()

Try(main)
