from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5901   ._SN',
        MapName             = 'Other',
        Location            = 'C5901.x',
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
        'Nial',                                 # 9
        'Dorothy',                              # 10
        'Park Block - Calmare I',               # 11
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT06/CH20063 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT06/CH20063P._CP',             # 01
    )

    DeclNpc(
        X                   = 550,
        Z                   = -8000,
        Y                   = -84180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = -8000,
        Y                   = -74410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -10,
        Z                   = 0,
        Y                   = -46260,
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
        X                   = 0,
        Y                   = -6000,
        Z                   = -105000,
        Range               = 2000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 28020,
        TriggerZ            = -7650,
        TriggerY            = -71570,
        TriggerRange        = 1000,
        ActorX              = 28320,
        ActorZ              = -6350,
        ActorY              = -71070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_23F",          # 03, 3
        "Function_4_4C0",          # 04, 4
        "Function_5_86E",          # 05, 5
        "Function_6_8E2",          # 06, 6
        "Function_7_CE2",          # 07, 7
        "Function_8_DD5",          # 08, 8
        "Function_9_E17",          # 09, 9
        "Function_10_F7D",         # 0A, 10
        "Function_11_10F7",        # 0B, 11
        "Function_12_117D",        # 0C, 12
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170")
    Jump("loc_190")

    label("loc_170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B")
    Jump("loc_190")

    label("loc_17B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_190")

    label("loc_190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1A1")
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_1DF")

    label("loc_1A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1B2")
    OP_A3(0x10F1)
    Event(0, 7)
    Jump("loc_1DF")

    label("loc_1B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1C3")
    OP_A3(0x10F2)
    Event(0, 10)
    Jump("loc_1DF")

    label("loc_1C3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_1CF"),
        (SWITCH_DEFAULT, "loc_1DF"),
    )


    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF")
    Event(0, 6)

    label("loc_1DF")

    Return()

    # Function_0_15E end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFCD380, 0x23007A)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 5)), scpexpr(EXPR_END)), "loc_215")
    OP_71(0x3, 0x10)
    OP_64(0x0, 0x1)
    OP_71(0x4, 0x4)

    label("loc_215")

    OP_22(0x1CA, 0x1, 0x64)
    Return()

    # Function_1_1E0 end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23E")
    OP_8D(0xFE, -1490, -89750, 1490, -74630, 2000)
    Jump("Function_2_21B")

    label("loc_23E")

    Return()

    # Function_2_21B end

    def Function_3_23F(): pass

    label("Function_3_23F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x101,
        "#1004FNial? What are you doing out here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#140FJust lookin' around a bit, is all.\x02\x03",

            "Already got all the photos we need\x01",
            "of the ship and its surroundings.\x02\x03",

            "But it's still hard to wrap my head\x01",
            "around all this bein' in the sky.\x02\x03",

            "Looks like this area's a park\x01",
            "or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x22D3)
    Jump("loc_4BC")

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427")

    ChrTalk(    #2
        0x8,
        (
            "#140FA lake up in the sky, and the\x01",
            "waterfall that feeds it...\x02\x03",

            "Looks like this area's a park\x01",
            "or somethin'.\x02\x03",

            "I should make sure Dorothy gets\x01",
            "some photos of all this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4BC")

    label("loc_427")


    ChrTalk(    #3
        0x8,
        (
            "#140FA lake up in the sky and the\x01",
            "waterfall that feeds it...\x02\x03",

            "#141FY'know what I see when I look at this?\x01",
            "I see the cover of a special edition!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC")

    TalkEnd(0xFE)
    Return()

    # Function_3_23F end

    def Function_4_4C0(): pass

    label("Function_4_4C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #4
        0x101,
        "#1004FDorothy? What are you doing out here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#150FOh, hiiii!\x01",
            "I'm getting photos for the front page!\x02\x03",

            "But there are so, so many things to shoot\x01",
            "that I just don't know where to point my\x01",
            "camera next!\x02\x03",

            "Ooooh, maybe I should take pictures\x01",
            "of that cute neato elevator!\x02\x03",

            "#151FOr, I know! I'll ride it, and see what\x01",
            "other treasures it leads me to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1016FUh, yeeeeah. Just don't wander too\x01",
            "far from the Arseille, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x22D3)
    Jump("loc_86A")

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(    #7
        0x9,
        (
            "#150FOooh, there's so, so many things to\x01",
            "shoot, I can't even make up my mind!\x02\x03",

            "I think I'll take pictures of that neato\x01",
            "waterfall first, like Nial said.\x02\x03",

            "And then, pictures of the elevator!\x02\x03",

            "#151FOr, I know! I'll ride it and see what\x01",
            "other treasures it leads me to!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_86A")

    label("loc_7A0")


    ChrTalk(    #8
        0x9,
        (
            "#150FI think I'll take pictures of that neato\x01",
            "waterfall first, like Nial said!\x02\x03",

            "That elevator looks so fun to ride,\x01",
            "though...\x02\x03",

            "Oh, I know! I'll ride it and see what\x01",
            "other treasures it leads me to!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A")

    TalkEnd(0xFE)
    Return()

    # Function_4_4C0 end

    def Function_5_86E(): pass

    label("Function_5_86E")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-980, 0, -103450, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(27200, 0)
    OP_6C(21000, 0)
    OP_6E(236, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_86E end

    def Function_6_8E2(): pass

    label("Function_6_8E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    Call(0, 11)
    Call(0, 12)

    label("loc_904")

    OP_6D(-21660, -2500, -66230, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(1150, 0)
    OP_6C(33000, 0)
    OP_6E(602, 0)
    SetChrPos(0x101, 1320, -500, -56520, 180)
    SetChrPos(0x102, 150, -500, -56440, 180)
    SetChrPos(0xF8, 1220, -500, -55050, 180)
    SetChrPos(0xF9, -170, -500, -55050, 180)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_995():
        OP_6D(9270, -8000, -86360, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_995)

    def lambda_9AD():
        OP_67(0, 8039, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9AD)

    def lambda_9C5():
        OP_6B(9070, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9C5)

    def lambda_9D5():
        OP_6C(336000, 12000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D5)

    def lambda_9E5():
        OP_6E(600, 12000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E5)
    OP_C8(0x200, 0x46, "C_PLAC26._CH", 0x0, 0xFA0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    Fade(500)
    OP_6D(1870, -500, -56280, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4030, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_DC()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A77")

    ChrTalk(    #9
        0x107,
        "#560F#6PWow!\x02",
    )

    CloseMessageWindow()

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #10
        0x105,
        "#1168F#6PIt's beautiful!\x02",
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACB")

    ChrTalk(    #11
        0x103,
        "#027F#6PWhat a view.\x02",
    )

    CloseMessageWindow()

    label("loc_ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0A")

    ChrTalk(    #12
        0x109,
        "#1064F#6PWellll, that's definitely a sight!\x02",
    )

    CloseMessageWindow()

    label("loc_B0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5A")

    ChrTalk(    #13
        0x104,
        (
            "#031F#6PAh... I have searched for\x01",
            "beauty, and now I find it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B82")

    ChrTalk(    #14
        0x106,
        "#052F#6PWell...damn.\x02",
    )

    CloseMessageWindow()

    label("loc_B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC5")

    ChrTalk(    #15
        0x108,
        "#070F#6PMmmm. This place is clean...refreshing.\x02",
    )

    CloseMessageWindow()

    label("loc_BC5")


    ChrTalk(    #16
        0x101,
        (
            "#1016F#6PI'm not even sure how to put this...\x02\x03",

            "#1008FIt's sort of hard to believe we're\x01",
            "in the sky, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#1035F#6PThe ancient Zemurian culture was\x01",
            "more than just its technology...\x02\x03",

            "#1040FIt seems they had a great understanding\x01",
            "of how to use their technology, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2202)
    EventEnd(0x0)
    Return()

    # Function_6_8E2 end

    def Function_7_CE2(): pass

    label("Function_7_CE2")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(140, -6000, -104620, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 500)
    FadeToBright(1000, 0)

    def lambda_D4B():
        OP_6D(27920, -7650, -71810, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4B)
    OP_6C(327000, 7000)
    Fade(500)
    OP_6D(26130, -8000, -68590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(327000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    OP_71(0x4, 0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_CE2 end

    def Function_8_DD5(): pass

    label("Function_8_DD5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        "\x07\x05The door is firmly locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_DD5 end

    def Function_9_E17(): pass

    label("Function_9_E17")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(0, -6000, -105000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x101, 0, -6000, -104000, 0)
    OP_89(0x102, -1000, -6000, -105000, 0)
    OP_89(0xF8, 1000, -6000, -105000, 0)
    OP_89(0xF9, 0, -6000, -106000, 0)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)

    def lambda_EC3():
        OP_6D(0, 45000, -105000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC3)

    def lambda_EDB():
        OP_67(0, 10500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDB)

    def lambda_EF3():
        OP_6C(320000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EF3)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1CA, 0x5A)
    Sleep(100)
    OP_24(0x1CA, 0x50)
    Sleep(100)
    OP_24(0x1CA, 0x46)
    Sleep(100)
    OP_24(0x1CA, 0x3C)
    Sleep(100)
    OP_24(0x1CA, 0x32)
    Sleep(100)
    OP_24(0x1CA, 0x28)
    Sleep(100)
    OP_24(0x1CA, 0x1E)
    Sleep(100)
    OP_24(0x1CA, 0x14)
    Sleep(100)
    OP_24(0x1CA, 0xA)
    Sleep(100)
    OP_23(0x1CA)
    Sleep(500)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_E17 end

    def Function_10_F7D(): pass

    label("Function_10_F7D")

    EventBegin(0x0)
    OP_6D(0, 40000, -105000, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(319000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 500)
    OP_48()
    OP_89(0x101, 0, 100000, -104000, 0)
    OP_89(0x102, -1000, 100000, -105000, 0)
    OP_89(0xF8, 1000, 100000, -105000, 0)
    OP_89(0xF9, 0, 100000, -106000, 0)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)

    def lambda_101C():
        OP_6D(0, -6000, -105000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_101C)

    def lambda_1034():
        OP_67(0, 6500, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1034)

    def lambda_104C():
        OP_6C(315000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_104C)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(0, -5990, -102670, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, -6000, -102670, 0)
    SetChrPos(0x1, 0, -6000, -102670, 0)
    SetChrPos(0x2, 0, -6000, -102670, 0)
    SetChrPos(0x3, 0, -6000, -102670, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_F7D end

    def Function_11_10F7(): pass

    label("Function_11_10F7")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1170"),
        (1, "loc_1176"),
        (SWITCH_DEFAULT, "loc_117C"),
    )


    label("loc_1170")

    OP_A2(0x1200)
    Jump("loc_117C")

    label("loc_1176")

    OP_A2(0x1201)
    Jump("loc_117C")

    label("loc_117C")

    Return()

    # Function_11_10F7 end

    def Function_12_117D(): pass

    label("Function_12_117D")

    FadeToDark(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_12_117D end

    SaveToFile()

Try(main)
