from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0304   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0304.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60125",
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
        'Dummy',                                # 9
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


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = -170,
        TriggerY            = 2770,
        TriggerRange        = 1000,
        ActorX              = 3450,
        ActorZ              = 800,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_12C",          # 01, 1
        "Function_2_196",          # 02, 2
        "Function_3_2EB",          # 03, 3
        "Function_4_82B",          # 04, 4
        "Function_5_A10",          # 05, 5
        "Function_6_D05",          # 06, 6
        "Function_7_1250",         # 07, 7
        "Function_8_133C",         # 08, 8
        "Function_9_1377",         # 09, 9
        "Function_10_1416",        # 0A, 10
        "Function_11_1468",        # 0B, 11
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_108")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 3)
    Jump("loc_12B")

    label("loc_108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_119")
    OP_A3(0x10F1)
    Event(0, 7)
    Jump("loc_12B")

    label("loc_119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 7)), scpexpr(EXPR_END)), "loc_127")
    Event(0, 8)
    Jump("loc_12B")

    label("loc_127")

    Event(0, 4)

    label("loc_12B")

    Return()

    # Function_0_EE end

    def Function_1_12C(): pass

    label("Function_1_12C")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xD6D8, 0x0)
    OP_43(0x8, 0x0, 0x0, 0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A")
    OP_6F(0x0, 0)
    Jump("loc_161")

    label("loc_15A")

    OP_6F(0x0, 60)

    label("loc_161")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_187")
    OP_65(0x0, 0x1)
    OP_72(0x0, 0x0)
    OP_72(0x0, 0x4)
    Jump("loc_195")

    label("loc_187")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)

    label("loc_195")

    Return()

    # Function_1_12C end

    def Function_2_196(): pass

    label("Function_2_196")

    OP_EA(0x2, 0x8, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x276, 1)"), scpexpr(EXPR_END)), "loc_207")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x76\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1968)
    Jump("loc_26B")

    label("loc_207")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x76\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x76\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_26B")

    Jump("loc_2DD")

    label("loc_26E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Were you hoping somebody would come along\x01",
            "and put in MORE stuff for you to take?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2DD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_196 end

    def Function_3_2EB(): pass

    label("Function_3_2EB")

    EventBegin(0x4)
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_315")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_315")

    SetChrPos(0x101, 3980, -160, 2990, 0)
    SetChrPos(0x103, 2730, -180, 2840, 0)
    SetChrPos(0xF8, 4260, -180, 1570, 0)
    SetChrPos(0xF9, 2840, -170, 1480, 0)
    OP_6D(3720, -160, 2770, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#1007F#6PWh-What the heck was all that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#522F#6PThe instant that bell rang,\x01",
            "we were engulfed in fog...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 270, 400)
    Sleep(500)

    ChrTalk(    #5
        0x103,
        "#023F#6P*gasp* No!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #6
        0x101,
        "#1004F#6PBwuh?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x7D)
    OP_1F(0x50, 0x64)
    Sleep(300)
    StopSound(0x64, 0x186A0, 0x1388)

    def lambda_496():
        OP_6B(6000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_496)
    Sleep(1000)

    def lambda_4AB():
        OP_6C(135000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AB)
    OP_8C(0x101, 90, 400)
    Sleep(100)
    OP_8C(0xF8, 90, 400)
    Sleep(100)
    OP_8C(0xF9, 180, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #7
        0x101,
        (
            "#1020F#6PYaa-aaah!\x02\x03",

            "Wh-Where are we NOW?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(3630, -150, 1970, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    StopSound(0x64, 0xD6D8, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BC")

    ChrTalk(    #8
        0x107,
        (
            "#065F#6PTh-The scenery's all different all\x01",
            "of a sudden!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_659")

    label("loc_5BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_606")

    ChrTalk(    #9
        0x106,
        (
            "#552F#6PDamn, our surroundings are\x01",
            "different again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_659")

    label("loc_606")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_659")

    ChrTalk(    #10
        0x105,
        (
            "#042F#6PIt looks like we're somewhere\x01",
            "completely different now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_659")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C1")

    ChrTalk(    #11
        0x108,
        (
            "#072F#6PWhat...? Qi Men Dun Jia?!\x01",
            "The Gates of Wonder and\x01",
            "the Hidden Wood?! How--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C")

    label("loc_6C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70C")

    ChrTalk(    #12
        0x104,
        (
            "#032F#6PHm. We appear to have been\x01",
            "sent somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #13
        0x101,
        "#1020F#6PSchera! What should we do?\x02",
    )

    CloseMessageWindow()

    def lambda_742():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_742)
    Sleep(100)

    def lambda_755():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_755)
    Sleep(100)
    OP_8C(0x103, 90, 400)

    ChrTalk(    #14
        0x103,
        (
            "#026F#4PCalm down, Estelle.\x02\x03",

            "#022FThere should...probably be a way out.\x02\x03",

            "We need to focus and find that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1002F#6PUm, right...\x02",
    )

    CloseMessageWindow()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1825)
    OP_28(0x92, 0x1, 0x4)
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_2EB end

    def Function_4_82B(): pass

    label("Function_4_82B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_843"),
        (105, "loc_86D"),
        (107, "loc_897"),
        (106, "loc_8C1"),
        (SWITCH_DEFAULT, "loc_8EB"),
    )


    label("loc_843")

    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86A")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86A")

    Jump("loc_8EB")

    label("loc_86D")

    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_894")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_894")

    Jump("loc_8EB")

    label("loc_897")

    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BE")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BE")

    Jump("loc_8EB")

    label("loc_8C1")

    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8E8")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E8")

    Jump("loc_8EB")

    label("loc_8EB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_901")
    OP_A2(0x1842)
    Call(0, 6)
    Jump("loc_A0F")

    label("loc_901")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_92A")

    label("loc_91D")

    RunExpression(0x2, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_92A")

    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_946")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_953")

    label("loc_946")

    RunExpression(0x3, (scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_953")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_973")
    Call(0, 6)
    Jump("loc_A0F")

    label("loc_973")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    Call(0, 5)
    Jump("loc_A0F")

    label("loc_98C")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_9C4"),
        (1, "loc_9CC"),
        (2, "loc_9D4"),
        (3, "loc_9DC"),
        (4, "loc_9E4"),
        (5, "loc_9EC"),
        (6, "loc_9F4"),
        (7, "loc_9FC"),
        (8, "loc_A04"),
        (SWITCH_DEFAULT, "loc_A0C"),
    )


    label("loc_9C4")

    OP_22(0x118, 0x0, 0x64)
    Jump("loc_A0C")

    label("loc_9CC")

    OP_22(0x118, 0x0, 0x5A)
    Jump("loc_A0C")

    label("loc_9D4")

    OP_22(0x118, 0x0, 0x50)
    Jump("loc_A0C")

    label("loc_9DC")

    OP_22(0x118, 0x0, 0x46)
    Jump("loc_A0C")

    label("loc_9E4")

    OP_22(0x118, 0x0, 0x3C)
    Jump("loc_A0C")

    label("loc_9EC")

    OP_22(0x118, 0x0, 0x32)
    Jump("loc_A0C")

    label("loc_9F4")

    OP_22(0x118, 0x0, 0x28)
    Jump("loc_A0C")

    label("loc_9FC")

    OP_22(0x118, 0x0, 0x1E)
    Jump("loc_A0C")

    label("loc_A04")

    OP_22(0x118, 0x0, 0x14)
    Jump("loc_A0C")

    label("loc_A0C")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A0F")

    Return()

    # Function_4_82B end

    def Function_5_A10(): pass

    label("Function_5_A10")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A30")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_A30")

    FadeToDark(0, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_A53"),
        (105, "loc_ACE"),
        (107, "loc_B49"),
        (106, "loc_BC4"),
        (SWITCH_DEFAULT, "loc_BC4"),
    )


    label("loc_A53")

    SetChrPos(0x101, -21430, 10, 3270, 0)
    SetChrPos(0x103, -22780, -10, 3150, 0)
    SetChrPos(0xF8, -21320, 0, 1950, 0)
    SetChrPos(0xF9, -22600, 0, 1850, 0)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_C3F")

    label("loc_ACE")

    SetChrPos(0x101, -22600, 0, 1850, 180)
    SetChrPos(0x103, -21320, 0, 1950, 180)
    SetChrPos(0xF8, -22780, -10, 3150, 180)
    SetChrPos(0xF9, -21430, 10, 3270, 180)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_C3F")

    label("loc_B49")

    SetChrPos(0x101, -21430, 10, 3270, 90)
    SetChrPos(0x103, -21320, 0, 1950, 90)
    SetChrPos(0xF8, -22780, -10, 3150, 90)
    SetChrPos(0xF9, -22600, 0, 1850, 90)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_C3F")

    label("loc_BC4")

    SetChrPos(0x101, -22780, -10, 3150, 270)
    SetChrPos(0x103, -22600, 0, 1850, 270)
    SetChrPos(0xF8, -21430, 10, 3270, 270)
    SetChrPos(0xF9, -21320, 0, 1950, 270)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_C3F")

    label("loc_C3F")

    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x118, 0x0, 0x50)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #16
        0x101,
        (
            "#1015FHey, Schera?\x02\x03",

            "Do you get the sense the bell\x01",
            "rings are getting louder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#022FYes, I'm sure of it.\x02\x03",

            "I believe...that may be a hint.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1826)
    OP_28(0x92, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_5_A10 end

    def Function_6_D05(): pass

    label("Function_6_D05")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")
    OP_2B(0x92, 0x3)

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D32")
    Call(0, 9)
    FadeToBright(0, 0)
    Call(0, 10)

    label("loc_D32")

    FadeToDark(0, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_D55"),
        (105, "loc_DD0"),
        (107, "loc_E4B"),
        (106, "loc_EC6"),
        (SWITCH_DEFAULT, "loc_EC6"),
    )


    label("loc_D55")

    SetChrPos(0x101, -21430, 10, 3270, 0)
    SetChrPos(0x103, -22780, -10, 3150, 0)
    SetChrPos(0xF8, -21320, 0, 1950, 0)
    SetChrPos(0xF9, -22600, 0, 1850, 0)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_F41")

    label("loc_DD0")

    SetChrPos(0x101, -22600, 0, 1850, 180)
    SetChrPos(0x103, -21320, 0, 1950, 180)
    SetChrPos(0xF8, -22780, -10, 3150, 180)
    SetChrPos(0xF9, -21430, 10, 3270, 180)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_F41")

    label("loc_E4B")

    SetChrPos(0x101, -21430, 10, 3270, 90)
    SetChrPos(0x103, -21320, 0, 1950, 90)
    SetChrPos(0xF8, -22780, -10, 3150, 90)
    SetChrPos(0xF9, -22600, 0, 1850, 90)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_F41")

    label("loc_EC6")

    SetChrPos(0x101, -22780, -10, 3150, 270)
    SetChrPos(0x103, -22600, 0, 1850, 270)
    SetChrPos(0xF8, -21430, 10, 3270, 270)
    SetChrPos(0xF9, -21320, 0, 1950, 270)
    OP_6D(-22050, 0, 2480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jump("loc_F41")

    label("loc_F41")

    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 2)), scpexpr(EXPR_END)), "loc_1139")
    Sleep(500)

    ChrTalk(    #18
        0x101,
        (
            "#1007FUgh, I feel like we've been walking\x01",
            "in circles.\x02\x03",

            "#1015FWhat should we do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#522FHm.\x02\x03",

            "#022FI'm certain the volume of the bell\x01",
            "is a hint.\x02\x03",

            "If we could just understand the\x01",
            "reasoning behind how it gets louder,\x01",
            "then--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x118, 0x0, 0x64)
    OP_20(0xBB8)
    StopSound(0x64, 0x2710, 0x1770)
    Sleep(3000)

    ChrTalk(    #20
        0x101,
        "#1020FNot again!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109A")

    ChrTalk(    #21
        0x107,
        "#065FWaaaaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_109A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BC")

    ChrTalk(    #22
        0x105,
        "#043FAaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_10BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DB")

    ChrTalk(    #23
        0x104,
        "#033FOh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_10DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FB")

    ChrTalk(    #24
        0x106,
        "#057FNgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1117")

    label("loc_10FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1117")

    ChrTalk(    #25
        0x108,
        "#072FHn!\x02",
    )

    CloseMessageWindow()

    label("loc_1117")


    ChrTalk(    #26
        0x103,
        "#025F...Out of time, hmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1231")

    label("loc_1139")

    OP_22(0x118, 0x0, 0x64)
    OP_20(0xBB8)
    StopSound(0x64, 0x2710, 0x1770)
    Sleep(3000)

    ChrTalk(    #27
        0x101,
        "#1005FAGAIN?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118D")

    ChrTalk(    #28
        0x107,
        "#065FWaaaaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_118D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AE")

    ChrTalk(    #29
        0x105,
        "#043FAaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_11AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CD")

    ChrTalk(    #30
        0x104,
        "#033FOh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_11CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11ED")

    ChrTalk(    #31
        0x106,
        "#057FNgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_11ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1209")

    ChrTalk(    #32
        0x108,
        "#072FHn!\x02",
    )

    CloseMessageWindow()

    label("loc_1209")


    ChrTalk(    #33
        0x103,
        "#022FWe've escaped...but to where?\x02",
    )

    CloseMessageWindow()

    label("loc_1231")

    StopSound(0x64, 0x2710, 0x7D0)
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0303   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_6_D05 end

    def Function_7_1250(): pass

    label("Function_7_1250")

    EventBegin(0x0)
    SetChrPos(0x101, 8300, 0, 5920, 0)
    OP_6D(8300, 0, 5920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #34
        0x101,
        "#1000FWha...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(1000)

    ChrTalk(    #35
        0x101,
        (
            "#1000FWhere is...?\x02\x03",

            "Schera... Everyone...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1828)
    OP_28(0x92, 0x1, 0x20)
    OP_28(0x92, 0x1, 0x40)
    OP_28(0x92, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_7_1250 end

    def Function_8_133C(): pass

    label("Function_8_133C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1351")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1351")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1376")
    EventBegin(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1376")

    Return()

    # Function_8_133C end

    def Function_9_1377(): pass

    label("Function_9_1377")

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
            "[Set Scherazard as Partner]\x01",      # 0
            "[Set Agate as Partner]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13F7"),
        (1, "loc_13FD"),
        (SWITCH_DEFAULT, "loc_1403"),
    )


    label("loc_13F7")

    OP_A2(0x1200)
    Jump("loc_1403")

    label("loc_13FD")

    OP_A2(0x1201)
    Jump("loc_1403")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1411")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1415")

    label("loc_1411")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1415")

    Return()

    # Function_9_1377 end

    def Function_10_1416(): pass

    label("Function_10_1416")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_10_1416 end

    def Function_11_1468(): pass

    label("Function_11_1468")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_11_1468 end

    SaveToFile()

Try(main)
