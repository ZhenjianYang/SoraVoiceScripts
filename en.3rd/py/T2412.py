from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2412   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2412.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Matron Theresa',                       # 9
        'Target Camera',                        # 10
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
        'ED6_DT07/CH02570 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 0,
        Y                   = 14280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        "Function_0_F2",           # 00, 0
        "Function_1_168",          # 01, 1
        "Function_2_169",          # 02, 2
        "Function_3_2E6",          # 03, 3
        "Function_4_A08",          # 04, 4
        "Function_5_101D",         # 05, 5
        "Function_6_1082",         # 06, 6
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_101")
    SetChrFlags(0x10, 0x80)
    Jump("loc_14F")

    label("loc_101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_11C")
    SetChrPos(0x10, 32940, 0, -34330, 262)
    Jump("loc_14F")

    label("loc_11C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_137")
    SetChrPos(0x10, -3000, 0, 14280, 0)
    Jump("loc_14F")

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_14F")
    SetChrPos(0x10, -3000, 0, 14280, 0)

    label("loc_14F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167")
    Event(0, 4)

    label("loc_167")

    Return()

    # Function_0_F2 end

    def Function_1_168(): pass

    label("Function_1_168")

    Return()

    # Function_1_168 end

    def Function_2_169(): pass

    label("Function_2_169")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2D0")

    label("loc_18E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2D0")

    label("loc_1A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2D0")

    label("loc_1C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2D0")

    label("loc_1D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2D0")

    label("loc_1F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2D0")

    label("loc_20B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2D0")

    label("loc_224")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2D0")

    label("loc_23D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2D0")

    label("loc_256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2D0")

    label("loc_26F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2D0")

    label("loc_288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2D0")

    label("loc_2A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2D0")

    label("loc_2BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2D0")

    label("loc_2E5")

    Return()

    # Function_2_169 end

    def Function_3_2E6(): pass

    label("Function_3_2E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_65B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E5, 1)), scpexpr(EXPR_END)), "loc_481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_387")

    ChrTalk(    #0
        0x10,
        (
            "#750FMaybe I should tidy up my room today, too.\x02\x03",

            "#751FMaybe I'll even end up finding something that\x01",
            "could be sold at the bazaar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47E")

    label("loc_387")


    ChrTalk(    #1
        0x10,
        (
            "#750FI thought it would be a good idea to search\x01",
            "for things that could be sold at the bazaar\x01",
            "while tidying up...\x02\x03",

            "#751FHeehee. But I just can't bring myself to part\x01",
            "with anything. Everything here has memories\x01",
            "attached to it, big or small.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_47E")

    Jump("loc_658")

    label("loc_481")


    ChrTalk(    #2
        0x14E,
        (
            "#1714FMatron, you don't need to clean up our room!\x01",
            "I'll do--\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E5, 0)), scpexpr(EXPR_END)), "loc_557")

    ChrTalk(    #3
        0x10,
        (
            "#750FOh, but I thought I told you to take the day off?\x02\x03",

            "Please, just go and have a bit of fun playing.\x01",
            "I can handle tidying up here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61D")

    label("loc_557")


    ChrTalk(    #4
        0x10,
        (
            "#750FIt's quite all right, Mary.\x02\x03",

            "I appreciate you helping out all the time, but\x01",
            "I want you to be able to enjoy playing once in\x01",
            "a while.\x02\x03",

            "It's a lovely day so why not have some fun in\x01",
            "the sun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D")

    TurnDirection(0x10, 0x14F, 400)

    ChrTalk(    #5
        0x10,
        "#751FWith Polly, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x14F,
        "#1732FYay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F29)

    label("loc_658")

    Jump("loc_A04")

    label("loc_65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E5, 0)), scpexpr(EXPR_END)), "loc_746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6BF")

    ChrTalk(    #7
        0x10,
        (
            "#750FYou don't need to help with anything today. \x01",
            "Go outside and play!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_743")

    label("loc_6BF")


    ChrTalk(    #8
        0x10,
        (
            "#750FYou don't need to help me with anything today,\x01",
            "Mary.\x02\x03",

            "You're always helping out as it is. Take it easy,\x01",
            "for my sake...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_743")

    Jump("loc_90F")

    label("loc_746")


    ChrTalk(    #9
        0x10,
        (
            "#753FHello, girls.\x02\x03",

            "#751FYou both smell like you've been on the beach.\x01",
            "Have you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #10
        0x14E,
        "#1714FUmm... Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#750FI don't mind one bit if you have, you know.\x02\x03",

            "I want you to have the chance to go out and\x01",
            "play once in a while without having to worry\x01",
            "about chores.\x02\x03",

            "The weather's lovely today, too...so go out and\x01",
            "have fun, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x14E,
        (
            "#1712FO-Okay!\x02\x03",

            "(I can't let her catch on...)\x02\x03",

            "#1713F(...but I'll do as she says and play!)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F28)

    label("loc_90F")

    Jump("loc_A04")

    label("loc_912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9A2")

    ChrTalk(    #13
        0x10,
        (
            "#750FThere's a bazaar being held over in Manoria today,\x01",
            "you know.\x02\x03",

            "I'm planning to head over there and help out\x01",
            "later on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A04")

    label("loc_9A2")


    ChrTalk(    #14
        0x10,
        (
            "#750FHello, girls.\x02\x03",

            "Is something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14E,
        "#1714FNothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x14F,
        "#1732FNot at aaall.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A04")

    TalkEnd(0xFE)
    Return()

    # Function_3_2E6 end

    def Function_4_A08(): pass

    label("Function_4_A08")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-3160, 400, 13640, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(50000, 0)
    OP_6E(272, 0)
    OP_4A(0x10, 255)
    SetChrPos(0x10, -4100, 0, 14380, 0)
    OP_43(0x10, 0x1, 0x0, 0x6)
    SetChrPos(0x14E, -600, 0, 4320, 0)
    FadeToBright(2000, 0)

    def lambda_A8D():
        OP_6B(2760, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_A8D)

    def lambda_A9D():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A9D)
    OP_0D()
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)

    def lambda_AB8():
        OP_8E(0xFE, 0xFFFFF4AC, 0x0, 0x2F80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_AB8)
    WaitChrThread(0x14E, 0x1)
    Sleep(200)

    ChrTalk(    #17
        0x14E,
        "#1718FLet me help you with the cooking, Matron.\x02",
    )

    CloseMessageWindow()

    def lambda_B12():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B12)
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "#751FOh, that's quite all right, Mary. I'll be fine.\x02\x03",

            "#750FIt's good for you to rest up once in a while.\x01",
            "I'm always burdening you by having you help\x01",
            "me and take care of the children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14E,
        (
            "#1714FTh-That's not true...\x02\x03",

            "#1710FIt's not a burden at all. I'm happy to help.\x02\x03",

            "Besides, I am the oldest one here. It's only\x01",
            "right that I help out wherever I can.\x02\x03",

            "#1719FI can't sit around doing nothing when Kloe's\x01",
            "so busy in Grancel, either!\x02\x03",

            "#1718FHmm... Well, if you don't need help with the\x01",
            "cooking...I'll go and clean our room!\x02\x03",

            "#1710FClem went and messed it all up again this\x01",
            "morning, so it could probably stand to be\x01",
            "tidied up some.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x14E, 0x1, 0x0, 0x5)
    Sleep(500)

    ChrTalk(    #20 op#A
        0x10,
        "#753F#20AOh, wait...\x02",
    )

    Sleep(2000)
    OP_56(0x0)
    WaitChrThread(0x14E, 0x1)
    OP_22(0x191, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x5)
    Sleep(1000)
    OP_63(0x14E)
    OP_8C(0x14E, 180, 500)
    Sleep(200)

    ChrTalk(    #21
        0x14E,
        (
            "#1714FHmm? What was that?\x02\x03",

            "I hope Daniel didn't try and water the chickens\x01",
            "instead of the plants...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x14E, 315, 500)

    ChrTalk(    #22
        0x14E,
        "#1710FI'll go and take a look just in case!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 500)

    ChrTalk(    #23
        0x14E,
        "#1710FWhew... So much to do, so much to do...\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_EF2():
        OP_8E(0xFE, 0xFFFFFBC8, 0x0, 0xFFFFFB8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_EF2)
    Sleep(2000)
    OP_63(0x14E)

    def lambda_F15():
        OP_6D(-3000, 400, 14280, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_F15)
    Sleep(2000)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #24
        0x10,
        (
            "#754F*sigh* I appreciate that she's always doing so much\x01",
            "to try and help out...\x02\x03",

            "...but I can't help but feel that she's overworking\x01",
            "herself a little lately...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF6():
        OP_6B(2460, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_FF6)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_A08 end

    def Function_5_101D(): pass

    label("Function_5_101D")

    Sleep(300)
    OP_8C(0x14E, 180, 500)

    def lambda_102F():
        OP_6D(-3160, 400, 12140, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_102F)

    def lambda_1047():
        OP_8E(0xFE, 0xFFFFF4AC, 0x0, 0x2580, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_1047)
    WaitChrThread(0x14E, 0x2)

    def lambda_1067():
        OP_8E(0xFE, 0xFFFFFBC8, 0x0, 0x2580, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_1067)
    WaitChrThread(0x14E, 0x2)
    Return()

    # Function_5_101D end

    def Function_6_1082(): pass

    label("Function_6_1082")

    Sleep(1000)

    def lambda_108D():
        OP_8E(0xFE, 0xFFFFEB10, 0x0, 0x3890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_108D)
    WaitChrThread(0x10, 0x2)
    OP_8C(0x10, 0, 500)
    Sleep(1500)

    def lambda_10B9():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0x37C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_10B9)
    WaitChrThread(0x10, 0x2)
    OP_8C(0x10, 0, 500)
    Return()

    # Function_6_1082 end

    SaveToFile()

Try(main)
