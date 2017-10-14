from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C6000   ._SN',
        MapName             = 'Other',
        Location            = 'C6000.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Target',                               # 9
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 2000,
        Y                   = 4500,
        Z                   = 19500,
        Range               = 4000,
        Unknown_10          = 0x1964,
        Unknown_14          = 0x4E20,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -12900,
        Y                   = 0,
        Z                   = 2140,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 2000,
        TriggerY            = 1560,
        TriggerRange        = 1000,
        ActorX              = 2000,
        ActorZ              = 2000,
        ActorY              = 1560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5200,
        TriggerZ            = 0,
        TriggerY            = 12110,
        TriggerRange        = 1000,
        ActorX              = 5200,
        ActorZ              = 1200,
        ActorY              = 13110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_197",          # 01, 1
        "Function_2_1FC",          # 02, 2
        "Function_3_12FA",         # 03, 3
        "Function_4_138C",         # 04, 4
        "Function_5_13A8",         # 05, 5
        "Function_6_13D8",         # 06, 6
        "Function_7_13F4",         # 07, 7
        "Function_8_1424",         # 08, 8
        "Function_9_1454",         # 09, 9
        "Function_10_1484",        # 0A, 10
        "Function_11_14B4",        # 0B, 11
        "Function_12_24BD",        # 0C, 12
        "Function_13_39B4",        # 0D, 13
        "Function_14_39EB",        # 0E, 14
        "Function_15_3A22",        # 0F, 15
        "Function_16_3A59",        # 10, 16
        "Function_17_3A90",        # 11, 17
        "Function_18_3C36",        # 12, 18
        "Function_19_4488",        # 13, 19
        "Function_20_4580",        # 14, 20
        "Function_21_45D4",        # 15, 21
        "Function_22_533B",        # 16, 22
        "Function_23_5392",        # 17, 23
        "Function_24_53E4",        # 18, 24
        "Function_25_5436",        # 19, 25
        "Function_26_5488",        # 1A, 26
        "Function_27_5593",        # 1B, 27
        "Function_28_574E",        # 1C, 28
        "Function_29_57D4",        # 1D, 29
        "Function_30_5865",        # 1E, 30
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_168")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_196")

    label("loc_168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_179")
    OP_A3(0x10F1)
    Event(0, 21)
    Jump("loc_196")

    label("loc_179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_196")
    OP_A3(0x10F2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192")
    Event(0, 2)
    Jump("loc_196")

    label("loc_192")

    Event(0, 27)

    label("loc_196")

    Return()

    # Function_0_152 end

    def Function_1_197(): pass

    label("Function_1_197")

    OP_22(0x1C3, 0x1, 0x64)
    StopSound(0x124F8, 0x493E0, 0x0)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 500)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_END)), "loc_1EA")
    OP_72(0x1, 0x4)
    OP_6F(0x1, 950)
    OP_6F(0x3, 240)

    label("loc_1EA")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    Return()

    # Function_1_197 end

    def Function_2_1FC(): pass

    label("Function_2_1FC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213")
    Call(0, 28)
    Call(0, 29)

    label("loc_213")

    OP_6D(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0, 300)
    OP_48()
    OP_89(0x101, -12000, -23000, 2000, 90)
    OP_89(0x102, -13000, -23000, 3000, 90)
    OP_89(0xF8, -13000, -23000, 1000, 90)
    OP_89(0xF9, -14000, -23000, 2000, 90)
    OP_70(0x0, 0x0)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2AE():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AE)

    def lambda_2C6():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C6)
    FadeToBright(1000, 0)
    Sleep(4000)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    OP_73(0x0)
    Sleep(200)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    WaitChrThread(0xF9, 0x1)

    def lambda_378():
        OP_6D(-3930, 0, 11550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_378)

    def lambda_390():
        OP_67(0, 7500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_390)

    def lambda_3A8():
        OP_6B(3650, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A8)

    def lambda_3B8():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3B8)
    Sleep(3000)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42B")

    ChrTalk(    #0
        0x107,
        "#064FWoooooow!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_42B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_457")

    ChrTalk(    #1
        0x105,
        "#1164FHow amazing...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_457")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47C")

    ChrTalk(    #2
        0x103,
        "#023FOh, my...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_47C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A6")

    ChrTalk(    #3
        0x109,
        "#1064FSweet holy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_4A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CA")

    ChrTalk(    #4
        0x104,
        "#033FOhhhh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F2")

    label("loc_4CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F2")

    ChrTalk(    #5
        0x106,
        "#052FWell I'll be...\x02",
    )

    CloseMessageWindow()

    label("loc_4F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51D")

    ChrTalk(    #6
        0x108,
        "#072FBreathtaking...\x02",
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_51D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_553")

    ChrTalk(    #7
        0x106,
        "#555FTalk about breathtaking...\x02",
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58F")

    ChrTalk(    #8
        0x104,
        "#035FAh... What an overwhelming view!\x02",
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_58F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D5")

    ChrTalk(    #9
        0x109,
        "#1060FA city-sized piece of art, is what it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_5D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F9")

    ChrTalk(    #10
        0x103,
        "#020FAmazing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_61E")

    label("loc_5F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61E")

    ChrTalk(    #11
        0x105,
        "#1382FAstounding!\x02",
    )

    CloseMessageWindow()

    label("loc_61E")


    ChrTalk(    #12
        0x101,
        (
            "#1004F#5PThe city's...THIS big?\x02\x03",

            "#1015FHey, we're...SURE no one\x01",
            "still lives here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1035F#5PI don't think so...\x02\x03",

            "#1040FI have to imagine everyone left before\x01",
            "the city was sent to that other dimension.\x02\x03",

            "In fact, I imagine the ancestors of modern\x01",
            "Liberlians came from this place.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    def lambda_76D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76D)

    ChrTalk(    #14
        0x101,
        (
            "#1020F#2PWait, so, like, my great-great-whatevers\x01",
            "lived here?!\x02\x03",

            "And we never knew?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_891")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #15
        0x105,
        (
            "#1167FThat...actually makes some sense.\x02\x03",

            "#1162FThere have always been so few traces\x01",
            "of old Zemuria, not just in Liberl, but anywhere.\x01",
            "If the city just disappeared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_942")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #16
        0x108,
        (
            "#074FIt makes some sense.\x02\x03",

            "#072FAll across the continent, Calvard included,\x01",
            "so few traces of old Zemuria remain.\x01",
            "If their cities simply vanished...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_942")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A28")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #17
        0x104,
        (
            "#035FUpon reflection, there is a certain logic to it.\x02\x03",

            "#030FEven in Erebonia, virtually no traces remain of\x01",
            "ancient Zemuria from before the Great Collapse.\x01",
            "If a place like this city simply vanished...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_A28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF2")
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #18
        0x109,
        (
            "#1065FIf anything, it starts to add up.\x02\x03",

            "#1063FIt's always weirded people out that SO little\x01",
            "of ancient Zemuria is left. If places like\x01",
            "this just straight-up disappeared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_AF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD5")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #19
        0x103,
        (
            "#026FThinking about it, Estelle, it\x01",
            "actually makes sense.\x02\x03",

            "#022FVirtually nothing is left of the ancient Zemurian\x01",
            "culture--not just in Liberl, but everywhere.\x01",
            "Why? Well, if their cities vanished...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_BD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C93")
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #20
        0x107,
        (
            "#063FActually, Grandpa and I talked\x01",
            "about this once.\x02\x03",

            "There's barely anything left of Zemuria\x01",
            "from before the Great Collapse. If the\x01",
            "city just disappeared, then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0D")

    ChrTalk(    #21
        0x106,
        (
            "#053FRight, I get it.\x02\x03",

            "#050FThey lived up in the sky, and then\x01",
            "their home in the sky goes 'poof'...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1063")

    label("loc_D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA9")

    ChrTalk(    #22
        0x107,
        (
            "#065FI get it, that explains what Grandpa's\x01",
            "always wondered...\x02\x03",

            "If everyone used to live in the sky,\x01",
            "and the city just disappeared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1063")

    label("loc_DA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E50")

    ChrTalk(    #23
        0x103,
        (
            "#026FRight, now I see.\x02\x03",

            "#022FThere wouldn't be much to leave behind\x01",
            "if they lived in the sky and then their\x01",
            "living space vanished like the wind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1063")

    label("loc_E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(    #24
        0x109,
        (
            "#1068FAhhh, right, I get it.\x02\x03",

            "#1060FThey didn't leave anything behind 'cause, hey,\x01",
            "livin' in the sky, you don't leave much on the\x01",
            "ground! Then hey presto, your city disappears!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1063")

    label("loc_F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCE")

    ChrTalk(    #25
        0x104,
        (
            "#035FAh, of course.\x02\x03",

            "#030FThose who live in the sky would not leave traces\x01",
            "upon the ground...and then their home in the\x01",
            "clouds is removed from this mortal coil.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1063")

    label("loc_FCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1063")

    ChrTalk(    #26
        0x108,
        (
            "#074FI see.\x02\x03",

            "#070FIf the ancients lived in the sky prior to\x01",
            "their exodus, they would leave little\x01",
            "upon the ground for us to find.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1063")


    ChrTalk(    #27
        0x101,
        (
            "#1007F#2PThis place seems to get crazier\x01",
            "with every step we take!\x02\x03",

            "#1017FAnyway. The view here is really pretty,\x01",
            "but what is this place, you think?\x01",
            "It feels different from the rest of the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1043F#5PGiven the nature of this area so far,\x01",
            "it may just be a scenic view, but it does\x01",
            "feel...a bit more important. Hmm...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11B2():
        OP_6D(-2200, 0, 8670, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11B2)

    def lambda_11CA():
        OP_67(0, 6140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11CA)
    OP_8C(0x102, 135, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #29
        0x102,
        (
            "#1040F#6PThat screen over there looks like something\x01",
            "you're meant to interact with.\x01",
            "Let's take a look at it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-3950, 0, 6730, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, -3950, 0, 6730, 225)
    SetChrPos(0x1, -3950, 0, 6730, 225)
    SetChrPos(0x2, -3950, 0, 6730, 225)
    SetChrPos(0x3, -3950, 0, 6730, 225)
    Sleep(500)
    OP_A2(0x2203)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_1FC end

    def Function_3_12FA(): pass

    label("Function_3_12FA")


    def lambda_1300():
        OP_6D(-7380, 0, 2100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1300)
    OP_8E(0xFE, 0xFFFFE958, 0x0, 0x884, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(18150, 5000, 23940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4990, 0)
    OP_6C(0, 0)
    OP_6E(267, 0)
    Return()

    # Function_3_12FA end

    def Function_4_138C(): pass

    label("Function_4_138C")

    OP_8E(0xFE, 0xFFFFF1AA, 0x0, 0x2486, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_138C end

    def Function_5_13A8(): pass

    label("Function_5_13A8")

    OP_8E(0xFE, 0xFFFFD5F8, 0xA, 0x708, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE44E, 0x0, 0x802, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_13A8 end

    def Function_6_13D8(): pass

    label("Function_6_13D8")

    OP_8E(0xFE, 0xFFFFED90, 0x0, 0x210C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_13D8 end

    def Function_7_13F4(): pass

    label("Function_7_13F4")

    OP_8E(0xFE, 0xFFFFD5F8, 0xA, 0x708, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0xAA, 0x780, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_13F4 end

    def Function_8_1424(): pass

    label("Function_8_1424")

    OP_8E(0xFE, 0xFFFFE520, 0x0, 0x816, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF498, 0x0, 0x1EA0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_1424 end

    def Function_9_1454(): pass

    label("Function_9_1454")

    OP_8E(0xFE, 0xFFFFD5F8, 0xA, 0x708, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDBA2, 0xC8, 0x762, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_1454 end

    def Function_10_1484(): pass

    label("Function_10_1484")

    OP_8E(0xFE, 0xFFFFE520, 0x0, 0x816, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x0, 0x1AE0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_1484 end

    def Function_11_14B4(): pass

    label("Function_11_14B4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D9")
    Call(0, 28)
    Call(0, 29)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_14D9")

    Fade(500)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #30
        (
            "\x07\x05#1SHalo Rail, West Calmare Station\x01",
            "The Halo Rail system is currently operating at limited\x01",
            "capacity. We apologize for the inconvenience.\x01",
            "Please select a service from this terminal.\x01",
            "Gospel-based citizen ID checks are not required\x01",
            "for service at this time.\x01\x01",
            "- Liber Ark Transit Authority\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#1020F#2PHmm...\x02\x03",

            "What's a Halo Rail system? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1035F#1PSome kind of rail-based transit system,\x01",
            "I guess.\x02\x03",

            "#1040FAnd given that there's a 'Transit Authority'\x01",
            "involved, I would guess this floating island\x01",
            "is called the 'Liber Ark.'\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #33
        0x101,
        (
            "#1004F#2POh, yeah. The Liber Ark... Hang on.\x01",
            "'Liber'? No way!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184D")

    ChrTalk(    #34
        0x105,
        (
            "#1382F'Way,' I think. We've just discovered\x01",
            "the origin of the name of Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_184D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18A5")

    ChrTalk(    #35
        0x104,
        (
            "#035FIndeed. We have discovered the\x01",
            "origin of the name of Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_18A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F9")

    ChrTalk(    #36
        0x103,
        (
            "#027FI think so. This must be where\x01",
            "Liberl got its name from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_18F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1957")

    ChrTalk(    #37
        0x108,
        (
            "#070FI think you're right. This must be\x01",
            "where Liberl got its name from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_1957")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B4")

    ChrTalk(    #38
        0x109,
        (
            "#1060FYou're right on, I bet! This is where\x01",
            "Liberl gets its name from!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_19B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A05")

    ChrTalk(    #39
        0x106,
        (
            "#051FNah, I think so. This must be\x01",
            "where 'Liberl' comes from.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A05")


    ChrTalk(    #40
        0x101,
        "#1015F#2PHoly Stregas...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #41
        0x102,
        (
            "#1042F#1PPersonally, I find the Gospel reference\x01",
            "more interesting.\x02\x03",

            "From the way this is written, they must have\x01",
            "been ubiquitous. Everyone would have had one.\x02\x03",

            "#1043FIt sounds like they served as identification...\x01",
            "and a portable, personal link to the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1007F#2PGraah, this is too much to take in\x01",
            "at once!\x02\x03",

            "#1006FAnyway, it looks like we don't need\x01",
            "a Gospel to do stuff here.\x02\x03",

            "Let's see what we can do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#1040F#1PRight. I think I can get it to list\x01",
            "available services if I push...this?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_A2(0x2204)
    SetMessageWindowPos(300, 78, 34, 12)

    AnonymousTalk(    #44
        "\x07\x05\x02",
    )

    Jump("loc_1D90")

    label("loc_1C5B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    AnonymousTalk(    #45
        (
            "\x07\x05#1SHalo Rail, West Calmare Station\x01",
            "The Halo Rail system is currently operating at limited\x01",
            "capacity. We apologize for the inconvenience.\x01",
            "Please select a service from this terminal.\x01",
            "Gospel-based citizen ID checks are not required\x01",
            "for service at this time.\x01\x01",
            "- Liber Ark Transit Authority\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_240F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        100,
        1,
        (
            "Calmare District Information\x01",       # 0
            "Halo Rail Service Information\x01",      # 1
            "Online Shop\x01",                        # 2
            "Gate Lock Release\x01",                  # 3
            "Cease Service\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E40"),
        (1, "loc_20BF"),
        (2, "loc_2213"),
        (3, "loc_223D"),
        (4, "loc_23F2"),
        (SWITCH_DEFAULT, "loc_23FF"),
    )


    label("loc_1E40")

    OP_56(0x0)

    AnonymousTalk(    #46
        (
            "\x07\x05#1SBuilt as the ultimate in rest and relaxation for the\x01",
            "citizens of the Ark, the Calmare district is Liber Ark's\x01",
            "premiere park and recreation district, located in the west\x01",
            "of the city. Each section of the park, designed around the\x01",
            "theme of 'harmony between progress and nature,' is a hexagon\x01",
            "exactly 300 arge across. Calmare as a whole is made up of\x01",
            "dozens of dozens of these hexagons.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #47
        (
            "\x07\x05#1SThe Calmare District has four Halo Rail stations--\x01",
            "North, South, East and West.\x01\x01",
            "Each station's tour path routes through different sections\x01",
            "of Calmare, allowing one to enjoy vistas of all the seasons\x01",
            "and wildlife Calmare has to offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240C")

    label("loc_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219F")
    OP_56(0x0)

    AnonymousTalk(    #48
        (
            "\x07\x05#1SHalo Rail service is currently limited.\x01",
            "Would you like to activate Emergency Operation Mode\x01",
            "for West Calmare Station?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            "Activate\x01",             # 0
            "Do Not Activate\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_217D"),
        (1, "loc_2196"),
        (SWITCH_DEFAULT, "loc_219C"),
    )


    label("loc_217D")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Call(0, 12)
    Return()

    label("loc_2196")

    OP_5F(0x1)
    Jump("loc_219C")

    label("loc_219C")

    Jump("loc_2210")

    label("loc_219F")

    OP_56(0x0)

    AnonymousTalk(    #49
        (
            "\x07\x05#1SHalo Rail service is currently limited.\x01",
            "West Calmare Station is currently in Emergency Operation\x01",
            "Mode.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2210")

    Jump("loc_240C")

    label("loc_2213")

    FadeToBright(300, 0)

    AnonymousTalk(    #50
        "\x07\x05\x02",
    )

    OP_A9(0xF0)

    AnonymousTalk(    #51
        "\x07\x05        \x02",
    )

    FadeToDark(300, 0, 100)
    Jump("loc_240C")

    label("loc_223D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23AD")
    OP_56(0x0)

    AnonymousTalk(    #52
        (
            "\x07\x05#1SIn the event of service disruption of the Halo Rail, a gate\x01",
            "may be unlocked at each station, leading to substratum\x01",
            "access passages. In accordance with emergency protocols,\x01",
            "this station's gate can be unlocked.\x01\x01",
            "Would you like to do so at this time?\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            "Unlock\x01",             # 0
            "Do Not Unlock\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2379"),
        (1, "loc_23A4"),
        (SWITCH_DEFAULT, "loc_23AA"),
    )


    label("loc_2379")

    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5901   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_23AA")

    label("loc_23A4")

    OP_5F(0x1)
    Jump("loc_23AA")

    label("loc_23AA")

    Jump("loc_23EF")

    label("loc_23AD")

    OP_56(0x0)

    AnonymousTalk(    #53
        "\x07\x05#1SThe West Calmare Substratum Gate is currently unlocked.\x02",
    )

    CloseMessageWindow()

    label("loc_23EF")

    Jump("loc_240C")

    label("loc_23F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_240C")

    label("loc_23FF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_240C")

    label("loc_240C")

    Jump("loc_1D9A")

    label("loc_240F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(100, 0)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    EventEnd(0x0)
    Return()

    # Function_11_14B4 end

    def Function_12_24BD(): pass

    label("Function_12_24BD")

    EventBegin(0x0)
    OP_72(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324C")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_2539():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2539)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0x101,
        "#1004F#6PHey, what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#1044F#6PThere's something coming.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_2637():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2637)

    def lambda_264F():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_264F)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_267A():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_267A)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(500)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #56
        0x101,
        "#1004F#5PWhat in the world?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2778")

    ChrTalk(    #57
        0x102,
        (
            "#1040F#5PLooks like this is a Halo Rail car.\x02\x03",

            "I wonder how that rail works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_2778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E7")

    ChrTalk(    #58
        0x10F,
        (
            "#173FThis must be a car for the Halo Rail.\x02\x03",

            "#178FI can't help but wonder how it works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_27E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2869")

    ChrTalk(    #59
        0x105,
        (
            "#1165F#5PThis must be a car for the Halo Rail.\x02\x03",

            "#1382FYou, um, have to wonder how it\x01",
            "works without, well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_2869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28CF")

    ChrTalk(    #60
        0x103,
        (
            "#026F#5PThis must be a car for the Halo Rail.\x02\x03",

            "#020FI do wonder how it works...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_28CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_294C")

    ChrTalk(    #61
        0x106,
        (
            "#053F#5PIf I had to guess, this is a Halo Rail car.\x02\x03",

            "#555FNot sure how the 'rail' bit works, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_294C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BB")

    ChrTalk(    #62
        0x108,
        (
            "#074F#5PHmmm. This must be a car for the Halo Rail.\x02\x03",

            "#070FI wonder how the 'rail' works.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_29BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A2A")

    ChrTalk(    #63
        0x109,
        (
            "#1064F#5PHuh. The Halo Rail, I presume!\x02\x03",

            "#1068FI'm kinda lost on how it works, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_2A2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A94")

    ChrTalk(    #64
        0x104,
        (
            "#035F#5PAh, this must be a car for the Halo Rail.\x02\x03",

            "#030FThose rails... Fascinating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AED")

    label("loc_2A94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AED")

    ChrTalk(    #65
        0x10B,
        (
            "#216F#5PWait, THIS is the Halo Rail?\x02\x03",

            "But, but, the rails! The RAILS!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BC2")

    ChrTalk(    #66
        0x110,
        (
            "#278FIt seems fundamentally similar to inter-city light\x01",
            "rail systems you find in major Imperial cities.\x02\x03",

            "#277FGranted, in the Empire we rather tend\x01",
            "to not make the rails out of actual light.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2BC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C65")

    ChrTalk(    #67
        0x10B,
        (
            "#213F#5PI see. It really is just like trains back home!\x02\x03",

            "#413FNot sure how okay I am with the idea\x01",
            "of riding on rails made of AIR, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2C65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3D")

    ChrTalk(    #68
        0x104,
        (
            "#030F#5PIt's very similar to the light rail systems\x01",
            "used throughout Erebonia, as I thought.\x02\x03",

            "#031FAh, to make the rails out of actual light!\x01",
            "The ancients knew the value of spectacle.\x01",
            "And humor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E02")

    ChrTalk(    #69
        0x109,
        (
            "#1064F#5PI see, it's like the train systems you find\x01",
            "in places like Erebonia.\x02\x03",

            "#1068FDon't think I've ever seen 'light rail'\x01",
            "taken to this extreme before, though.\x01",
            "No siree...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2E02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9A")

    ChrTalk(    #70
        0x108,
        (
            "#073F#5PAh, I see. It runs on rails a bit\x01",
            "like a mine cart.\x02\x03",

            "#075FI'm not sure how to feel about the\x01",
            "transparent rails, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F47")

    ChrTalk(    #71
        0x106,
        (
            "#555F#5PLooks a lot like the train systems\x01",
            "the Imperials use.\x02\x03",

            "#551F'Course, the Imperials aren't crazy enough\x01",
            "to try and make rails out of nothin'...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2F47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE5")

    ChrTalk(    #72
        0x103,
        (
            "#020F#5PAh, so it's like the Erebonian train\x01",
            "system. I see.\x02\x03",

            "#524FI...have to wonder just how safe a\x01",
            "rail made out of light is, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_2FE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307A")

    ChrTalk(    #73
        0x105,
        (
            "#1164F#5PIt seems to be an advanced version of\x01",
            "the trains which run throughout Erebonia.\x02\x03",

            "I wonder what the rails are made of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E4")

    label("loc_307A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30E4")

    ChrTalk(    #74
        0x10F,
        (
            "#176FIt seems similar to Imperial trains.\x02\x03",

            "#178FI'm unsure about the rails, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_318A")

    ChrTalk(    #75
        0x107,
        (
            "#064F#5PWooooooooooooooow...\x01",
            "It uses a projected force field in\x01",
            "place of a solid rail!\x02\x03",

            "#067FThat... That's the most amazing\x01",
            "thing I've ever seen!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_318A")


    ChrTalk(    #76
        0x101,
        (
            "#1006F#5PIt all feels a little over my head, but if\x01",
            "it'll get us where we need to go without\x01",
            "dropping us into the clouds, I'm all for it!\x02\x03",

            "#1018FC'mon, let's hop on and try it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2205)
    OP_28(0x9D, 0x1, 0x20)
    Jump("loc_390E")

    label("loc_324C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C4")
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_32BC():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_32BC)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()

    ChrTalk(    #77
        0x101,
        "#1006F#6PHere it comes!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_338E():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_338E)

    def lambda_33A6():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33A6)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_33D1():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33D1)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #78
        0x101,
        (
            "#1006F#5PSo we should finally be able\x01",
            "to use these things, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#1040F#5PI think so.\x01",
            "Let's get on and try.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220A)
    Jump("loc_390E")

    label("loc_34C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D6")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_3539():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3539)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_35A6():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35A6)

    def lambda_35BE():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35BE)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_35E9():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_35E9)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #80
        0x101,
        (
            "#1015F#5PLet's see, we can use three\x01",
            "stations now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1040F#5PYes. This makes things much easier.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x220B)
    Jump("loc_390E")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390E")
    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x8, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    Sleep(500)

    def lambda_374B():
        OP_6D(17390, 5000, 16010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_374B)
    OP_22(0x13D, 0x0, 0x64)
    OP_73(0x3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_37B8():
        OP_6D(3080, 5110, 21340, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37B8)

    def lambda_37D0():
        OP_67(0, 6030, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37D0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_37FB():
        OP_8E(0xFE, 0xC44, 0x13F6, 0x523A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_37FB)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    OP_73(0x1)
    OP_23(0x13E)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)

    ChrTalk(    #82
        0x102,
        (
            "#1035F#5PAll right...\x02\x03",

            "#1040FNow we can easily go everywhere,\x01",
            "from Calmare to the Axis Pillar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1007F#5P*pheeeew* That was a bit of work.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x220C)
    OP_28(0x9F, 0x1, 0x2)

    label("loc_390E")

    OP_A2(0x2206)
    OP_28(0x9D, 0x1, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3060, 5000, 18520, 0)
    SetChrPos(0x1, 3060, 5000, 18520, 0)
    SetChrPos(0x2, 3060, 5000, 18520, 0)
    SetChrPos(0x3, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_12_24BD end

    def Function_13_39B4(): pass

    label("Function_13_39B4")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xA3C, 0x1388, 0x47B8, 0x1388, 0x0)

    def lambda_39DF():

        label("loc_39DF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_39DF")

    QueueWorkItem2(0xFE, 2, lambda_39DF)
    Return()

    # Function_13_39B4 end

    def Function_14_39EB(): pass

    label("Function_14_39EB")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xE2E, 0x1388, 0x47CC, 0x1388, 0x0)

    def lambda_3A16():

        label("loc_3A16")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A16")

    QueueWorkItem2(0xFE, 2, lambda_3A16)
    Return()

    # Function_14_39EB end

    def Function_15_3A22(): pass

    label("Function_15_3A22")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0x8C0, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_3A4D():

        label("loc_3A4D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A4D")

    QueueWorkItem2(0xFE, 2, lambda_3A4D)
    Return()

    # Function_15_3A22 end

    def Function_16_3A59(): pass

    label("Function_16_3A59")

    SetChrPos(0xFE, 13930, 4000, 17320, 270)
    OP_8E(0xFE, 0xFE6, 0x1388, 0x4326, 0x1388, 0x0)

    def lambda_3A84():

        label("loc_3A84")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A84")

    QueueWorkItem2(0xFE, 2, lambda_3A84)
    Return()

    # Function_16_3A59 end

    def Function_17_3A90(): pass

    label("Function_17_3A90")

    EventBegin(0x0)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2480, 2000, 500, 0)
    SetChrPos(0x102, 1480, 2000, 500, 0)
    SetChrPos(0xF8, 2450, 1600, -1400, 0)
    SetChrPos(0xF9, 1560, 1600, -1220, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #84
        "\x07\x05Locks on gate in station vicinity have been removed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #85
        "\x07\x05Tunnel #78 is now usable.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, 2020, 2000, 40, 180)
    SetChrPos(0x1, 2020, 2000, 40, 180)
    SetChrPos(0x2, 2020, 2000, 40, 180)
    SetChrPos(0x3, 2020, 2000, 40, 180)
    OP_0D()
    OP_A2(0x220D)
    OP_28(0x9D, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_17_3A90 end

    def Function_18_3C36(): pass

    label("Function_18_3C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3F")
    Return()

    label("loc_3C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C6")
    EventBegin(0x0)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2620, 5000, 18360, 0)
    SetChrPos(0x102, 3630, 5000, 18380, 0)
    SetChrPos(0xF8, 2240, 5000, 17190, 0)
    SetChrPos(0xF9, 4070, 5000, 17190, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #86
        (
            "\x07\x05Currently, no other stations are operating in\x01",
            "Emergency Operations Mode.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Machine Voice")

    AnonymousTalk(    #87
        (
            "\x07\x05We are sorry, but the Halo Rail service is not currently\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DFD")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E31")

    label("loc_3DFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1F")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E31")

    label("loc_3E1F")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3E31")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E58")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E8C")

    label("loc_3E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7A")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3E8C")

    label("loc_3E7A")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3E8C")

    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0xF8)
    OP_63(0xF9)
    Sleep(500)

    ChrTalk(    #88
        0x101,
        (
            "#1019F#5P...Real informative.\x01",
            "Thanks, Creepy Disembodied Voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#1035F#5PIt sounds like the other stations need to be in\x01",
            "this 'Emergency Operations Mode' if we intend to\x01",
            "get around.\x02\x03",

            "#1040FFor now, I'm afraid the 'Halo Rail'\x01",
            "isn't of much use to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1007F#5PNuts. And here I was, getting hopeful for once.\x02\x03",

            "#1015FWell, let's see if we can\x01",
            "find another way around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x220E)
    OP_28(0x9D, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3060, 5000, 18520, 0)
    SetChrPos(0x1, 3060, 5000, 18520, 0)
    SetChrPos(0x2, 3060, 5000, 18520, 0)
    SetChrPos(0x3, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_41AE")

    label("loc_40C6")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Machine Voice")

    AnonymousTalk(    #91
        (
            "\x07\x05Currently, no other stations are operating in\x01",
            "Emergency Operations Mode.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Machine Voice")

    AnonymousTalk(    #92
        (
            "\x07\x05We are sorry, but the Halo Rail service is not currently\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_41AE")

    Jump("loc_4487")

    label("loc_41B1")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2620, 5000, 18360, 0)
    SetChrPos(0x102, 3630, 5000, 18380, 0)
    SetChrPos(0xF8, 2240, 5000, 17190, 0)
    SetChrPos(0xF9, 4070, 5000, 17190, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 7)), scpexpr(EXPR_END)), "loc_4290")
    OP_CC(0x1, 0x0, "Cradle Station #35")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 0)), scpexpr(EXPR_END)), "loc_42B9")
    OP_CC(0x1, 0x0, "Factoria Station #7 ")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_42B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 1)), scpexpr(EXPR_END)), "loc_42E1")
    OP_CC(0x1, 0x0, "Axis Pillar Station")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_42E1")

    OP_CC(0x1, 0x0, "Quit")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_431C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_439E")

    label("loc_431C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4326")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4340")
    Jump("loc_439E")

    label("loc_4340")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4391")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_437A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4377")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4377")

    Jump("loc_4391")

    label("loc_437A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4340")

    label("loc_4391")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4326")

    label("loc_439E")

    SetMapFlags(0x100000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_43BC"),
        (1, "loc_43FA"),
        (2, "loc_4438"),
        (3, "loc_4476"),
        (SWITCH_DEFAULT, "loc_4479"),
    )


    label("loc_43BC")

    OP_A2(0x2210)
    OP_A2(0x2215)
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_43CF():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_43CF)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4479")

    label("loc_43FA")

    OP_A2(0x2210)
    OP_A2(0x2216)
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_440D():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_440D)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4479")

    label("loc_4438")

    OP_A2(0x2210)
    OP_A2(0x2217)
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_444B():
        OP_67(0, 5450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_444B)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4479")

    label("loc_4476")

    Jump("loc_4479")

    label("loc_4479")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    EventEnd(0x0)

    label("loc_4487")

    Return()

    # Function_18_3C36 end

    def Function_19_4488(): pass

    label("Function_19_4488")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_43(0x101, 0x2, 0x0, 0x14)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x14)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    Sleep(1500)
    OP_6F(0x1, 950)
    OP_70(0x1, 0x44C)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 7)), scpexpr(EXPR_END)), "loc_4534")
    OP_6F(0x1, 1100)
    OP_70(0x1, 0x514)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_44FF():
        OP_6D(8300, 5000, 21350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44FF)

    def lambda_4517():
        OP_6C(12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4517)

    def lambda_4527():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4527)
    Jump("loc_456F")

    label("loc_4534")

    OP_6F(0x1, 300)
    OP_70(0x1, 0x1F4)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_454D():
        OP_6D(-2860, 5000, 21710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_454D)

    def lambda_4565():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4565)

    label("loc_456F")

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_19_4488 end

    def Function_20_4580(): pass

    label("Function_20_4580")

    OP_8E(0xFE, 0xC08, 0x1388, 0x4A56, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x13F6, 0x4F6A, 0x7D0, 0x0)

    def lambda_45AE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_45AE)
    OP_8E(0xFE, 0xC1C, 0x13F6, 0x5E9C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_4580 end

    def Function_21_45D4(): pass

    label("Function_21_45D4")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(3100, 5110, 23900, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3050, 5110, 21510, 180)
    SetChrPos(0x102, 3050, 5110, 21510, 180)
    SetChrPos(0xF8, 3050, 5110, 21510, 180)
    SetChrPos(0xF9, 3050, 5110, 21510, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x442, 1)), scpexpr(EXPR_END)), "loc_46DD")
    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x320)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_46C8():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_46C8)
    Jump("loc_4755")

    label("loc_46DD")

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_22(0x13E, 0x0, 0x64)

    def lambda_4733():
        OP_6D(2890, 5000, 22450, 5500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4733)

    def lambda_474B():
        OP_6C(0, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_474B)

    label("loc_4755")

    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    FadeToBright(1000, 0)
    OP_73(0x1)
    OP_23(0x13E)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x3B6)
    Sleep(300)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x441, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5231")
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x17)
    Sleep(800)

    def lambda_47B1():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47B1)

    def lambda_47C9():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_47C9)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #93
        0x101,
        "#1004F#2PWhoaaaaaa, that didn't take very long!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#1035F#5PFor as fast as it went, there was barely\x01",
            "any vibration or unsteadiness, either.\x02\x03",

            "#1040FTo be honest, this technology is a bit\x01",
            "mind-blowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1015F#2PNo kidding. Still...\x02\x03",

            "#1016FAs nice as it is to go fast, the view was\x01",
            "amazing, too. I kinda wish it went a\x01",
            "bit slower so you could enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F0")

    ChrTalk(    #96
        0x10B,
        (
            "#413FIt'd be a tourist attraction in that case,\x01",
            "not a train system. Duh.\x02\x03",

            "#210FIt IS kinda a waste of a good view,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_49F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A21")

    ChrTalk(    #97
        0x107,
        "#067FHeehee! It is, sorta.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4A21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A59")

    ChrTalk(    #98
        0x105,
        "#1168FHaha. It is, unfortunately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A93")

    ChrTalk(    #99
        0x103,
        "#021FAhh, the perils of technology.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ACA")

    ChrTalk(    #100
        0x109,
        "#1061FHaha! Yeah, unfortunately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B01")

    ChrTalk(    #101
        0x104,
        "#031FHaha! Lamentable, but true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4B01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B34")

    ChrTalk(    #102
        0x10F,
        "#171FHah... I suppose it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B69")

    ChrTalk(    #103
        0x108,
        "#071FHaha! Unfortunately, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B91")

    label("loc_4B69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B91")

    ChrTalk(    #104
        0x106,
        "#051FHeh, I suppose.\x02",
    )

    CloseMessageWindow()

    label("loc_4B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C52")

    ChrTalk(    #105
        0x110,
        (
            "#278FFar more important is how much easier\x01",
            "this will make our investigations.\x02\x03",

            "#277FI would recommend making the discovery of\x01",
            "these stations a top priority in a new area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_4C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CF7")

    ChrTalk(    #106
        0x106,
        (
            "#051FMore importantly, this'll make gettin'\x01",
            "around a hell of a lot easier.\x02\x03",

            "We should try 'n find these stations\x01",
            "as soon as we hit a new area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_4CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D87")

    ChrTalk(    #107
        0x108,
        (
            "#070FThis makes getting around the\x01",
            "city quite a bit easier.\x02\x03",

            "We should try and find the other\x01",
            "stations as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_4D87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E4B")

    ChrTalk(    #108
        0x10F,
        (
            "#179FI'm more impressed with what this does\x01",
            "to the speed at which we can investigate.\x02\x03",

            "#170FI think it would be wise to make finding\x01",
            "these stations a priority going forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_4E4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F12")

    ChrTalk(    #109
        0x104,
        (
            "#035FHeh, and of course, this also solves\x01",
            "the travel problems we have had.\x02\x03",

            "#030FIt would behoove us to locate the local\x01",
            "rail station as soon as we enter a new\x01",
            "area, I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_4F12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FC8")

    ChrTalk(    #110
        0x109,
        (
            "#1060FI kinda think the important bit is what\x01",
            "this does to the speed at which we can\x01",
            "get around.\x02\x03",

            "We oughtta try and find the other\x01",
            "stations as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_4FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50A5")

    ChrTalk(    #111
        0x103,
        (
            "#027FI'm more impressed with how\x01",
            "this improves our ability to get around.\x02\x03",

            "It's just a suggestion from the itinerant\x01",
            "circus girl, but we may just want to focus\x01",
            "on finding the rest of these stations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_50A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5180")

    ChrTalk(    #112
        0x105,
        (
            "#1167FAnd in addition to the view, this also\x01",
            "allows us to travel across the Ark\x01",
            "incredibly quickly.\x02\x03",

            "#1168FI think it would be a good idea to find\x01",
            "the other stations as soon as we enter\x01",
            "new areas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522B")

    label("loc_5180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_522B")

    ChrTalk(    #113
        0x107,
        (
            "#061FHeehee, yeah, and it lets us get around\x01",
            "really fast too! ♪\x02\x03",

            "#560FI think we should try and find the other\x01",
            "stations as soon as we find a new area!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_522B")

    OP_A2(0x220F)
    Jump("loc_5289")

    label("loc_5231")

    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x17)
    Sleep(800)

    def lambda_524F():
        OP_6D(3100, 5000, 18850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_524F)

    def lambda_5267():
        OP_6B(4000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5267)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    Sleep(500)

    label("loc_5289")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrPos(0x0, 3060, 5000, 18520, 180)
    SetChrPos(0x1, 3060, 5000, 18520, 180)
    SetChrPos(0x2, 3060, 5000, 18520, 180)
    SetChrPos(0x3, 3060, 5000, 18520, 180)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x100000)
    Return()

    # Function_21_45D4 end

    def Function_22_533B(): pass

    label("Function_22_533B")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5351():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5351)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xECE, 0x1388, 0x4376, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x80)
    Return()

    # Function_22_533B end

    def Function_23_5392(): pass

    label("Function_23_5392")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_53A8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53A8)
    OP_8E(0xFE, 0xC1C, 0x1388, 0x49DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9F6, 0x1388, 0x4362, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_5392 end

    def Function_24_53E4(): pass

    label("Function_24_53E4")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_53FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53FA)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1086, 0x1388, 0x4808, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_24_53E4 end

    def Function_25_5436(): pass

    label("Function_25_5436")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_544C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_544C)
    OP_8E(0xFE, 0xC58, 0x1388, 0x4AB0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7B2, 0x1388, 0x47A4, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_25_5436 end

    def Function_26_5488(): pass

    label("Function_26_5488")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-13000, 0, 2000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_89(0x101, -12000, 0, 2000, 90)
    OP_89(0x102, -13000, 0, 3000, 90)
    OP_89(0xF8, -13000, 0, 1000, 90)
    OP_89(0xF9, -14000, 0, 2000, 90)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x4B0)

    def lambda_5534():
        OP_6D(-13000, -25000, 490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5534)

    def lambda_554C():
        OP_67(0, 3890, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_554C)

    def lambda_5564():
        OP_6B(5200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5564)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    Sleep(500)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5901   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_26_5488 end

    def Function_27_5593(): pass

    label("Function_27_5593")

    EventBegin(0x0)
    OP_6D(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0, 300)
    OP_48()
    OP_89(0x101, -12000, -23000, 2000, 90)
    OP_89(0x102, -13000, -23000, 3000, 90)
    OP_89(0xF8, -13000, -23000, 1000, 90)
    OP_89(0xF9, -14000, -23000, 2000, 90)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_70(0x0, 0x0)

    def lambda_5639():
        OP_6D(-13000, 0, 2000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5639)

    def lambda_5651():
        OP_67(0, 3880, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5651)
    Sleep(4000)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    OP_73(0x0)
    Sleep(200)
    Fade(500)
    OP_6D(-7000, 0, 2000, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0, -7000, 0, 2000, 90)
    SetChrPos(0x1, -7000, 0, 2000, 90)
    SetChrPos(0x2, -7000, 0, 2000, 90)
    SetChrPos(0x3, -7000, 0, 2000, 90)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_27_5593 end

    def Function_28_574E(): pass

    label("Function_28_574E")

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
        (0, "loc_57C7"),
        (1, "loc_57CD"),
        (SWITCH_DEFAULT, "loc_57D3"),
    )


    label("loc_57C7")

    OP_A2(0x1200)
    Jump("loc_57D3")

    label("loc_57CD")

    OP_A2(0x1201)
    Jump("loc_57D3")

    label("loc_57D3")

    Return()

    # Function_28_574E end

    def Function_29_57D4(): pass

    label("Function_29_57D4")

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

    # Function_29_57D4 end

    def Function_30_5865(): pass

    label("Function_30_5865")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #114
        "\x07\x05Platform This Way⇒ West Calmare Station\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_5865 end

    SaveToFile()

Try(main)
