from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5408   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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


    DeclActor(
        TriggerX            = 4670,
        TriggerZ            = 0,
        TriggerY            = -64739,
        TriggerRange        = 1000,
        ActorX              = 4670,
        ActorZ              = 2000,
        ActorY              = -64739,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_10A",          # 01, 1
        "Function_2_13F",          # 02, 2
        "Function_3_F51",          # 03, 3
        "Function_4_F76",          # 04, 4
        "Function_5_F9B",          # 05, 5
        "Function_6_FC0",          # 06, 6
        "Function_7_FE5",          # 07, 7
        "Function_8_1203",         # 08, 8
        "Function_9_1485",         # 09, 9
        "Function_10_1613",        # 0A, 10
        "Function_11_176E",        # 0B, 11
        "Function_12_1884",        # 0C, 12
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_E6"),
        (SWITCH_DEFAULT, "loc_ED"),
    )


    label("loc_E6")

    Event(0, 9)
    Jump("loc_ED")

    label("loc_ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_109")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_109")

    Return()

    # Function_0_CE end

    def Function_1_10A(): pass

    label("Function_1_10A")

    OP_1B(0x3, 0x0, 0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_12D")
    OP_71(0x404, 0x0)
    ExitThread()

    label("loc_12D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E")

    Return()

    # Function_1_10A end

    def Function_2_13F(): pass

    label("Function_2_13F")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -160, 0, -34200, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4")
    SetChrPos(0xEF, 870, 0, -34950, 180)
    SetChrPos(0xF0, 1720, 0, -34090, 180)
    SetChrPos(0xF1, 810, 0, -33230, 180)
    Jump("loc_229")

    label("loc_1A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8")
    SetChrPos(0xF0, 870, 0, -34950, 180)
    SetChrPos(0xEF, 1720, 0, -34090, 180)
    SetChrPos(0xF1, 810, 0, -33230, 180)
    Jump("loc_229")

    label("loc_1E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229")
    SetChrPos(0xF1, 870, 0, -34950, 180)
    SetChrPos(0xEF, 1720, 0, -34090, 180)
    SetChrPos(0xF0, 810, 0, -33230, 180)

    label("loc_229")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(1120, 400, -34000, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(32000, 0)
    OP_6E(332, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_398():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_398)

    def lambda_3AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3AA)

    def lambda_3BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3BC)

    def lambda_3CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3CE)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_423")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A")

    label("loc_423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A")

    label("loc_44B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A")

    label("loc_473")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_48A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B7")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51E")

    label("loc_4B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51E")

    label("loc_4DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_507")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51E")

    label("loc_507")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_51E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5B2")

    label("loc_54B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5B2")

    label("loc_573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5B2")

    label("loc_59B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5B2")

    Sleep(1000)

    ChrTalk(    #0
        0x102,
        "#1506F#5PWhy here...?!\x02",
    )

    CloseMessageWindow()
    OP_1D(0xEA)
    Sleep(300)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_6D(1510, 0, -33570, 0)
    OP_67(0, 8440, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(466, 0)

    def lambda_627():
        OP_6D(8039, -23200, -45530, 10000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_627)

    def lambda_63F():
        OP_67(0, 9560, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_63F)

    def lambda_657():
        OP_6B(12760, 10000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_657)

    def lambda_667():
        OP_6E(583, 10000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_667)
    OP_C8(0x200, 0x46, "C_PLAC36._CH", 0x0, 0xDAC)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_717")

    def lambda_69F():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFF5D8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_69F)
    Sleep(150)

    def lambda_6BF():
        OP_8F(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF5D94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6BF)
    Sleep(250)

    def lambda_6DF():
        OP_8F(0xFE, 0x60E, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6DF)
    Sleep(150)

    def lambda_6FF():
        OP_8F(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_6FF)
    Jump("loc_82C")

    label("loc_717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A3")

    def lambda_72B():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFF5D8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_72B)
    Sleep(150)

    def lambda_74B():
        OP_8F(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF5D94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_74B)
    Sleep(250)

    def lambda_76B():
        OP_8F(0xFE, 0x60E, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_76B)
    Sleep(150)

    def lambda_78B():
        OP_8F(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_78B)
    Jump("loc_82C")

    label("loc_7A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82C")

    def lambda_7B7():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFF5D8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_7B7)
    Sleep(150)

    def lambda_7D7():
        OP_8F(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF5D94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7D7)
    Sleep(250)

    def lambda_7F7():
        OP_8F(0xFE, 0x60E, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7F7)
    Sleep(150)

    def lambda_817():
        OP_8F(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_817)

    label("loc_82C")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_43(0xEE, 0x0, 0x0, 0x3)
    OP_43(0xEF, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    WaitChrThread(0xEE, 0x1)
    Sleep(1000)
    Sleep(300)
    Fade(1000)
    SetMapFlags(0x10)
    OP_6D(1500, 0, -40100, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_973")

    ChrTalk(    #1
        0x110,
        (
            "#1306F#5PThe Glorious, huh?\x02\x03",

            "So much for the Crimson Ark... Now it's\x01",
            "all black like a nasty crow.\x02\x03",

            "#261FHeehee. Maybe it ate something burned\x01",
            "and changed its color?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EA")

    label("loc_973")


    ChrTalk(    #2
        0x109,
        (
            "#1065F#5PSo our next area's the Glorious, huh?\x02\x03",

            "#1063FOr rather, a version of it that's black instead\x01",
            "of crimson.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF4")

    ChrTalk(    #3
        0x101,
        (
            "#1002F#5PW-Well, I see why they called it the 'black ark'\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1505F#5PIt looks like it's the same size as the original\x01",
            "Glorious. It has the same layout, too.\x02\x03",

            "#1502FWe can't be sure until we actually go inside\x01",
            "and look around, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E08")

    label("loc_AF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFD")

    ChrTalk(    #5
        0x10B,
        (
            "#212F#5PW-Well, I see why they called it the 'black ark'\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1505F#5PIt looks like it's the same size as the original\x01",
            "Glorious. It has the same layout, too.\x02\x03",

            "#1502FWe can't be sure until we actually go inside\x01",
            "and look around, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E08")

    label("loc_BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D04")

    ChrTalk(    #7
        0x102,
        (
            "#1505F#5PWell, at least we know what the 'black ark'\x01",
            "was referring to now.\x02\x03",

            "#1502FIt looks like it's the same size as the original\x01",
            "Glorious. It has the same layout, too.\x02\x03",

            "We can't be sure until we actually go inside\x01",
            "and look around, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E08")

    label("loc_D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E08")

    ChrTalk(    #8
        0x102,
        (
            "#1505F#5PWell, at least we know what the 'black ark'\x01",
            "was referring to now.\x02\x03",

            "#1502FIt looks like it's the same size as the original\x01",
            "Glorious. It has the same layout, too.\x02\x03",

            "We can't be sure until we actually go inside\x01",
            "and look around, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E08")


    ChrTalk(    #9
        0x109,
        (
            "#1841F#5PThis looks like it's gonna be a barrel of laughs...\x01",
            "although we should've figured as much since it's\x01",
            "our last area to go through and all.\x02\x03",

            "#1063FIt'll most likely be full of Ouroboros archaisms\x01",
            "just like the laboratory was, too.\x02\x03",

            "You know the drill. Guards up, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1500F#5PGot it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B23)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_28(0x3A, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_13F end

    def Function_3_F51(): pass

    label("Function_3_F51")

    Sleep(400)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_F51 end

    def Function_4_F76(): pass

    label("Function_4_F76")

    Sleep(200)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 15, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_F76 end

    def Function_5_F9B(): pass

    label("Function_5_F9B")

    Sleep(600)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_F9B end

    def Function_6_FC0(): pass

    label("Function_6_FC0")

    Sleep(300)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_FC0 end

    def Function_7_FE5(): pass

    label("Function_7_FE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1000, 2650, -37750, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(0, 0)
    OP_6E(341, 0)

    def lambda_1048():
        OP_6D(1000, 4550, -23050, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1048)

    def lambda_1060():
        OP_67(0, 3810, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1060)

    def lambda_1078():
        OP_6B(2900, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1078)

    def lambda_1088():
        OP_6C(0, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1088)

    def lambda_1098():
        OP_6E(350, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1098)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    Fade(1000)

    def lambda_10C1():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10C1)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_35(0xA, 0x113)
    OP_BB(0xA, 0x6, 0x113)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1141")

    AnonymousTalk(    #11
        (
            "\x07\x05Josette learned the S-Craft\x01",
            "\x07\x02[Bobcat 2]\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1177")

    label("loc_1141")


    AnonymousTalk(    #12
        "\x07\x05Josette's \x07\x02[Bobcat]\x07\x05 S-Craft was strengthened.\x02",
    )

    CloseMessageWindow()

    label("loc_1177")

    OP_22(0x21E, 0x0, 0x64)

    AnonymousTalk(    #13
        (
            "\x07\x05The support of Don and Kyle lets the Bobcat fire\x01",
            "a powerful missile in addition to its gatling guns.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5406   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_FE5 end

    def Function_8_1203(): pass

    label("Function_8_1203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D2")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(7168)
    Sleep(500)
    Jump("loc_12D5")

    label("loc_12D2")

    TalkBegin(0xFF)

    label("loc_12D5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1454")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_136D"),
        (1, "loc_13E8"),
        (2, "loc_1416"),
        (SWITCH_DEFAULT, "loc_1444"),
    )


    label("loc_136D")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xEA)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1451")

    label("loc_13E8")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1451")

    label("loc_1416")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_1451")

    label("loc_1444")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1451")

    label("loc_1451")

    Jump("loc_1311")

    label("loc_1454")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1481")
    OP_A2(0x259E)
    EventEnd(0x1)
    Jump("loc_1484")

    label("loc_1481")

    TalkEnd(0xFF)

    label("loc_1484")

    Return()

    # Function_8_1203 end

    def Function_9_1485(): pass

    label("Function_9_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1496")
    Call(0, 2)
    Return()

    label("loc_1496")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 850, 0, -34850, 180)
    SetChrPos(0x1, 10, 0, -34040, 180)
    SetChrPos(0x2, 1640, 0, -34010, 180)
    SetChrPos(0x3, 810, 0, -33180, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 11)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_1485 end

    def Function_10_1613(): pass

    label("Function_10_1613")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 850, 0, -34850, 0)
    SetChrPos(0x2, 10, 0, -34040, 0)
    SetChrPos(0x1, 1640, 0, -34010, 0)
    SetChrPos(0x0, 810, 0, -33180, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 12)
    NewScene("ED6_DT21/M4110   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1613 end

    def Function_11_176E(): pass

    label("Function_11_176E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1797")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_178B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_178B)

    label("loc_1797")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C0")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_17B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_17B4)

    label("loc_17C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E9")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_17DD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_17DD)

    label("loc_17E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1812")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1806():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1806)

    label("loc_1812")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183E")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_183E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1855")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1855")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186C")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_186C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1883")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1883")

    Return()

    # Function_11_176E end

    def Function_12_1884(): pass

    label("Function_12_1884")


    def lambda_188A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_188A)

    def lambda_189C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_189C)

    def lambda_18AE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_18AE)

    def lambda_18C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_18C0)
    Sleep(1000)
    Return()

    # Function_12_1884 end

    SaveToFile()

Try(main)
