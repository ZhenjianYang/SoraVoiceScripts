from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0610   ._SN',
        MapName             = 'Event',
        Location            = 'E0610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Enhanced Jaeger',                      # 9
        'Enhanced Jaeger',                      # 10
        'Enhanced Jaeger',                      # 11
        'Gilbert',                              # 12
        'Target Camera',                        # 13
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
        'ED6_DT26/CH20396 ._CH',             # 00
        'ED6_DT26/CH20760 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20396P._CP',             # 00
        'ED6_DT26/CH20760P._CP',             # 01
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_19E",          # 02, 2
        "Function_3_934",          # 03, 3
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_180")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_197")

    label("loc_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_197")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_197")

    Return()

    # Function_0_15A end

    def Function_1_198(): pass

    label("Function_1_198")

    OP_22(0x7A, 0x1, 0x46)
    Return()

    # Function_1_198 end

    def Function_2_19E(): pass

    label("Function_2_19E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_24(0x7A, 0x46)
    OP_6D(-72100, 1000, 980, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13, -70600, 1200, -160, 270)
    SetChrPos(0x11, -70600, 1200, 2150, 270)
    SetChrPos(0x12, -70600, 1200, -2500, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x13, 0x2)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x12,
        "#6PThe Bobcat, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        "#6PYou familiar with it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x13,
        "Blue-Haired Jaeger",
        "You could say that.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x13,
        "Blue-Haired Jaeger",
        (
            "I'm surprised by what I'm seeing here,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x13,
        "Blue-Haired Jaeger",
        (
            "Last I saw them, they were sky bandits,\x01",
            "but it looks like they're running a delivery\x01",
            "service now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x13,
        "Blue-Haired Jaeger",
        "Heh. Really, now? Talk about simpletons.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "Anyway, looks like they have no interest\x01",
            "in fighting us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        "Let's just leave 'em be.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #8
        0x13,
        "Blue-Haired Jaeger",
        "...Not so fast. Have you forgotten our mission?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x13,
        "Blue-Haired Jaeger",
        (
            "I'd say they're the perfect target for carrying\x01",
            "it out, wouldn't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0xC8, 1700, 0x2, 0x7, 0x64, 0x1)
    Sleep(50)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0xC8, 1700, 0x2, 0x7, 0x64, 0x1)
    Sleep(1000)
    SetChrSubChip(0x11, 1)
    Sleep(50)
    SetChrSubChip(0x12, 2)
    Sleep(300)

    ChrTalk(    #10
        0x11,
        (
            "...Wait. You're pulling my leg, right?\x01",
            "Attacking THEM?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#6PWe only need to test whether they operate\x01",
            "properly today. There's no reason to actually\x01",
            "use them in combat.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #12
        0x13,
        "Blue-Haired Jaeger",
        (
            "Puh-lease, my comrade. You're never going to\x01",
            "move up the ranks with that attitude.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x13,
        "Blue-Haired Jaeger",
        (
            "If our target was a Royal Army ship, I'd agree\x01",
            "with you...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x13,
        "Blue-Haired Jaeger",
        (
            "...but it's just an isolated ship full of ex-bandits.\x01",
            "There's no risk to be had here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "W-Well, I suppose that's true...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x13,
        "Blue-Haired Jaeger",
        (
            "Besides, the Thirteen Factories want accurate\x01",
            "combat data.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x13,
        "Blue-Haired Jaeger",
        (
            "There's no way we're going to get punished for\x01",
            "doing this! We might even earn ourselves a nice\x01",
            "reward.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0)
    Sleep(300)

    ChrTalk(    #18
        0x11,
        "...All right. You talk a good game.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0)
    Sleep(300)

    ChrTalk(    #19
        0x12,
        (
            "#6PBut if this thing backfires, you're taking\x01",
            "responsibility for whatever happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8CB():

        label("loc_8CB")

        OP_7C(0x32, 0x32, 0xBB8, 0x3E8)
        OP_48()
        Jump("loc_8CB")

    QueueWorkItem2(0x10, 3, lambda_8CB)
    OP_24(0x7A, 0x50)
    Sleep(200)
    OP_24(0x7A, 0x5A)
    Sleep(200)
    OP_24(0x7A, 0x64)
    Sleep(600)

    def lambda_901():
        OP_6D(-32100, 1000, 980, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_901)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_19E end

    def Function_3_934(): pass

    label("Function_3_934")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_24(0x7A, 0x46)
    OP_6D(-72100, 1000, 980, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, -70600, 1200, 2150, 270)
    SetChrPos(0x12, -70600, 1200, -2500, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_62(0x12, 0xC8, 1500, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0xC8, 1500, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_63(0x12)
    OP_63(0x11)
    Sleep(500)
    SetChrSubChip(0x12, 2)
    Sleep(300)

    ChrTalk(    #20
        0x12,
        (
            "#6PWhat should we do? Should we go down and \x01",
            "recover him?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 1)
    Sleep(300)

    ChrTalk(    #21
        0x11,
        "What? Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        "Forget it. I say we just leave him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#6PLord Campanella seems to have taken quite\x01",
            "a liking to him, though... You sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "I think that's all the more reason we should\x01",
            "leave him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "You know what Lord Campanella's personality\x01",
            "is like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "He'll probably find the whole thing much more \x01",
            "entertaining this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        "#6P...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0)
    Sleep(500)

    ChrTalk(    #28
        0x12,
        "#6PI guess you're right.\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_C2A():
        OP_6D(-32100, 1000, 980, 7000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_C2A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2507)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_934 end

    SaveToFile()

Try(main)
