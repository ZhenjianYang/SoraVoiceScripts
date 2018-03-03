from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Deen',                                 # 9
        'Rais',                                 # 10
        'Rocco',                                # 11
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
        "Function_4_13DA",         # 04, 4
        "Function_5_2487",         # 05, 5
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
        "Young Man's Voice",
        (
            "#3PI almost thought you guys weren't\x01",
            "gonna show up!\x02",
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

    def lambda_403():
        OP_6D(127110, 500, 28500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_403)

    def lambda_41B():
        OP_67(0, 7330, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41B)

    def lambda_433():
        OP_6B(2610, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_433)

    def lambda_443():
        OP_6C(57000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_443)

    def lambda_453():
        OP_6E(338, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_453)

    def lambda_463():
        OP_8F(0xFE, 0x1FA36, 0x0, 0x6BEE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_463)
    Sleep(100)

    def lambda_483():
        OP_8F(0xFE, 0x1FE5A, 0x0, 0x70D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_483)
    Sleep(100)

    def lambda_4A3():
        OP_8F(0xFE, 0x1FE14, 0x0, 0x67B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4A3)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_1D(0xAC)

    ChrTalk(    #1
        0x109,
        "#1064F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x105,
        "#1164F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_522")

    ChrTalk(    #3
        0x106,
        "#055F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_522")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D")

    ChrTalk(    #4
        0x101,
        "#1005F#6PThe Ravens!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_54D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_576")

    ChrTalk(    #5
        0x102,
        "#1504F#6PYou're...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_576")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A9")

    ChrTalk(    #6
        0x104,
        "#1543F#6PHmm? Aren't you...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_5A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D6")

    ChrTalk(    #7
        0x108,
        "#073F#6PAren't you...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_5D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FA")

    ChrTalk(    #8
        0x103,
        "#1523F#6P...Hmm?\x02",
    )

    CloseMessageWindow()

    label("loc_5FA")


    ChrTalk(    #9
        0x10,
        (
            "#1741F#5PYou guys look like you've just seen\x01",
            "a ghost or somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#1751F#11PHaha! That surprised to see us here, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1063F#6PWho're you guys? I've never even seen you before.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80C")

    ChrTalk(    #12
        0x106,
        (
            "#551F#6PThey're part of the Ravens, a gang that used to\x01",
            "hang around over in Ruan. They recently passed\x01",
            "the exam to become junior bracers, though.\x02\x03",

            "#057FHey! The hell are you guys doing here?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D1")

    ChrTalk(    #13
        0x101,
        "#1004F#6PThey actually became bracers? Cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_809")

    label("loc_7D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_809")

    ChrTalk(    #14
        0x102,
        "#1502F#6PI didn't know about that...\x02",
    )

    CloseMessageWindow()

    label("loc_809")

    Jump("loc_9C7")

    label("loc_80C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A9")

    ChrTalk(    #15
        0x101,
        (
            "#1007F#6PThey're a bunch of delinquents from this\x01",
            "group that hangs around Ruan called the\x01",
            "Ravens.\x02\x03",

            "#1005FWhat're you guys doing here?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C7")

    label("loc_8A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_931")

    ChrTalk(    #16
        0x102,
        (
            "#1505F#6PThey're members of a group that hangs\x01",
            "around Ruan called the Ravens.\x02\x03",

            "#1502FWhat are you all doing here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C7")

    label("loc_931")


    ChrTalk(    #17
        0x105,
        (
            "#1163F#6PThey're members of the Ravens, a group that\x01",
            "usually gathers in the harbor area in Ruan City.\x02\x03",

            "But what are the three of you doing here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C7")


    ChrTalk(    #18
        0x12,
        (
            "#1763F#11PHmph. Damned if we know.\x02\x03",

            "#1761FAll of a sudden, we just...were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#1162F#6PWait. Are you implying...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1746F#5PWe're not real, by the looks of it.\x02\x03",

            "#1740FWe're just imitations of our real selves created\x01",
            "by someone or something to do battle with you.\x01",
            "That's all we're here for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x109,
        (
            "#1065F#6PSo you're copies of real people created here like\x01",
            "Celeste, then?\x02\x03",

            "#1063FAlthough unlike her, it was the Lord of Phantasma\x01",
            "that created you. Maybe.\x02\x03",

            "And if that's the case, you're not gonna let us go\x01",
            "without a fight, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#1750F#2PCan't say I've got anything against you guys,\x01",
            "but fightin' you is what we're here for, so yep.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5C")

    ChrTalk(    #23
        0x12,
        (
            "#1761F#11PAnd if we can't go against it, we might as well\x01",
            "enjoy it!\x02\x03",

            "Time to pay you back for workin' us to the bone,\x01",
            "Agate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        "#051F#6PHeh. Show me what you got!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E62")

    label("loc_D5C")


    ChrTalk(    #25
        0x12,
        (
            "#1761F#11PAnd if we can't go against it, we might as well\x01",
            "enjoy it!\x02\x03",

            "Time to show off how much stronger we've\x01",
            "gotten since that redheaded bastard started\x01",
            "workin' us to the bone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1840F#6PHeh. Agate must be a real slave driver to fire\x01",
            "you up this much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E62")


    ChrTalk(    #27
        0x105,
        (
            "#1167F#6PIf we have no choice, then let's fight with all\x01",
            "we have.\x02",
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
            "#1749F#5P*sigh* I can't help but wonder how we of all folks\x01",
            "ended up being created here to fight you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        "#1756F#11PI guess this is just fate or somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "#1766F#11PJust don't even think of holding back.\x01",
            "Come at us with all you've got!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102A")

    ChrTalk(    #31
        0x102,
        "#1506F#6PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_102A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(    #32
        0x10F,
        "#1441F#6PWe won't!\x02",
    )

    CloseMessageWindow()

    label("loc_1050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107B")

    ChrTalk(    #33
        0x101,
        "#1006F#6PYou've got it!\x02",
    )

    CloseMessageWindow()

    label("loc_107B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A2")

    ChrTalk(    #34
        0x10B,
        "#210F#6PHere we go!\x02",
    )

    CloseMessageWindow()

    label("loc_10A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F3")

    ChrTalk(    #35
        0x110,
        (
            "#268F#6P*sigh* They sure are a hotblooded bunch,\x01",
            "aren't they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1124")

    ChrTalk(    #36
        0x107,
        "#065F#6PI won't let you down!\x02",
    )

    CloseMessageWindow()

    label("loc_1124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1159")

    ChrTalk(    #37
        0x10A,
        "#816F#6PTime for a serious brawl!\x02",
    )

    CloseMessageWindow()

    label("loc_1159")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118D")

    ChrTalk(    #38
        0x103,
        "#1536F#6PHeehee. That's the way!\x02",
    )

    CloseMessageWindow()

    label("loc_118D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C1")

    ChrTalk(    #39
        0x108,
        "#070F#6PShow us what you can do!\x02",
    )

    CloseMessageWindow()

    label("loc_11C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F8")

    ChrTalk(    #40
        0x104,
        "#1545F#6PThen let the battle begin!\x02",
    )

    CloseMessageWindow()

    label("loc_11F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(    #41
        0x10E,
        "#172F#6POnward!\x02",
    )

    CloseMessageWindow()

    label("loc_121B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(    #42
        0x10D,
        "#271F#6PBegin!\x02",
    )

    CloseMessageWindow()

    label("loc_123D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1261")

    ChrTalk(    #43
        0x10C,
        "#114F#6PTo arms!\x02",
    )

    CloseMessageWindow()

    label("loc_1261")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1297")

    ChrTalk(    #44
        0x106,
        "#054F#6PShow me what you guys got!\x02",
    )

    CloseMessageWindow()

    label("loc_1297")

    Sleep(300)

    def lambda_12A2():
        OP_6D(127600, 0, 28260, 200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_12A2)

    def lambda_12BA():
        OP_67(0, 8109, -10000, 200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_12BA)

    def lambda_12D2():
        OP_6B(2000, 200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_12D2)

    def lambda_12E2():
        OP_6E(304, 200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_12E2)
    SetChrChipByIndex(0x12, 9)

    def lambda_12F7():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_12F7)
    SetChrChipByIndex(0x10, 4)

    def lambda_1317():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1317)
    SetChrChipByIndex(0x11, 7)

    def lambda_1337():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1337)

    def lambda_1352():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1352)

    def lambda_136D():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_136D)

    def lambda_1388():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1388)

    def lambda_13A3():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_13A3)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x29E, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1AF end

    def Function_4_13DA(): pass

    label("Function_4_13DA")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1517")
    SetChrPos(0xEF, 125510, 0, 28500, 90)
    SetChrPos(0xF0, 124170, 0, 26900, 90)
    SetChrPos(0xF1, 123920, 0, 28340, 90)
    Jump("loc_159C")

    label("loc_1517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155B")
    SetChrPos(0xF0, 125510, 0, 28500, 90)
    SetChrPos(0xEF, 124170, 0, 26900, 90)
    SetChrPos(0xF1, 123920, 0, 28340, 90)
    Jump("loc_159C")

    label("loc_155B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159C")
    SetChrPos(0xF1, 125510, 0, 28500, 90)
    SetChrPos(0xEF, 124170, 0, 26900, 90)
    SetChrPos(0xF0, 123920, 0, 28340, 90)

    label("loc_159C")

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
        "#1749F#5PCruuud...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#1757FW-Whew... You got us good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x12,
        (
            "#1763F#11PHeh. Looks like we're gonna have to get a hell of\x01",
            "a lot stronger if we wanna rank up to being senior\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        (
            "#1066F#6PHey! There's no need to be hard on yourselves.\x01",
            "You put up a damn good fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x105,
        "#1168F#6PI agree. You did very well.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192C")

    ChrTalk(    #50
        0x106,
        (
            "#053F#6PRemember what I said after your exam? You've got\x01",
            "the strength--how far you can go after this is just a\x01",
            "matter of experience.\x02\x03",

            "#051FMake sure you put as much into your bracer work\x01",
            "as you did into that battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        (
            "#1761F#11PHeh. You just can't resist a chance to act like\x01",
            "our teacher, can you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A41")

    label("loc_192C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A41")

    ChrTalk(    #52
        0x101,
        (
            "#1001F#6PYeah. You guys really went all out.\x02\x03",

            "#1006FI'm surprised you ended up becoming bracers,\x01",
            "but you've shown you got what it takes in my\x01",
            "eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x11,
        (
            "#1756FOooh! Praise from Estelle! Now there's somethin'\x01",
            "that'll put me on cloud nine for at least a week.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A41")


    ChrTalk(    #54
        0x10,
        (
            "#1746F#5PEither way, it looks like our role in this world\x01",
            "is over now.\x02\x03",

            "#1740FWe've got no way of telling if our real selves\x01",
            "are even gonna be aware of what happened\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        (
            "#1751F...but, well, if you run into us in the real world\x01",
            "again, say hi, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x12,
        (
            "#1763F#11PDon't get cocky 'cause you won, though.\x01",
            "The guy waitin' up ahead is nastier than\x01",
            "we could dream of.\x02\x03",

            "#1761FYou're not gonna stand a chance if you\x01",
            "don't give it everything you've got.\x02",
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

    def lambda_1CEE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1CEE)

    def lambda_1D00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D00)

    def lambda_1D12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D12)
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

    def lambda_1DC0():
        OP_6D(125860, 0, 28600, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DC0)

    def lambda_1DD8():
        OP_67(0, 8130, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DD8)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #57
        0x105,
        "#1164F#6PThey just...vanished.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E81")

    ChrTalk(    #58
        0x106,
        (
            "#556F#6PHeh. Hang around just long enough to say\x01",
            "their piece and then off they go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDE")

    label("loc_1E81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDE")

    ChrTalk(    #59
        0x104,
        (
            "#1541F#6PThey stay just long enough to say their piece,\x01",
            "then off they go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F2F")

    ChrTalk(    #60
        0x101,
        "#1016F#6PThey left us some pretty useful advice, at least!\x02",
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F80")

    ChrTalk(    #61
        0x102,
        "#1514F#6PThey left us some pretty useful advice, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD0")

    ChrTalk(    #62
        0x107,
        "#067F#6PThey left us some pretty useful advice, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_201D")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(    #63
        0x10A,
        "#811F#6PThey left us some pretty useful advice, at least.\x02",
    )

    CloseMessageWindow()

    label("loc_201D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_205D")

    ChrTalk(    #64
        0x10F,
        "#1447F#6PThey seemed like likable people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2136")

    label("loc_205D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20AC")

    ChrTalk(    #65
        0x10B,
        (
            "#210F#6PThey seem like decent enough guys,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2136")

    label("loc_20AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F5")

    ChrTalk(    #66
        0x103,
        "#1527F#6PThey seem like decent guys, to be honest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2136")

    label("loc_20F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2136")

    ChrTalk(    #67
        0x108,
        "#070F#6PThey're a decent bunch, to be honest.\x02",
    )

    CloseMessageWindow()

    label("loc_2136")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2189")

    ChrTalk(    #68
        0x110,
        (
            "#261F#6PThey seem too nice to be delinquents,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EB")

    label("loc_2189")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EB")

    ChrTalk(    #69
        0x10D,
        (
            "#278F#6PHeh. They don't really seem cut out to be \x01",
            "delinquents, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_224C")

    ChrTalk(    #70
        0x10E,
        (
            "#171F#6PHaha... I look forward to seeing what kind of\x01",
            "bracers they become.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22AA")

    label("loc_224C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22AA")

    ChrTalk(    #71
        0x10C,
        (
            "#111F#6PHaha... I look forward to seeing what kind of\x01",
            "bracers they become.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22AA")


    ChrTalk(    #72
        0x109,
        (
            "#1065F#5PAnyone else feel like the purple-haired guy's\x01",
            "parting words were on the ominous side?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #73
        0x109,
        "#1063F#12PWe're heading towards the old schoolhouse, right?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)
    Sleep(300)

    ChrTalk(    #74
        0x105,
        (
            "#1167F#5PThat's right. It's a stone building that was used\x01",
            "by the academy until a few decades ago. It's no\x01",
            "longer in use these days.\x02\x03",

            "#1162FI'm not sure who Rocco was referring to, but it \x01",
            "sounds like we should make sure we're ready\x01",
            "before going inside.\x02",
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

    # Function_4_13DA end

    def Function_5_2487(): pass

    label("Function_5_2487")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A8")
    Sleep(100)
    Jump("loc_2523")

    label("loc_24A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24BD")
    Sleep(200)
    Jump("loc_2523")

    label("loc_24BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D2")
    Sleep(300)
    Jump("loc_2523")

    label("loc_24D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E7")
    Sleep(400)
    Jump("loc_2523")

    label("loc_24E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24FC")
    Sleep(500)
    Jump("loc_2523")

    label("loc_24FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2511")
    Sleep(600)
    Jump("loc_2523")

    label("loc_2511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2523")
    Sleep(700)

    label("loc_2523")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2545")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_2523")

    label("loc_2545")

    Return()

    # Function_5_2487 end

    SaveToFile()

Try(main)
